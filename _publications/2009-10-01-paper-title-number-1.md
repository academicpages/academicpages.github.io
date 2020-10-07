---
title: "SCC++: Predicting the programming language of questions and snippets of Stack Overflow"
collection: publications
permalink: /publication/2009-10-01-paper-title-number-1
excerpt: 'This paper based on my master's thesis.'
date: 2020-01-01
venue: 'Journal of Systems and Software'
paperurl: 'http://kamel773.github.io/files/paper1.pdf'
citation: ''
---
[Download paper here](http://kamel773.github.io/files/paper1.pdf)

Abstruct: Stack Overflow is the most popular Q&A website among software developers. As a platform for knowledge sharing and acquisition, the questions posted on Stack Overflow usually contain a code snippet.
Determining the programming language of a source code file has been considered in the research community; it has been shown that Machine Learning (ML) and Natural Language Processing (NLP) algorithms
can be effective in identifying the programming language of source code files. However, determining the
programming language of a code snippet or a few lines of source code is still a challenging task. Online
forums such as Stack Overflow and code repositories such as GitHub contain a large number of code
snippets. In this paper, we design and evaluate Source Code Classification (SCC++), a classifier that can
identify the programming language of a question posted on Stack Overflow. The classifier achieves an
accuracy of 88.9% in classifying programming languages by combining features from the title, body and
the code snippets of the question. We also propose a classifier that only uses the title and body of the
question and has an accuracy of 78.9%. Finally, we propose a classifier of code snippets only that achieves
an accuracy of 78.1%. These results show that deploying Machine Learning techniques on the combination of text and code snippets of a question provides the best performance. In addition, the classifier can
distinguish between code snippets from a family of programming languages such as C, C++ and C#, and
can also identify the programming language version such as C# 3.0, C# 4.0 and C# 5.0.