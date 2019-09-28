---
date: '2015-12-21'
slug: ggplot-gotcha-beware-jittering-your-data
title: 'ggplot gotcha: beware jittering your data'
---

I like to overlay boxplots with a scatter plot so that you get the comfort of seeing the real data with the easiness of seeing the mean and IQR. Here's an example with some fake data in a data frame that I'll call `dat`:
`
group val
A 0.6
B 1.6
A 0.7
B 1.7
A 0.8
...
`

It looks like:

`ggplot(dat, aes(x=group, y=val)) + geom_boxplot() + geom_point()`
[![p1](http://scottolesen.com/wp-content/uploads/2015/12/p1-300x300.png)](http://scottolesen.com/wp-content/uploads/2015/12/p1.png)

Often there's a lot of data, so I want to jitter the points left and right to prevent them overlapping. I've found that `width=0.1` is good enough to get that kind of separation:

`ggplot(dat, aes(x=group, y=val)) + geom_boxplot() + geom_point(position=position_jitter(w=0.1))`
[![p2](http://scottolesen.com/wp-content/uploads/2015/12/p2-300x300.png)](http://scottolesen.com/wp-content/uploads/2015/12/p2.png)

Unfortunately, this seemingly reasonable command did something very insidious: it _also_ jittered in the _y_-axis direction! To see that, I'll draw horizontal lines where the original data were:

`ggplot(dat, aes(x=group, y=val)) + geom_boxplot() + geom_point(position=position_jitter(w=0.1)) + geom_hline(aes(yintercept=val))`
[![p25](http://scottolesen.com/wp-content/uploads/2015/12/p25-300x300.png)](http://scottolesen.com/wp-content/uploads/2015/12/p25.png)

To get this right, you need to actually add `h=0`:

`ggplot(dat, aes(x=group, y=val)) + geom_boxplot() + geom_point(position=position_jitter(h=0, w=0.1))`
[![p3](http://scottolesen.com/wp-content/uploads/2015/12/p3-300x300.png)](http://scottolesen.com/wp-content/uploads/2015/12/p3.png)

To show that it's right:
`ggplot(dat, aes(x=group, y=val)) + geom_boxplot() + geom_point(position=position_jitter(h=0, w=0.1)) + geom_hline(aes(yintercept=val))`
[![p35](http://scottolesen.com/wp-content/uploads/2015/12/p35-300x300.png)](http://scottolesen.com/wp-content/uploads/2015/12/p35.png)