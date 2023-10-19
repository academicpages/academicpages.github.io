---
permalink: /codingadvice
title: "Coding Advice"
author_profile: true
redirect_from: 
  - /codingadvice/
---

### Switch from Stata to R and Python
   1. Make sure you know all of them
   2. If you cannot learn all of them, make sure you are expert in one first
      - Predoc employers often emphasize this, and that they believe an expert in one language can quickly pick up other languages on the job
   3. Once you do 1 and 2, prioritize R and Python
      - Why? Aside from all their common advantages, LLMs are much better in R an Python due to the large amount of tidy code online in Python and R vs Stata. If LLMs like ChatGPT and Github copilot 

### Write functions
   - whenever a chunk of code is used twice or more
   - LLMs can easily re-write your code into functions 

### For complex tasks
- conceptualize the structure of your ideal dataset, on which you can run analyses, then work toward that structure
- write a roadmap with a numbered sequence of steps, then code with each numbered section step by step

### Describe data by row, colum, and unique level
- Each row identifies a...
- Key columns include ...
- Data is unique at ... level

### Keep a coding notebook
  - Benefit: can easily copy & paste with minor changes
  - Reflect: if you have to copy & paste a large chunk of code multiple times from your notebook, then maybe there're packages online that address your needs

### Use `renv` for long-term projects in R
