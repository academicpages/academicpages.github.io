---
title: "📐 Online Examination App"
collection: projects
permalink: /project/online_examination_app
excerpt: 'A simulated Online Examination App that allows an administrator to manage different subjects, exams, instructors, and students.'
date: 2020-09-01
---

<div>
  <img src="/images/online-examination-app/oea-screenshot.png" alt="oea_homepage"> 
</div>

<!-- TOC start (generated with https://github.com/derlin/bitdowntoc) -->

- [Project Timeline](#project-timeline)
- [Project Description](#project-description)
- [Tech Stack](#tech-stack)
- [Main Features](#main-features)
  - [User Abilities](#user-abilities)
  - [Patterns Used](#patterns-used)
- [Appendix](#appendix)

<!-- TOC end -->

<!-- TOC --><a name="project-timeline"></a>

# Project Timeline

August 2020 - October 2020

> **Github: [https://github.com/ZhangzihanGit/Online-Examination-App](https://github.com/ZhangzihanGit/Online-Examination-App){:target="_blank"}**

# Project Description

This project is a simulated [Online Examination App](https://online-examination-app.herokuapp.com/){:target="_blank"} that allows an administrator to manage different subjects, exams, instructors, and students; allows instructors to `create/update/delete/publish/close/mark` exams; allows students to take exams. The application also takes care of concurrency and security issues.

This project intended to explore many patterns used in the enterprise, so no backend frameworks were used.

# Tech Stack

- **Backend**: Java Servlet + Tomcat
- **Frontend**: React + Redux
- **Security**: [Apache Shiro](https://shiro.apache.org/)
- **Database**: [PostgreSQL](https://www.postgresql.org/)

<div>
  <img src="/images/online-examination-app/oea-tomcat.png" alt="oea_tomcat"> 
</div>

# Main Features

## User Abilities

**Admin** has the ability to:

- create new subjects
- view all subjects and associated instructors, students, and exams

<div>
  <img src="/images/online-examination-app/oea-admin-view.png" alt="oea_admin"> 
</div>

<div>
  <img src="/images/online-examination-app/oea-admin-detailed-view.png" alt="oea_admin_detailed"> 
</div>

<br>

**Instructor** has the ability to:

- view subjects he/she teaches
- create/update/delete/mark/publish/close exams
- mark students' submissions in table and detailed view


<div>
  <img src="/images/online-examination-app/oea-instructor-view.png" alt="oea_instructor"> 
</div>

<div>
  <img src="/images/online-examination-app/oea-instructor-edit-exam.png" alt="oea_edit"> 
</div>

<div>
  <img src="/images/online-examination-app/oea-instructor-mark.png" alt="oea_mark"> 
</div>

<div>
  <img src="/images/online-examination-app/oea-instrcutor-detailed-mark.png" alt="oea_detailed_mark"> 
</div>

<br>

**Student** has the ability to:

- view subjects he/she enrolls
- take available exams

<div>
  <img src="/images/online-examination-app/oea-student-take-exam.png" alt="oea_student"> 
</div>

## Patterns Used

| Category                                  | Patterns                                                                                                 |
| ----------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| Organising domain logic                   | Domain model                                                                                             |
| Architecture design for data-source layer | Data mapper                                                                                              |
| Object-to-relational behavioral design    | Unit of work; Lazy load                                                                                  |
| Object-to-relational structural design    | Identity field; Foreign key mapping; Association table mapping; Embedded value; Single table inheritance |
| Concurrency                               | Pessimistic offline lock                                                                                 |
| Security                                  | Authentication enforcer; Authorisation enforcer; Secure Pipe                                             |

<br>

# Appendix

<div>
  <img src="/images/online-examination-app/oea-fullstacksoftware.png" alt="oea_fullstack"> 
</div>

> Source: [https://www3.ntu.edu.sg/home/ehchua/programming/howto/Tomcat_HowTo.html](https://www3.ntu.edu.sg/home/ehchua/programming/howto/Tomcat_HowTo.html){:target="_blank"}