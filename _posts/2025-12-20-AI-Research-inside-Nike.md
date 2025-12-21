---
title: "What is it like to do AI research inside Nike?"
date: 2025-12-20
permalink: /posts/2025/12/ai-research-inside-nike/
tags:
  - research
  - ai
  - internship
  - nike
  - mit
---

I'm feeling bittersweet because yesterday, December 19, 2025, was my last day at Nike. My six-month research internship culminated in three presentations across multiple time zones. While the details of the work will eventually show up in my MIT thesis next year, here I reflect on this unique journey of conducting AI research at a world-renowned brand.

![Amazing sunset over Lake Nike](/images/2025-12-20-AI-Research-inside-Nike/Nike-Campus-Last-Day.jpeg)
> On my last day, the rainy Oregon sky cleared up just in time for a stunning sunset over Nike's [Philip H. Knight Campus](https://about.nike.com/en/newsroom/releases/nike-philip-h-knight-campus-announcement)

## The Dual Mandate

**You must think about complicated business needs and state-of-the-art research at the same time.** At a company like Nike, the first priority is being intentional about how the work solves real problems and creates wins. For example, if I get too enamored to a very valid problem in academia but not yet relevant to the business, it might not create immediate value. This is exactly why I'm grateful to bring both my MIT EECS and MBA lenses to the job.

**Networking is a must.** In any huge company, knowledge of a complex business process is naturally distributed. The most effective way (in my experience) to connect the dots is to form collaborative partnerships with teammates who have the subject-matter expertise. Map out everything, put it into one complete document, invite feedback, and iterate.

**Literature review starts on day one.** When your research takes the form of an industry internship, it's easy to lose sight of what's happening in academia, especially in the midst of all the networking above. I'm grateful my thesis advisors constantly reminded me to find the papers that back up what I'm seeing (or claiming). There's no real substitute to shuttling between "professional work" and "research." This context switching happens basically every other day.

## AI at Nike

From the outside, Nike is not likely associated with AI research. However, the company is deeply invested in leveraging AI to enhance customer experiences, optimize supply chains, and innovate product designs. During my internship, I witnessed firsthand how AI is integrated into various facets of Nike's operations. One recent example that the public may be familiar is the [AI search feature on the Nike app](https://www.thestack.technology/nikes-cto-welcomes-nikeai-rollout-are-there-lessons-here-for-developers/), which allows users to find products in natural language.

**My first taste of an enterprise AI platform.** Nike is the very first large enterprise that I have ever worked at (naturally given that my only previous full-time endeavor was at an AI startup), and I truly didn't know much about how data is managed at scale and whether there is an established platform on which AI solutions can be developed.

Through this internship, I got my hands on Databricks for the first time. On the surface, Databricks is a data lakehouse platform that unifies data engineering, data science, and business analytics. But quickly I realized that it is also a powerful AI platform that allows researchers and engineers to build, deploy, and monitor machine learning models at scale. From a simple regression model to access to nearly all major large language models (LLMs) via API, Databricks provides a seamless environment for AI research and development within a large organization like Nike.

Need to embed some text data? Databricks has you covered with various embedding models. Done training your model? You can easily deploy it on Databricks and create an endpoint for real-time predictions. My amazement grew as I saw how Databricks quickly made a new model like GPT-5.2 available as soon as OpenAI released it. And more importantly, all of these models are accessed in a secure and compliant manner, which is crucial for enterprise applications.

When I was just a student/individual builder outside of big companies, it rarely occurred to me how important aspects like internal data governance are; sharing my whole life's troubles with the public instance of ChatGPT.com seems like the way to go. (Well, I shouldn't...)


**I was also blessed with a supportive environment.** From my day-to-day data science teammates to the VP of the customer organization that my research serves, everyone was incredibly supportive and encouraging. They provided me with the resources, mentorship, and feedback needed to thrive in this internship. Over the past six months, I interacted with a far more diverse set of functions than I would have at a purely technical company. In AI, my technical mentors are all hands-on builders who ship models or agentic tools every day, and my business function partners are genuinely excited about applying AI to solve their real problems.

## Cool Company

If you know Nike, you know it's a cool company. The brand is iconic, the culture is vibrant, and the people are passionate about what they do—and about sports. I warmed up with [Eliud Kipchoge before a 5K on campus](https://www.facebook.com/share/v/1H299taBo3/), and I've made sports a daily habit by frequenting three different on-site gyms. Running, cycling, swimming, repeat. I grew up with the Swoosh too, so it's kind of magical to work behind a brand that's instantly recognized around the world. I also joined during an important turning point as the company sharpens its focus on winning again, winning now, so it was valuable to witness a major transition unfold—and to watch how people from senior leadership to every individual contributor react and adapt.

If you ask me what was the coolest experience during my internship, I'd say it was the **Shoe School** where I got to hand make my own shoe from scratch! Sadly it's just one for the left foot because the teaching materials were ordered in batch such that each school cohort gets to make either left or right shoes. Still, it was an unforgettable experience to understand the craftsmanship and technology that goes into making a Nike shoe.

![I made a shoe!](/images/2025-12-20-AI-Research-inside-Nike/Shoe-School.jpeg)

At Nike, there is also a **unique MIT community.**  My research internship at Nike was part of the MIT LGO program, and this [~15-year partnership](https://lgo.mit.edu/partnercompanies/nike-inc/) has created a strong alumni network on campus. I was lucky to have this community's support: both for career development and for fun activities.

And yes, I'll admit it: I've collected a dangerous number of Nike shoes (free or at huge discounts, thanks to the employee perks). But hey, I'm running comfortably in my brand new Vomero Plus, and my knees will be happier.

![My Nike Shoe Boxes](/images/2025-12-20-AI-Research-inside-Nike/Shoe-Boxes.jpeg)

---

Well, finally, a teaser on my research: **a multi-agent buyer–seller negotiation framework under limited information**...

Enough said. [LaTeX time]({% post_url 2025-08-04-Tutorial-MIT-Thesis-LaTeX %})...