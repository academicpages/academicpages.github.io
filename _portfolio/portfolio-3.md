---
title: "[CSE4110] Database-Systems Individual Projects"
excerpt: "Real Estate Database Management Program<br/>"
semester: "Spring-2024"
collection: portfolio
---

## 🏢 Project Overview

This project aimed to develop a complete real estate database management system that tracks agents, properties, and sales using an end-to-end approach. Beginning with ERD and BCNF normalization, the system was implemented through C++ and MySQL integration using ODBC.  
Led the individual project, responsible for ER schema design, data modeling, query logic, implementation of a program, and final report compilation.

## 🧱 System Design

- Conceptual Modeling: Entity-Relationship diagram reflecting realistic business rules (agent, buyer, seller, property, photo, sold)
- Logical Schema: Relations normalized into **BCNF**, with attention to domain-specific constraints
- Physical Schema: Implemented in **Erwin** with detailed data types and nullability control
- Implementation Language: **C++ with MySQL ODBC Driver**
- Platform: Windows + Visual Studio 2019 + MySQL 8.x

## 🛠️ Features

- **C++ Program with User Interface**  
  - Console-based UI for running 13 types of structured queries (e.g., most expensive property, top agents, listing properties by area/price, etc.)
  - Submenu & input validation for parameterized queries  
- **Query Support Highlights**  
  - Find homes by district, price range, or school zone  
  - Rank agents by sales value (top-K, bottom 10%)  
  - Average time on the market, average selling price per agent  
  - Visual output of property photos per housing type  

## 📐 Sample Schema Elements

- Tables: `property`, `photo`, `sold`, `agent`, `buyer`, `seller`
- Types: `DECIMAL`, `VARCHAR`, `DATE` with primary and foreign key constraints
- Enforced constraints such as one interior photo per studio/one-bedroom, one exterior + floor plan for larger homes

## 💬 Technologies Used

- `C++`, `ODBC`, `MySQL`, `Visual Studio 2019`, `Erwin Data Modeler`
- SQL Query processing using `snprintf` + `mysql_query()` + `mysql_store_result()`

## 📎 Download Project Documents
📄 [Download Project2 Guide](/files/project2(spring2024).pdf) <br/>
📄 [Download System Specification (project2_system_guide)](/files/project2_system_guide(spring2024).pdf)  <br/>
📄 [Download Mid Report: Primary ER design of the Real Estate](/files/[project1]20190741.pdf) <br/>
📄 [Download Final Report](/files/[project2]20190741.pdf) <br/>
