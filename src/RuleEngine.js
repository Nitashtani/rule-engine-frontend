import React, { useState } from "react";
import axios from "axios";

const RuleEngine = () => {
  const [ruleString, setRuleString] = useState("");
  const [ruleIds, setRuleIds] = useState("");
  const [data, setData] = useState("");
  const [result, setResult] = useState(null);

  const handleCreateRule = () => {
    axios
      .post("http://127.0.0.1:5000/create_rule", { rule_string: ruleString })
      .then((response) => {
        alert(`Rule created with ID: ${response.data.id}`);
      })
      .catch((error) => {
        console.error("Error creating rule:", error);
      });
  };

  const handleCombineRules = () => {
    axios
      .post("http://127.0.0.1:5000/combine_rules", {
        rule_ids: ruleIds.split(","),
      })
      .then((response) => {
        alert(`Combined rule: ${response.data.combined_rule}`);
      })
      .catch((error) => {
        console.error("Error combining rules:", error);
      });
  };

  const handleEvaluateRule = () => {
    axios
      .post("http://127.0.0.1:5000/evaluate_rule", {
        rule_json: ruleString,
        data: JSON.parse(data),
      })
      .then((response) => {
        setResult(response.data.result);
      })
      .catch((error) => {
        console.error("Error evaluating rule:", error);
      });
  };

  return (
    <div>
      <h1>Rule Engine</h1>
      <div>
        <h2>Create Rule</h2>
        <input
          type="text"
          value={ruleString}
          onChange={(e) => setRuleString(e.target.value)}
          placeholder="Enter rule string"
        />
        <button onClick={handleCreateRule}>Create Rule</button>
      </div>
      <div>
        <h2>Combine Rules</h2>
        <input
          type="text"
          value={ruleIds}
          onChange={(e) => setRuleIds(e.target.value)}
          placeholder="Enter rule IDs (comma separated)"
        />
        <button onClick={handleCombineRules}>Combine Rules</button>
      </div>
      <div>
        <h2>Evaluate Rule</h2>
        <input
          type="text"
          value={data}
          onChange={(e) => setData(e.target.value)}
          placeholder="Enter data (JSON)"
        />
        <button onClick={handleEvaluateRule}>Evaluate Rule</button>
        {result !== null && <p>Result: {result.toString()}</p>}
      </div>
    </div>
  );
};

export default RuleEngine;
