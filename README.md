# Getting Started with Create React App

This project was bootstrapped with [Create React App](https://github.com/facebook/create-react-app).

## Available Scripts

In the project directory, you can run:

### `npm start`

Runs the app in the development mode.\
Open (https://nitashtani.github.io/rule-engine-frontend/) to view it in your browser.

The page will reload when you make changes.\
You may also see any lint errors in the console.

### `npm test`

Launches the test runner in the interactive watch mode.\
See the section about [running tests](https://facebook.github.io/create-react-app/docs/running-tests) for more information.

### `npm run build`

Builds the app for production to the `build` folder.\
It correctly bundles React in production mode and optimizes the build for the best performance.

The build is minified and the filenames include the hashes.\
Your app is ready to be deployed!

See the section about [deployment](https://facebook.github.io/create-react-app/docs/deployment) for more information.

### `npm run eject`

**Note: this is a one-way operation. Once you `eject`, you can't go back!**

If you aren't satisfied with the build tool and configuration choices, you can `eject` at any time. This command will remove the single build dependency from your project.

Instead, it will copy all the configuration files and the transitive dependencies (webpack, Babel, ESLint, etc) right into your project so you have full control over them. All of the commands except `eject` will still work, but they will point to the copied scripts so you can tweak them. At this point you're on your own.

You don't have to ever use `eject`. The curated feature set is suitable for small and middle deployments, and you shouldn't feel obligated to use this feature. However we understand that this tool wouldn't be useful if you couldn't customize it when you are ready for it.

## Learn More

You can learn more in the [Create React App documentation](https://facebook.github.io/create-react-app/docs/getting-started).

To learn React, check out the [React documentation](https://reactjs.org/).

### Code Splitting

This section has moved here: [https://facebook.github.io/create-react-app/docs/code-splitting](https://facebook.github.io/create-react-app/docs/code-splitting)

### Analyzing the Bundle Size

This section has moved here: [https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size](https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size)

### Making a Progressive Web App

This section has moved here: [https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app](https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app)

### Advanced Configuration

This section has moved here: [https://facebook.github.io/create-react-app/docs/advanced-configuration](https://facebook.github.io/create-react-app/docs/advanced-configuration)

### Deployment
# 3-Tier Rule Engine Application

## Overview

This repository contains a 3-tier rule engine application designed to manage and apply business rules to data. The application is structured into three layers:

1. **Presentation Layer**: Handles user interactions and displays results.
2. **Application Layer**: Manages business logic and rule processing.
3. **Data Layer**: Handles data storage and retrieval.

## Architecture

### 1. Presentation Layer

- **Frontend**: Built using React.js for a responsive and interactive user interface.
- **Endpoints**: Exposes RESTful APIs for communication with the Application Layer.

### 2. Application Layer

- **Business Logic**: Implements the core rule engine logic.
- **Rule Management**: Allows dynamic addition, modification, and deletion of rules.
- **API Endpoints**: Provides RESTful APIs for the Presentation Layer and interacts with the Data Layer.

### 3. Data Layer

- **Database**: Uses PostgreSQL for robust and scalable data storage.
- **ORM**: Implements an Object-Relational Mapping (ORM) layer for efficient data manipulation.

## Technologies Used

- **Frontend**: React.js, Axios, Redux (for state management)
- **Backend**: Node.js, Express.js
- **Database**: PostgreSQL
- **ORM**: Sequelize
- **Deployment**: Docker, Kubernetes

## Setup and Installation

### Prerequisites

- Node.js (v14.x or later)
- PostgreSQL (v12.x or later)
- Docker (optional, for containerization)

### Steps

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/rule-engine-app.git
   cd rule-engine-app
