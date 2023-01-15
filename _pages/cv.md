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

* Bachelor of Computer Science, Auburn University, 2026 (expected)
* Associate of Science in Computer Science & Programming, Wallace State Community College, 2023 (expected)

Relevant Experience
===================

* Senior Linux System Administrator - Retail DevOps & Hardware @ *O'Reilly Auto Parts*
  - Administered multiple petabyte-scale storage systems and computational infrastructure at scale
  - Maintained large-scale distrubuted production and test systems using Ansible and Terraform
  - Created a Zabbix query system using Starlite API to allow business users to query aggregate data for 14,000 hosts
  - Support production Ubuntu/RHEL servers with VMware vSphere, vSAN, Docker, and IaC
  - Stack: Python, Django, FastAPI, Bash, MySQL, PostreSQL, Terraform, Ansible, Vagrant, Agile, Atlassian, Jenkins
  - Software development using best practices of
    the full software development life cycle, including coding standards,
    code reviews, source control, testing, build and release engineering
    processes with focus on automation and end to end traceability.
  - View more about the [tech and skills I use daily here](https://www.linkedin.com/in/jacobcoffee).
* IT Specialist - IT Infrastructure & Business Continuity - Mar 2018 - Present @ *Labcorp*

  * Duties included: Windows & Linux Systems Administration, Network Administration, Tier 2 End User Support for 6 States & Puerto Rico, Project Management, and Task Automation.
  * Azure and Active Directory Management, Group Policy (GPO) Configuration, O365 Administration
* Systems Architect - May 2018 - Present @ *Homelab*

  * Built, automated, and mainted production-level systems solely for the purpose of learning and enjoying the technology
  * Systems include:
    * VMWare suite (vSphere including ESXi, vRealize)
      * Other virtualization/hypervisor solutions used include Proxmox, Citrix, Hyper-V, and SUSE Harvester.
    * Other virtualization/hypervisor solutions used include Proxmox, Citrix, Hyper-V, and SUSE Harvester.
    * Docker
    * Linux Servers running Ubuntu, RHEL (CentOS), Rocky Linux.
    * Automation using Ansible, Rancher, and Kubernetes (k3s).
    * Windows Servers performing ADFS, ADDS, DNS, DHCP, Group Policy, Azure AD sync, SCCM, and more.
    * Hardware that includes Cisco Switches, Ubiquiti switches and routers, and Dell and HP servers.
    * Networking providing RADIUS, Remote User VPN, VLANs, firewall, and IDS/IPS services.
    * Currently learning/improving on Ansible, Kubernetes, SCCM, and Python.

Skills
======

* Languages
  * Java, Powershell, Bash, Python, SQL
* Languages I am Excited to Learn
  * Rust
* Frameworks and Libraries I am Eager to Learn
  * Node.js, Gradle, Maven, TailwindCSS, Starlite (Akin to FastAPI)
* Tools
  * Git, Linux, Docker, AWS/GCP/Azure, Atlassian Stack, Active Directory, Group Policy, VMWare stack, Ansible, LXD/LXC
* Tools I am Excited to Learn
  * CI/CD (Jenkins, Travis/CircleCI), Kubernetes, Container Orchestration, Jenkins

Projects
========

Xpress Order Management | Web app for teams across the nation to order tests

* Developed and deployed multi-environment (Dev/QA/Prod) Flask web app
* Integrated LDAP and OAuth authentication, registration, tiered permissions, and password reset
* Implemented Docker containerization to deploy at scale with NGINX and Gunicorn
* Utilized Bootstrap along with Jinja2 to dynamically update the data and UI
* Designed a complex databases with SQLite, PostgreSQL, order data, and permissions
* Building reporting dashboard for national teams to understand their workloads, business cost, and patient data

Homelab | VMWare vSphere, Active Directory, Linux, Docker, Azure

* Designed, deployed, and maintained production-level systems solely for the purpose of learning more about them
* Designed systems around hardware constrains (Dell R510, R620, R430s) in a highly available 8 node cluster
  utilizing vSphere, IPMI, Reverse Proxy with NGINX, and container deployment and management
* Implemented Docker containerization for individual services with source-controlled configuration
* Designed networks with multiple VLANs for segmentation of services such as IoT, Servers, End Users, and Security
* Automated various deployments using Powershell and Bash
* Provides various services including OpenID (OAuth2), public and intranet web hosting, NAS storage, VDI remote environments, logging and monitoring with tools like Grafana, Elasticsearch, and logstash, and much more

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
