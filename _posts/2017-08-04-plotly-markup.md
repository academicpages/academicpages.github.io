---
title: "Embedding Python plotly figures in markup"
date: 2017-08-04
permalink: /posts/2017/08/plotly-markup/
tags:
  - Python
  - plotly
  - Markdown
  - Sphinx
---

A **lightweight markup language** is a simple, human-readable language for formatting text.
It's easy to read and compatible with most text editors.
Documents written in lightweight markup are usually then converted to things that are harder for people, but easier for computers, to read, like HTML.
The most common ones that I've heard of people using are Markdown, R Markdown, and reStructured Text.
I imagine that most people who do data analysis/exploratory visualization/data science use a markup language more often than they write in raw HTML.

I made a figure using [plotly for Python](https:plot.ly/python) today and wanted to include it in the documentation for a package I'm working on.
The plotly guide has instructions for embedding figures in HTML, but I write my docs in reStructured Text and compile it using Sphinx.
It took me a while to figure out how to do this intermediate step, getting the plot embedded in the reStructured Text so it would render in HTML properly, so I'm writing it up here.

[Here's](https://plot.ly/python/pie-charts/) an easy example plot for us to make.

```python
import plotly
labels = ['Oxygen', 'Hydrogen', 'Carbon_Dioxide', 'Nitrogen']
values = [4500, 2500, 1053, 500]

trace = plotly.graph_objs.Pie(labels=labels, values=values)
plotly.offline.plot([trace], filename='basic-pie-chart')
```

## Step 1: Embed HTML in the markup language

We want to hack the markup language and tell it to stop parsing what we write, and instead just let us enter raw HTML.

In Markdown, there's no need to do so: it just recognizes HTML and treats it as such.

In reStructured Text, we'd use the `raw` directive and start a chunk with `.. raw:: html`.

## Step 2: Generate HTML to make the plot

If you're making a plotly figure offline, you'd typically just run `plotly.offline.plot(fig, filename)`.
This will open up the figure in a browser and save it in your working directory.

We want to get the raw HTML which makes the figure.
Luckily the function can give us that, too.
Instead, we would enter

```python
plotly.offline.plot([trace], include_plotlyjs=False, output_type='div')
```

Python spits out the raw HTML!

## Putting them together

We have the code we need to make the plot.
We need to add one more thing, a `<script>` tag that tells the site where to look in order to render the Javascript behind the plot.
In reStructured Text, it looks like this:

```rst
.. raw:: html
	
    <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
    <div id="cd52e831-399a-403d-9bb2-0c56214b1d38" style="height: 100%; width: 100%;" class="plotly-graph-div"></div>
	<script type="text/javascript">window.PLOTLYENV=window.PLOTLYENV || {};window.PLOTLYENV.BASE_URL="https://plot.ly";Plotly.newPlot("cd52e831-399a-403d-9bb2-0c56214b1d38", [{"type": "pie", "values": [4500, 2500, 1053, 500], "labels": ["Oxygen", "Hydrogen", "Carbon_Dioxide", "Nitrogen"]}], {}, {"linkText": "Export to plot.ly", "showLink": true})</script>
```

And in Markdown, we do the same but leave out the raw tag.
It looks like this.

<script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
<div id="cd52e831-399a-403d-9bb2-0c56214b1d38" style="height: 100%; width: 100%;" class="plotly-graph-div"></div>
<script type="text/javascript">window.PLOTLYENV=window.PLOTLYENV || {};window.PLOTLYENV.BASE_URL="https://plot.ly";Plotly.newPlot("cd52e831-399a-403d-9bb2-0c56214b1d38", [{"type": "pie", "values": [4500, 2500, 1053, 500], "labels": ["Oxygen", "Hydrogen", "Carbon_Dioxide", "Nitrogen"]}], {}, {"linkText": "Export to plot.ly", "showLink": true})</script>