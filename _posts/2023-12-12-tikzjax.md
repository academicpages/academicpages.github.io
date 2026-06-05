---
layout: post
title: a post with TikZJax
date: 2023-12-12 22:25:00
description: this is what included TikZ code could look like
tags: formatting diagrams
categories: sample-posts
tikzjax: true
---

This is an example post with TikZ code. TikZJax converts script tags (containing TikZ code) into SVGs.

<script type="text/tikz">
\begin{tikzpicture}
    \draw[red,fill=black!60!red] (0,0) circle [radius=1.5];
    \draw[green,fill=black!60!green] (0,0) circle [x radius=1.5cm, y radius=10mm];
    \draw[blue,fill=black!60!blue] (0,0) circle [x radius=1cm, y radius=5mm, rotate=30];
\end{tikzpicture}
</script>
