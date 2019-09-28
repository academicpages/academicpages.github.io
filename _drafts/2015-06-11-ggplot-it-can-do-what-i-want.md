---
date: '2015-06-11'
slug: ggplot-it-can-do-what-i-want
title: 'ggplot: it can do what I want!'
---

As a scientist, I often run into this scenario:







  * An experiment has a few treatment groups and a few measurements/replicates per group.


  * I want to show all the data points.





A Cleveland [dot chart](http://www.perceptualedge.com/articles/b-eye/dot_plots.pdf) is a nice way to show data, but if I have multiple replicates then the dots can start to mush on top of each other. R has a command `dotchart` that can do _some_ of what I want: it can take a data frame, recognize that the y-axis has factors, and plot all the points. Unfortunatley, `dotchart` falls short when I want to, say, add some y-jitter so that all the points don't overlap.





ggplot to the rescue! Say you have a dataframe `df` with values in column `value` and the treatment group name in column `variable`. Then you can quickly get an approximation of `dotchart` with `ggplot(dat, aes(x=value, y=variable)) + geom_point()`. Then, to get 10% jitter in the up-down direction, just change `geom_point()` to `geom_point(position=position_jitter(height=0.1))`.





![Horizontal dots with jitter](http://scottolesen.com/img/blog/dot_jitter.png)





If I have more data points, I often want a boxplot. With ggplot, it's a piece of cake to keep the same data but change the plot: just add `+ coord_flip()`. If I were using the `boxplot` command, then adding points is a _big_ pain, and adding jittered points is an even _bigger_ pain, especially if there are many treatments. ggplot makes this easy: the `geom_boxplot` command just takes the `position_jitter` argument as above!





![Boxplot with jitter](http://scottolesen.com/img/blog/boxplot_jitter.png)