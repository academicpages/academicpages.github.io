---
layout: archive
title: ""
permalink: /cs6604FA23/
author_profile: true
---


# 🤖 CS 6604: Embodied Artificial Intelligence (Fall 2023) 

👩🏻‍🏫 Instructor: [Ismini Lourentzou](https://isminoula.github.io/)

🏫 Meeting time: Tuesdays and Thursdays, 9:30 AM - 10:45 AM EST, McBryde Hall 232 and [Zoom](https://virginiatech.zoom.us/j/83632738882)

🕦 Office hours:  Tuesdays and Thursdays, 11:00 AM - 12:00 PM EST, [Zoom](https://virginiatech.zoom.us/j/87481223897)

📚 [Reading List](/readings)

## Course Description 
Embodied Artificial Intelligence (E-AI) is a rapidly advancing field that aims to develop intelligent agents that can perceive and act 
in the physical world through sensors and actuators and learn from their experiences in completing various physical tasks. In an era where 
AI systems are increasingly expected to interact with the world in a human-like manner, E-AI offers a promising approach. 
By integrating intelligence with physicality, AI systems gain a deeper understanding of visual perception, language comprehension, 
and multimodal interactions. 

This is an immersive seminar course that offers a unique opportunity to explore the cutting-edge intersection of embodied AI, 
computer vision, and natural language processing (NLP). The course goes beyond traditional vision and language approaches by focusing on the integration of cognition, physical embodiment, and multimodal sensory input to develop AI systems that perceive, understand, and interact with the physical world. Students will examine the theoretical foundations, cutting-edge research, and practical implications of embodied AI across various 
vision-language planning tasks such as Vision-Language Navigation (VLN), Vision-Dialog Navigation (VDN), Embodied Question Answering (EQA), 
Embodied Task Completion, etc. By the end of the course, students will possess the knowledge and skills required to design, implement, 
and advance the next generation of intelligent embodied systems.

## Prerequisites 
Students should have experience with machine learning, data analytics, and deep learning. Strong programming skills in a high-level language such as Python, as well as frameworks for rapid ML prototyping, e.g., PyTorch, Tensorflow, Keras, etc. are essential for implementing and experimenting with the concepts covered in this course. While not mandatory, familiarity with computer vision, natural language processing, and reinforcement learning would be advantageous. Most importantly, students are expected to extract key concepts and ideas from reading ML conference papers. 

## Course Format 
The course is a [role-playing paper reading seminar](https://colinraffel.com/blog/role-playing-seminar.html) that is structured around reading, presenting, and discussing weekly papers. Each class will involve the presentation and discussion of two papers. Each student will have a unique, rotating role per week. This role defines the lens through which each student reads the paper and determines what they prepare for the group in-class discussion. All students, irrespective of their role, are expected to have read the paper readings of each corresponding session before class and come to class ready to discuss. There will be no exams or traditional assignments. Instead, throughout the course, students will engage in practical hands-on projects and discussions to identify and work on open research questions on a variety of topics in embodied AI.  

## Course Topics

Key topics covered in the course include:
- Embodied Perception in Computer Vision: How embodied AI systems leverage visual perception, object recognition, scene understanding, and spatial reasoning.
- Embodied Language Understanding: How embodied AI systems comprehend and generate natural language for effective human-machine communication.
- Sensorimotor Integration: How embodied AI systems use sensory perception and action planning to navigate in a physical environment and complete tasks.
- Learning and Adaptation in Embodied AI: Mechanisms and algorithms for learning and adapting in dynamic physical environments.  
- Applications of Embodied AI: Real-world applications, including embodied visual question answering, interactive virtual agents, embodied conversational agents, etc.

## Presentation Roles
This seminar is organized around the different "roles" students play each week, that define the lens through which students read the paper.
Students will be divided into two groups, one group presenting on Tuesdays and the other on Thursdays. 
In a given class session, students in the presenting groups will each be given a rotating role (described below):
Presenter (two students), Reviewer, Archaeologist, Researcher, Industry Expert, and Blogger OR Hacker (pick one).
Presenting groups should create a formal presentation, i.e., have slides prepared for the group in-class discussion.
For each student in a presenting group, their assigned role determines what they should include in the slides. The Hacker and Blogger roles are the only exceptions to the rule. Hackers should provide a Jupyter Notebook instead of slides and Bloggers go over their written articles. 

> *Depending on changes in course enrollment, the roles might change, for example, remove roles or make roles optional in case enrollment decreases or allow groups of two students for all roles in the event of enrollment increase. Improving based on student feedback, as we go along with the readings, is crucial.*

  - **Presenter:** Create the main presentation, describing the motivation, problem definition, method, and experimental findings of this paper.
  - **Reviewer:** Complete a full---critical but not necessarily negative---review of the paper. 
  Follow the [guidelines for NeurIPS reviewers](https://nips.cc/Conferences/2020/PaperInformation/ReviewerGuidelines) 
  (under "Review Content"). Please answer questions 1-6 under "Review Content", and assign an Overall score (question 9) and a Confidence score (question 10). Skip the rest of the review, including writing a summary. <span style="color:Green"> Note that you can **bypass questions** by filling N/A</span>. For example, you really liked the paper and can't think of any disadvantages. Therefore you can skip the respective question (but use this skip option sparingly). Also, please note that this role does not require going over related work, and is not an exhaustive list of all arguments you can think of. The goal is to enhance your *overall critical thinking*. The instructor reserves the right to contact students who overuse the N/A option.
  - **Archaeologist:** Determine where this paper sits in the context of previous and subsequent work. Find and report on one older paper that has substantially influenced the current paper and one newer paper citing this current paper.
  - **Researcher:** Propose an imaginary follow-up project that has now become possible due to the existence and success of the current paper.
  - **Industry Expert:** Propose a new application or company product for the method in the paper (not already discussed in class), and discuss at least one positive and negative impact of this application. Convince your industry boss that it's worth investing time and money to implement this paper. Your arguments should be particularly applicable to the chosen industry market.
  - **Hacker (optional between two choices):** <span style="color:Green">This role is **optional**, i.e., students can declare if they would like to be a Hacker or a Blogger</span>.  Implement a small part of the paper on a small dataset, a toy problem, or any other simplified version of the paper. Another valid and useful option is to try to reproduce results from the paper, either by downloading and running an existing implementation (with proper credit given to the code sources) or by implementing a core method from the paper. Share a Jupyter Notebook with the code of the algorithm with the class. Your code does not have to be bug-free or run perfectly in all scenarios. Also, you are welcome to use (and give credit to) an existing implementation for "backbone" code (e.g. model building, data loading, training loop, etc.). 
  - **Blogger (optional between two choices):** <span style="color:Green">This role is **optional**, i.e., students can declare if they would like to be a Hacker or a Blogger</span>.  Write a paragraph each about the two papers and an additional paragraph comparing and contrasting them. The summary of each paper should cover the motivation behind the paper, a description of any of the proposed methods, and an overview of the key findings. Include visual aids such as figures, charts, or graphs to illustrate key points. Explain how these papers relate to one another within the broader context of their shared theme. Explore how these papers may complement, challenge, or build upon one another. Provide links or references to additional resources that complement your blog. This could include related research articles, videos, or online discussions. Your insights should reflect critical thinking, encouraging discussion within the class. Think about how your blog can be useful and interesting to an actual online reader. 

**Non-presenter assignment**:
- If you are not in the presenting group during a class session, please submit **the day before class (due 11:59pm EST)** at least one question about either paper - could be something you're confused about or something you'd like to hear discussed more. Questions that open debates and make in-class discussions explore different viewpoints are a plus.  
- After class **and before the end of the day 11:59pm EST**, provide constructive feedback to the presenting group. You may focus on one or more reading roles, or on the presentation holistically. Evaluate the clarity of the presentation, the strength of the arguments, and the quality of visuals, if any. Highlighting strengths and areas for improvement. This feedback will be shared post each presentation.

**Everyone, every week (Optional)**: After each class session, you may post your thoughts on Piazza, for example, which parts did you enjoy reading, what results and insights did you find interesting, a missing result the paper could have included, any useful additional links and resources, etc. Whenever you agree with the comments of a student's post, make sure to endorse their answer. You can also post a reply with your additional thoughts.
 
## Final Project
The main project goal is to engage students in research on Embodied AI.
In particular, students should try to extend papers from topics covered in class 
and present the research outcomes as a research paper, in a standard [conference paper format](https://www.overleaf.com/latex/templates/neurips-2020/mnshsmqkjsqz). Students are encouraged to work in groups of no more than four members, taking into consideration that the work produced should be proportional to the number of members in a team. Groups are required to include a "contributions" section in the final project report, listing each member's contributions in detail. Projects will be hosted on [GitHub](https://github.com/) and should include a written report accompanied by a descriptive Jupyter Notebook, with a format similar to [this notebook](http://nlp.seas.harvard.edu/2018/04/03/attention.html). In addition, groups will present their final projects during the last two class sessions. A PowerPoint or LaTex final presentation is required. 

## Technology
[Piazza](https://piazza.com/vt/fall2023/cs6604) will be used for announcements, general questions, and discussions, etc. 
If you are unable to register to Piazza, please email me. Please familiarize yourself with [GitHub](https://education.github.com/git-cheat-sheet-education.pdf), [Zoom](https://tutorials.tlos.vt.edu/index/zoom.html), [LaTeX](https://www.overleaf.com/learn/latex/Main_Page) 
and [paper writing practices](https://filebox.ece.vt.edu/~jbhuang/slides/Research%20101%20-%20Paper%20Writing%20with%20LaTeX.pdf). To enhance class participation, and unless restricted by low internet bandwidth, please try to keep your video turned on during class. Please keep your audio muted unless you would like to respond to an ongoing discussion or have a question. You can also use the "raise hand" option, type in the chatbox, or use the Zoom reactions for nonverbal feedback. 
Please remember that all in-class discussions should adhere to Virginia Tech's [Principles of Community](https://www.inclusive.vt.edu/Programs/vtpoc0.html). To keep track of student order during office hours, please type your name in the chat as soon as you enter the Zoom room. 
For one-on-one interactions with the instructor, please post a [private note](https://trunkuserguide.screenstepslive.com/s/5891/m/18197/l/195539-how-do-students-ask-a-private-question-to-the-instructor-in-piazza) 
on Piazza or use [Slack](cs-vt.slack.com).


## Schedule
We will update the schedule regularly based on the readings and presentations.
<table style="border: 2px solid black; border-collapse: collapse; width: 100%; max-width: 800px;">
    <thead>
        <tr style="height: 27px;">
            <th style="border: 1px solid gray; height: 27px; width: 10%;">Lecture No.</th>
            <th style="border: 1px solid gray; height: 27px; width: 30%;">Date</th>
            <th style="border: 1px solid gray; height: 27px; width: 60%;">Readings</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>1</td>
            <td>Tuesday, August 22</td>
            <td>Course Introduction</td>
        </tr>
        <tr>
            <td>2</td>
            <td>Thursday, August 24</td>
            <td>Building Blocks in Perception (Instructor)</td>
        </tr>
        <tr>
            <td>3</td>
            <td>Tuesday, August 29</td>
            <td>Building Blocks in Planning (Instructor)</td>
        </tr>
        <tr>
            <td>4</td>
            <td>Thursday, August 31</td>
            <td>Episodic Transformer, Intro to Simulators (Instructor)</td>
        </tr>
        <tr>
            <td>5</td>
            <td>Tuesday, September 5</td>
            <td>Benchmarks: Simulators, Environments, Datasets </br> <b>ProcTHOR: Large-Scale Embodied AI Using Procedural AI Generation</b> <a href="https://arxiv.org/abs/2206.06994">📚</a> <a href="https://procthor.allenai.org/">🌍</a></td>
        </tr>
        <tr>
            <td>6</td>
            <td>Thursday, September 7</td>
            <td>Benchmarks: Simulators, Environments, Datasets</td>
        </tr>
        <tr>
            <td>7</td>
            <td>Tuesday, September 12</td>
            <td>Benchmarks: Simulators, Environments, Datasets</td>
        </tr>
        <tr>
            <td>8</td>
            <td>Thursday, September 14</td>
            <td>Benchmarks: Simulators, Environments, Datasets</td>
        </tr>
        <tr>
            <td>9</td>
            <td>Tuesday, September 19</td>
            <td></td>
        </tr>
        <tr>
            <td>10</td>
            <td>Thursday, September 21</td>
            <td></td>
        </tr>
        <tr>
            <td>11</td>
            <td>Tuesday, September 26</td>
            <td></td>
        </tr>
        <tr>
            <td>12</td>
            <td>Thursday, September 28</td>
            <td></td>
        </tr>
        <tr>
            <td>13</td>
            <td>Tuesday, October 3</td>
            <td><strong><span style="color: #169179;"><span style="color: #b96ad9;">Project Pitch Due</span><br /></span></strong></td>
        </tr>
        <tr>
            <td>14</td>
            <td>Thursday, October 5</td>
            <td></td>
        </tr>
        <tr>
            <td>15</td>
            <td>Tuesday, October 10</td>
            <td><strong><span style="color: #169179;"><span style="color: #b96ad9;">Project Proposal Due</span><br /></span></strong></td>
        </tr>
        <tr>
            <td>16</td>
            <td>Thursday, October 12</td>
            <td></td>
        </tr>
        <tr>
            <td>17</td>
            <td>Tuesday, October 17</td>
            <td></td>
        </tr>
        <tr>
            <td>18</td>
            <td>Thursday, October 19</td>
            <td></td>
        </tr>
        <tr>
            <td>19</td>
            <td>Tuesday, October 24</td>
            <td></td>
        </tr>
        <tr>
            <td>20</td>
            <td>Thursday, October 26</td>
            <td></td>
        </tr>
        <tr>
            <td>21</td>
            <td>Tuesday, October 31</td>
            <td></td>
        </tr>
        <tr>
            <td>22</td>
            <td>Thursday, November 2</td>
            <td><span style="color: #236fa1;"><strong>Project Checkpoint Due</strong></span></td>
        </tr>
        <tr>
            <td>23</td>
            <td>Tuesday, November 7</td>
            <td></td>
        </tr>
        <tr>
            <td>24</td>
            <td>Thursday, November 9</td>
            <td></td>
        </tr>
        <tr>
            <td>25</td>
            <td>Tuesday, November 14</td>
            <td></td>
        </tr>
        <tr>
            <td>26</td>
            <td>Thursday, November 16</td>
            <td></td>
        </tr>
        <tr>
            <td>No class</td>
            <td>Tuesday, November 21</td>
            <td><strong>Thanksgiving Break</strong></td>
        </tr>
        <tr>
            <td>No class</td>
            <td>Thursday, November 23</td>
            <td><strong>Thanksgiving Break</strong></td>
        </tr>
        <tr>
            <td>27</td>
            <td>Tuesday, November 28</td>
            <td></td>
        </tr>
        <tr>
            <td>28</td>
            <td>Thursday, November 30</td>
            <td><strong><span style="color: #e67e23;">Project Presentations</span></strong></td>
        </tr>
        <tr>
            <td>29</td>
            <td>Tuesday, December 5</td>
            <td><strong><span style="color: #e67e23;">Project Presentations</span></strong></td>
        </tr>
    </tbody>
</table>

### Grading

  1. **Readings:** 60 points: Each student will be in the presenting role for 12 sessions and the non-presenting role for the remaining 12. You can earn up to 4 points each time you present (all presenting roles are considered equal). You will receive full credit if you do a thorough job of undertaking your role and present it in a clear and compelling way. When you aren't presenting, you can earn up to 1 point by completing the non-presenting assignment and by participating in the class. At the end of the semester, extra credit of up to 3 points will be assigned to the most well-made presentation, blog, and notebook.
  
  2. **Final Project:** 40 points divided into the following categories:
      - Proposal: 5 points.
      - Clarity: 12 points; your paper should be readable, contain well-defined and clear motivation and contribution statements and appropriately make connections with related work. In general, your project report should follow standard machine learning conference paper formatting and style.
      - Novelty: 3 points; your project should propose something new (a new method, application, or perspective).
      - Code: 5 points; the code accompanying your project should be well-documented and your experimental results should be reproducible. 
      Your repository should include a README file with full instructions on how to run the code.
      Moreover, your code should be easy to run with one simple command; if there are multiple steps involved, please make a bash script. 
      - In-class presentation: 15 points; your final presentation should be clear to the audience and provide a solid review of your work as if you were presenting at a conference. You can find examples in the NeurIPS'20 [schedule](https://nips.cc/virtual/2020/public/cal_main.html) (Oral Spotlight sessions such as [this](https://nips.cc/virtual/2020/public/session_oral_21071.html) one).
           
### Attendance and late work
If you expect to miss a class session in which you are in a "presenting" role, you should still create the presentation 
for your assigned session and find someone else to present for you before the day of the presentation. Missing the class session in which you are supposed to present without arranging the aforementioned accommodations will result in a penalty of 12 points from your total grade, as this disrupts the whole class.
If you miss a non-presenting assignment, you'll get a zero for that session. 
Final project presentations cannot be postponed, as they are scheduled in the course's last few sessions and students need to present at their assigned timeslot. You are welcome to switch your timeslot with another group, but you are responsible for making such arrangements.
Other materials, such as the final project submission and report are negotiable, based on the severity of the request, e.g., medical reasons. 

At any time during the course, if you are facing any difficulties in meeting the course deliverables or would like to discuss any concerns, 
you are welcome to contact me over email, [Slack](cs-vt.slack.com), or Piazza. 
Students can also submit anonymous feedback to this [link](https://tinyurl.com/CS6604EAIFeedback). 
Students seeking special accommodations based on disabilities should contact me and also 
coordinate accessibility arrangements with the [Services for Students with Disabilities office](http://www.ssd.vt.edu).

### Honor Code Statement
All assignments submitted shall be considered “graded work” and all aspects of your coursework are covered by the Honor Code. 
Students enrolled in this course are responsible for abiding by the Honor Code. For additional information about the Honor Code, please visit [https://www.honorsystem.vt.edu/](https://www.honorsystem.vt.edu/). You must attribute appropriate credit to existing ideas, facts, methods, and external sources of code by citing the source. At all times, you should avoid claiming someone else's work as your own. This course will have a **zero-tolerance** philosophy regarding plagiarism or other forms of cheating, and incidents of academic dishonesty
will be [**reported**](https://graduateschool.vt.edu/academics/expectations/graduate-honor-system/how-to-report-violation.html).
A student who has doubts about how the Honor Code applies to this course should obtain specific guidance from the course instructor before submitting the respective assignment.

