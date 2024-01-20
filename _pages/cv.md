---
layout: archive
title: "Resume"
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---

> I'm a PhD student at the University of Technology Sydney (UTS), sponsored by TPG Telecom. \
> **[Download my Resume here](https://zhangzihangit.github.io/files/zihan_zhang_resume.pdf "download"){:target="_blank"}**

## 📚 Education
---

### University of Technology Sydney

<p>PhD in Engineering and IT &nbsp;&nbsp; ⏲️  <em>Mar 2021 - Present</em></p>

- Natural language processing
- Machine learning

### University of Melbourne

<p>Master in Software Engineering &nbsp;&nbsp; ⏲️  <em>Jul 2018 - Dec 2020</em></p>

- GPA: 83/100 (First Class Honours/Distinction)
- **Awards:**
  - Dean’s Honour List, 2019 & 2020
  - Liz Haywood Awards for Best Software Engineering Team, 2020
- **Activities:**
  - Member of Computing & Information Systems Students Association (CISSA)
 
### University of British Columbia

<p>Summer Exchange Program in Computer Science &nbsp;&nbsp; ⏲️  <em>Jul 2017 - Aug 2017</em></p>

- Algorithms and data structures
- Web design and programming

### China Pharmaceutical University

<p>Bachelor in Information System and Information Management &nbsp;&nbsp; ⏲️  <em>Sep 2014- Jun 2018</em></p>

- GPA: 82/100 (Ranking: 25/143)
- **Awards:**
    - Excellent Volunteer (2015-2016)
    - Second-Class Scholarship (2016-2017)
- **Activities:**
    - Chairman of the Faculty of Science Student Union (2016-2017)
  
## 📑 Publications
---

- **How Do Large Language Models Capture the Ever-changing World Knowledge? A Review of Recent Advances** \
**Zihan Zhang**\*, Meng Fang\*, Ling Chen, Mohammad-Reza Namazi-Rad, Jun Wang \
Conference on Empirical Methods in Natural Language Processing (***EMNLP***), 2023 \
<a href="https://arxiv.org/abs/2310.07343" target="_blank"><i class="fa-regular fa-file-pdf"></i></a> &nbsp; <a href="https://github.com/hyintell/awesome-refreshing-llms" target="_blank"><i class="fa-brands fa-github"></i></a> &nbsp;

- **Turn-Level Active Learning for Dialogue State Tracking** \
**Zihan Zhang**, Meng Fang, Ling Chen, Mohammad-Reza Namazi-Rad \
Conference on Empirical Methods in Natural Language Processing (***EMNLP***), 2023 \
<a href="https://arxiv.org/abs/2310.14513" target="_blank"><i class="fa-regular fa-file-pdf"></i></a> &nbsp; <a href="https://github.com/hyintell/AL-DST" target="_blank"><i class="fa-brands fa-github"></i></a> &nbsp;

- **CITB: A Benchmark for Continual Instruction Tuning** \
**Zihan Zhang**, Meng Fang, Ling Chen, Mohammad-Reza Namazi-Rad \
Conference on Empirical Methods in Natural Language Processing (***EMNLP, Findings***), 2023 \
<a href="https://arxiv.org/abs/2310.14510" target="_blank"><i class="fa-regular fa-file-pdf"></i></a> &nbsp; <a href="https://github.com/hyintell/CITB" target="_blank"><i class="fa-brands fa-github"></i></a> &nbsp;

- **Is Neural Topic Modelling Better than Clustering? An Empirical Study on Clustering with Contextual Embeddings for Topics** \
**Zihan Zhang**, Meng Fang, Ling Chen, Mohammad-Reza Namazi-Rad \
Annual Conference of the North American Chapter of the Association for Computational Linguistics (***NAACL***), 2022 \
<a href="https://arxiv.org/abs/2204.09874" target="_blank"><i class="fa-regular fa-file-pdf"></i></a> &nbsp; <a href="https://github.com/hyintell/topicx" target="_blank"><i class="fa-brands fa-github"></i></a> &nbsp;


## 👩🏻‍💻 Work Experience
---

### Research Analyst

<p>TPG Telecome &nbsp;&nbsp; <em>Sydney, Australia</em>  &nbsp;&nbsp; ⏲️  <em>Mar 2021 - Present</em></p>

