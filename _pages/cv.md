---
layout: archive
title: "CV"
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---
{% include base_path %}

Resume in PDF Format: [Resume.pdf](/files/resume.pdf)

Education
=========

* Bachelor of Computer Science, Auburn University, 2024 (expected)
* Associate of Science in Computer Science & Programming, Wallace State Community College, 2022 (expected)

Relevant Experience
===================

* IT Specialist - IT Infrastructure & Business Continuity - Mar 2018 - Present
  * *Labcorp*
    * Duties included: Windows & Linux Systems Administration, Network Administration, Tier 2 End User Support for 6 States & Puerto Rico, Project Management, and Task Automation.
* Systems Architect - May 2018 - Present
  * See *Homelab* in Projects below

Skills
======

* Languages
  * Java, Powershell, Bash
* Languages I am Excited to Learn
  * Python, C++, SQL
* Frameworks and Libraries I am Eager to Learn
  * Spring, Hibernate, .NET Core, Node.js, Vue.js, React
* Tools
  * Git, Linux, Docker, AWS/GCP/Azure, Jira, Active Directory, Group Policy, VMWare vSphere
* Tools I am Excited to Learn
  * Gradle, Maven, JWT, CI/CD, Kubernetes, Container Orchestration, Jenkins, Ansible, Chef, Puppet

Projects
========

### Xpress Order Management | Web app for teams across the nation to order tests

* Developed and deployed multi-environment (Dev/QA/Prod) Flask web app
* Integrated LDAP and OAuth authentication, registration, tiered permissions, and password reset
* Implemented Docker containerization to deploy at scale with NGINX and Gunicorn
* Utilized Bootstrap along with Jinja2 to dynamically update the data and UI
* Designed a complex databases with SQLite, PostgreSQL, order data, and permissions
* Building reporting dashboard for national teams to understand their workloads, business cost, and patient data

### Homelab | Highly-available 8 node ESXi cluster managed by VMWare vSphere, Active Directory, Linux, Docker, Azure

* Designed, deployed, and maintained production-level systems solely for the purpose of learning more about them
* Designed systems around hardware constrains (Dell R510, R620, R430s) in a highly available 8 node cluster
  utilizing vSphere, IPMI, Reverse Proxy with NGINX, and container deployment and management
* Implemented Docker containerization for individual services with source-controlled configuration
* Designed networks with multiple VLANs for segmentation of services such as IoT, Servers, End Users, and Security
* Automated various deployments using Powershell and Bash

Service and leadership
======================

* Auburn Student ACM Club
* Auburn Ethical Hacking Club
* Auburn AI/Machine Learning Group
* IEEE & ACM Student Member

Publications
============

Coming Soon

<ul>{% for post in site.publications %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>

Talks
=====

Coming Soon

<ul>{% for post in site.talks %}
    {% include archive-single-talk-cv.html %}
  {% endfor %}</ul>
