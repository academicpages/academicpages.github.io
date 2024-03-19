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

Experience
==========

* Senior Linux Systems Administrator | Feb 2022 – Present @ *O'Reilly Auto Parts* (Remote)
  - Managed petabyte-scale storage systems and computational infrastructure, ensuring seamless operations
  - Enhanced system reliability and efficiency through maintenance of distributed systems using Ansible and Terraform
  - Supported Ubuntu/RHEL servers with VMware, Containers, and IaC, optimizing server performance
  - Introduced code reviews, pull requests, code formatting, linting, and testing to users

* IT Specialist | Mar 2018 – Feb 2022 @ *Labcorp* (Remote)
  - Automated routine tasks with Python, Powershell, and Ansible, reducing downtime and increasing efficiency
  - Instituted new Active Directory GPO structure to facilitate automation
  - Managed networks using Cisco ISE, Infoblox IPAM, Velocloud Orchestrator, and Meraki dashboard

Projects
========

* Internal Apps | Highly-available APIs for 1000+ users | 2022 – Present
  - Architected and deployed a highly available internal store API and corresponding frontend
  - Developed ChatOps interfaces and automation to reduce user friction
  - Deployed load balancing and versioned multi-container deployments for application resiliency

* Homelab | vSphere, Active Directory, Linux, Docker, Azure | May 2018 – Present
  - Engineered systems around hardware constraints in an 8 node cluster
  - Implemented Docker containerization with source-controlled configuration deployed with GitOps
  - Built complex networks with VLANs for service segmentation, multi-user VPN, and IDS/IPS services

* Order Management System | Web app for pathologists' test ordering | Jan 2022 – Feb 2022
  - Deployed a multi-environment Flask web app with Docker, LDAP, OAuth authentication, and tiered permissions
  - Engineered scalable deployment with NGINX, Gunicorn, and Docker
  - Developing a reporting dashboard for national teams

Technical Skills
================

* **Languages:** Python, Bash, Java, Powershell
* **Frameworks:** Litestar, Django, Flask, Jinja2, OAuth, PostgreSQL
* **Tools:** Git, Docker, LXD/LXC, NGINX, Ansible, Azure, Prometheus, Grafana, Zabbix, OpenTelemetry
* **Operating Systems:** Windows Server (2012-2022), Ubuntu Server, Red Hat Server (RHEL/CentOS/Rocky Linux)
* **Software:** VMWare vSphere, ESXi, Proxmox, Hyper-V, GPO, ServiceNow, SCCM, Citrix
* **Currently Learning:** Kubernetes, Rancher (Harvester, k3s), Jenkins, Terraform, Rust

Open Source
===========

* [Litestar](https://github.com/litestar-org/) | Maintainer - Asynchronous Python Framework for building APIs and Web Apps | 2023 – Present
  * Contribute to the codebase for Litestar, ensuring its performance and capabilities
  * Managed complex CI pipelines, including testing, linting, and deployment
  * Collaborate on project roadmap and features, and maintain related projects like Polyfactory
  * Provide assistance and guidance within the project’s community
  * Steered Litestar organization projects, roadmap, and vision
  * Maintained priorities and relationships with user and business sponsors
  * Managed the project’s community, including contributors, users, and sponsors

* Maintainer | Powerful utilities for Python - 2023 - Present @ Jolt Organization
  * Split off popular internals from the Litestar organization projects to provide them en masse.
  * Maintained projects including a [SQLAlchemy companion library](https://github.com/jolt-org/advanced-alchemy), 
    Python runtime type introspection utility library, and more.

Projects
========

Xpress Order Management | Web app for teams across the nation to order tests

* Developed and deployed multi-environment (Dev/QA/Prod) Flask web app
* Integrated LDAP and OAuth authentication, registration, tiered permissions, and password reset
* Implemented Docker containerization to deploy at scale with NGINX and Gunicorn
* Utilized Bootstrap along with Jinja2 to dynamically update the data and UI
* Designed a complex databases with SQLite, PostgreSQL, order data, and permissions
* Built a reporting dashboard for national teams to understand their workloads, business cost, and patient data

Homelab | VMWare vSphere, Active Directory, Linux, Docker, Azure

* Designed, deployed, and maintained production-level systems solely for the purpose of learning more about them
* Designed systems around hardware constrains (Dell R510, R620, R430s) in a highly available 8-node cluster
  using vSphere, IPMI, Reverse Proxy with NGINX, and container deployment and management
* Implemented Docker containerization for individual services with source-controlled configuration
* Designed networks with multiple VLANs for segmentation of services such as IoT, Servers, End Users, and Security
* Automated various deployments using Powershell and Bash
* Provides various services including OpenID (OAuth2), 
  public and intranet web hosting, NAS storage, VDI remote environments, 
  logging and monitoring with tools like Grafana, Elasticsearch, and logstash, and much more

Education
=========

* Bachelor of Computer Science, Auburn University, 2026 (expected)
* Associate of Science in Computer Science & Programming, Wallace State Community College, 2023 (expected)

[//]: # (Service and leadership)

[//]: # (======================)

[//]: # ()
[//]: # (* Auburn Student ACM Club)

[//]: # (* Auburn Ethical Hacking Club)

[//]: # (* Auburn AI/Machine Learning Group)

[//]: # (* IEEE & ACM Student Member)

[//]: # ()
[//]: # (Publications)

[//]: # (============)

[//]: # ()
[//]: # (Coming Soon)

[//]: # ()
[//]: # (<ul>{% for post in site.publications %})

[//]: # (    {% include archive-single-cv.html %})

[//]: # (  {% endfor %}</ul>)

[//]: # ()
[//]: # (Talks)

[//]: # (=====)

[//]: # ()
[//]: # (Coming Soon)

[//]: # ()
[//]: # (<ul>{% for post in site.talks %})

[//]: # (    {% include archive-single-talk-cv.html %})

[//]: # (  {% endfor %}</ul>)
