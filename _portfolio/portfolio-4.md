---
title: "SQL Query"
excerpt: "Intuitive SQL Query Generator with Natural Language Processing<br/>"
collection: portfolio
---



## Overview


The Intuitive SQL Query Generator is a full-stack application that leverages the power of Natural Language Processing (NLP) to allow users to create complex SQL queries using simple, human-friendly language. The application is built using React for the front end, Node.js and Express for the backend, and integrates the ChatGPT API to process natural language input.

[Check it out on Github Here!](https://github.com/shuaibahmed01/SQL-Query-Generator)


## Features

- Generate SQL queries without any prior coding knowledge.
- User-friendly interface for entering natural language descriptions of queries.
- NLP-powered backend for converting natural language input to structured SQL queries.
- Real-time suggestions and feedback to guide users in creating accurate queries.
- Customizable query options and parameters.
- Responsive design for seamless usage on various devices.

## Technologies Used

- **Front End:** React, HTML, CSS
- **Back End:** Node.js, Express
- **NLP Integration:** OpenAI's ChatGPT API
- **Database:** (Specify if applicable, e.g., MySQL, PostgreSQL)
- **Deployment:** (Specify if applicable, e.g., Heroku, AWS, etc.)

## Installation and Usage

1. **Clone the repository:**

   ```shell
   git clone https://github.com/shuaibahmed01/SQL-Query-Generator.git
   cd SQL-Query-Generator
   ```
   
2. **Install dependencies for both the frontend and backend:**

```shell
# Install frontend dependencies
cd client
npm install

# Install backend dependencies
cd ../server
npm install
```

3. **Set up environment variables:**
Create a .env file in the backend directory and add your ChatGPT API key and any other relevant configuration:
```env
OPENAI_API_KEY= your-api-key
```
4. **Start Development Environment:**
```shell
cd client
npm run dev

cd ../server
node index.js
```