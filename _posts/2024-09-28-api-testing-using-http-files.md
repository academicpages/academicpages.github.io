---
title: 'Simplify API Testing with `.http` Files in .NET 8'
date: 2024-09-28
permalink: /posts/api-testing-net8/
tags:
  - API Testing
  - .NET 8
  - .http
  - C#
---

With the release of **.NET 8**, a new type of file has been introduced in API projects — the **`.http` file**. This addition aims to make API testing faster and easier by allowing developers to write and execute HTTP requests directly within the IDE.

---

## What is a `.http` File?

The `.http` file is a **plain text file** that contains HTTP commands such as `GET`, `POST`, `PUT`, `DELETE`, and others commonly used for interacting with APIs.

Instead of relying on external tools like **Postman** or **cURL**, you can now write your HTTP requests inside this file and run them **directly in Visual Studio or VS Code**.

---

The main goal from using `.http` files is to provide a **simple, fast, and integrated** environment for testing your APIs.

- ✅ No need to switch to external tools  
- ✅ Easily maintain and share requests within your team  
- ✅ Keep test requests version-controlled inside your project

---

## Example Usage
Here’s what a basic `.http` file might look like:

```http
GET https://localhost:5000/api/products
###

POST https://localhost:5000/api/products
Content-Type: application/json

{
  "name": "Product X",
  "price": 100
}
```
Each section is separated by `###`, allowing multiple requests to be defined in one file.

---

## Working with Environments

One of the powerful features of `.http` files is environment support. You can create different environments (e.g., development, staging, production) and switch between them easily.

To do this, define an `.env` file with environment variables:
```json
{
  "dev": {
    "HostAddress": "https://localhost:5000"
  },
  "staging": {
    "HostAddress": "https://api.stg.com"
  },
  "production": {
    "HostAddress": "https://api.app.com"
  }
}
```
Then reference those variables inside your `.http` file like this:

{% raw %}
```http
GET {{HostAddress}}/api/products
```
{% endraw %}

This makes your requests portable and adaptable to different environments without changing the request logic.