As a part of the Data and Analytics Centre of Excellence (CoE) team, I transform numerous data into actionable insights.
- [**NPS**](https://en.wikipedia.org/wiki/Net_Promoter){:target="_blank"} topic modelling - extract keywords from customers' feedback and study why the customers are satisfying/unsatisfying.
- **Market offer text extraction** - extract and analyse competitors' offers, transform from raw images to structured data that the market team could use.
- **Business Insights analysis** - model and analysis customers churn and upgrade
- **AWS ML pipeline**

### Front-End Developer Intern

<p>RESORTer &nbsp;&nbsp; <em>Melbourne, Australia </em>  &nbsp;&nbsp; ⏲️  <em>Nov 2019 - Mar 2020</em></p>

I was responsible for refactoring and developing the Lesson Section in the Web application.

- Refactored the Lesson Section using React + Hooks + Material-UI. Used Grid layout and Card component to render different kinds of lessons and simplified the rendering logic, which was a serious issue when using the Tabs system.
- Managed the global state using Redux and created default lessons for the users based on the form they filled. I also cooperated with my team using Middleware to catch and handle certain actions to ensure the generated lessons are always consistent with the global state, thereby improving the user experience.
- Utilized CSS Module to avoid class names collisions and global style pollution. Used lazy load to dynamically import required components, thereby improving the performance.


## 🏗️ Projects
---

### 🔧 [Algorithms in Action](/project/algorithms-in-action)

*March 2020 - October 2020*

> **Try AiA demo here: [https://algorithms-in-action.github.io/](https://algorithms-in-action.github.io/){:target="_blank"}** \
> **Github: [https://github.com/algorithms-in-action/algorithms-in-action.github.io](https://github.com/algorithms-in-action/algorithms-in-action.github.io){:target="_blank"}{:target="_blank"}**

An algorithm visualization Web application provided for the first year Computer Science students.
I was responsible for implementing the pseudocode and algorithm animation.

- Using JavaScript function closures, all the visualization API functions and corresponding variables can be stored in an array and executed later, so it solved using ES6 `Generators` that functions executions cannot be reversed. Thereby, the animation can step backward as well.
- To map the algorithm pseudocode with the actual code, I parsed and added a bookmark in each line of the pseudocode, and inserted the bookmarks at the corresponding position in the actual code, so the pseudocode and animation can be synchronized.
- Implemented a customized hook use interval so that the auto-play function can read fresh states between each render. This hook can also detect the speed changes and reset the setInterval function, thereby adjusting the playback speed is achievable.
- Based on the visualization APIs provided by `[Tracer.js](https://github.com/algorithm-visualizer/tracers.js)`, I implemented some common components and functions and expanded the library as well.

### ✏️ [Distributed Shared Whiteboard](/project/distributed_shared_whiteboard)

*August 2019 - October 2019*

> **Github: [https://github.com/ZhangzihanGit/Distributed-Shared-Whiteboard-Application](https://github.com/ZhangzihanGit/Distributed-Shared-Whiteboard-Application){:target="_blank"}**

A shared whiteboard desktop application that allows multiple users to draw shapes and chat at the same time. I was responsible for developing the client and server GUI.

- The project used Java 8 as the backend language, [JavaFX](https://openjfx.io/){:target="_blank"} as the frontend framework, and used a three-tier Client/Server architecture. It separated the client – whiteboard server – data server.
- Java RMI was used as the communication method between the whiteboard server and data server; the request sends from the client were remotely called in the whiteboard server. To synchronize each client, MQTT was used to provide a subscribe/publish protocol. The whiteboard server was used as an intermediate agent to accept messages from each client and publish the messages to all other subscribers.

### 📐 [Guttman Chart Analysis System](/project/guttman_chart_analysis_system)

*Aug 2019 - Nov 2019*

> **Github: [https://github.com/ZhangzihanGit/Guttman-Chart-Analysis-System](https://github.com/ZhangzihanGit/Guttman-Chart-Analysis-System){:target="_blank"}**

A Guttman chart based students assessment analysis system. It can be used to help educators find students’ Zones of Personal Development (ZPD) and adjust future teaching plans.

- The project provided support for the 🔗 [research](https://education.unimelb.edu.au/research/projects/improving-assessment-with-intelligent-automation){:target="_blank"} in the Assessment Research Centre, Melbourne Graduate School of Education.
- I was responsible for developing the frontend pages and integrating them with the backend developers. The project used Python as the backend programming language, adopted the Client/Server model, and used RESTful API for HTTP communication.


## ☀️ Services
---

Academic Reviewer:
- EMNLP 2022-2023
- EACL 2023
- ACL Rolling Review October, December 2023

## ⭐ Skills & Certificates

**Languages**: Mandarin (native), English (fluent) \
**Programming**: Python $\gg$ JavaScript $==$ SQL $>$ Spark $==$ Java $>$ C $==$ C++ $==$ Haskell \
**Libraries & Frameworks**: PyTorch, HuggingFace, Amazon Web Service, Databricks \
**Certificates**:
  - [AWS Cloud Practitioner](https://www.credly.com/badges/35ab6c23-ab2e-46e1-af9a-68988cd8fdda/public_url){:target="_blank"}
  - [(Databricks) Large Language Models: Application through Production](https://courses.edx.org/certificates/2e4450253cf4494d91aa796a2a3b5fda){:target="_blank"}

**Other**:
  - Git
  - CI/CD Pipelines
  - Data ETL

