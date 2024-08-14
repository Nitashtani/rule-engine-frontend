class Node:
    def __init__(self, type, left=None, right=None, value=None):
        self.type = type
        self.left = left
        self.right = right
        self.value = value

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///rules.db'
db = SQLAlchemy(app)

class Rule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rule_json = db.Column(db.Text, nullable=False)

db.create_all()

class Node:
    def __init__(self, type, left=None, right=None, value=None):
        self.type = type
        self.left = left
        self.right = right
        self.value = value

def parse_rule(rule_string):
    # Simplified parser for demonstration purposes
    # This should be replaced with a proper parser
    if 'AND' in rule_string:
        left, right = rule_string.split(' AND ', 1)
        return Node('operator', left=parse_rule(left), right=parse_rule(right), value='AND')
    elif 'OR' in rule_string:
        left, right = rule_string.split(' OR ', 1)
        return Node('operator', left=parse_rule(left), right=parse_rule(right), value='OR')
    else:
        return Node('operand', value=rule_string)

def evaluate_rule(node, data):
    if node.type == 'operator':
        if node.value == 'AND':
            return evaluate_rule(node.left, data) and evaluate_rule(node.right, data)
        elif node.value == 'OR':
            return evaluate_rule(node.left, data) or evaluate_rule(node.right, data)
    elif node.type == 'operand':
        # Simplified evaluation for demonstration purposes
        # This should be replaced with a proper evaluator
        key, op, value = node.value.split(' ')
        key = key.strip()
        value = value.strip("'")
        if op == '>':
            return data.get(key, 0) > int(value)
        elif op == '<':
            return data.get(key, 0) < int(value)
        elif op == '=':
            return data.get(key, '') == value
    return False

@app.route('/create_rule', methods=['POST'])
def create_rule():
    rule_string = request.json.get('rule_string')
    node = parse_rule(rule_string)
    rule_json = json.dumps(node, default=lambda o: o.__dict__)
    new_rule = Rule(rule_json=rule_json)
    db.session.add(new_rule)
    db.session.commit()
    return jsonify({'id': new_rule.id})

@app.route('/combine_rules', methods=['POST'])
def combine_rules():
    rule_ids = request.json.get('rule_ids')
    rules = Rule.query.filter(Rule.id.in_(rule_ids)).all()
    combined_node = None
    for rule in rules:
        node = json.loads(rule.rule_json, object_hook=lambda d: Node(**d))
        if combined_node is None:
            combined_node = node
        else:
            combined_node = Node('operator', left=combined_node, right=node, value='OR')
    combined_json = json.dumps(combined_node, default=lambda o: o.__dict__)
    return jsonify({'combined_rule': combined_json})

@app.route('/evaluate_rule', methods=['POST'])
def evaluate_rule_endpoint():
    rule_json = request.json.get('rule_json')
    data = request.json.get('data')
    node = json.loads(rule_json, object_hook=lambda d: Node(**d))
    result = evaluate_rule(node, data)
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)