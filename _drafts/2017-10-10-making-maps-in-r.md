---
title: Making maps in R
author: ''
date: '2017-10-10'
slug: making-maps-in-r
---

I sometimes want to show maps, usually political maps, with some sections highlighted. For example, I recently wanted to show a map of Europe with France and the Netherlands highlighted, and I wanted to crop the map closely.

It turns out that [ggplot](http://ggplot2.tidyverse.org/) has some commands that interact with the [maps](https://cran.r-project.org/web/packages/maps/index.html) package. Start by installing both of those, and we'll load up the world map:

```{r load}
library(dplyr)
library(ggplot2)
library(knitr)

world = map_data('world')
world %>% head(3) %>% kable
```

The subregion is for when a country has multiple, non-contiguous parts. For example, the UK has its England-Scotland-Wales mainland as well as a bunch of islands:

```{r uk-parts}
world %>% filter(region=='UK') %>%
  head(3) %>% kable
```

You can just plot this data straight up with ggplot:

```{r naive-proj-map}
world %>%
  ggplot(aes(x=long, y=lat, group=group)) +
  geom_polygon(fill=NA, color='black')
```

But I only wanted Europe. Filtering out points outside this region leads to bad effects, because it messes up the polygons. Check out what happens to Morocco near Gibraltar:

```{r naive-crop-map}
world %>%
  filter(between(long, -10, 25),
         between(lat, 35, 65)) %>%
  ggplot(aes(x=long, y=lat, group=group)) +
  geom_polygon(fill=NA, color='black')
```

One sensible approach would be to change the axes so that all the points are drawn and we just hide some of them. It turns out that `xlim` and `ylim` (and setting `limits` as an option to `scale_x_continuous`) also do weird cropping. Check out Ireland and Morocco:

```{r lim-crop}
world %>%
  ggplot(aes(x=long, y=lat, group=group)) +
  geom_polygon(fill=NA, color='black') +
  xlim(-10, 25) + ylim(35, 65)
```

To do good cropping, it has to be inside a `coord` function. Incidentally, I'll use this as an opportunity to fix the aspect ratio:

```{r square-crop}
world %>%
  ggplot(aes(x=long, y=lat, group=group)) +
  geom_polygon(fill=NA, color='black') +
  coord_fixed(xlim=c(-10, 25),
              ylim=c(35, 65),
              ratio=1.3)
```

This worked, but it's not a good map projection. It becomes pretty obvious to me when looking at the US, because I'm more used to looking at that map. Things are too square, Texas looks squeezed, Florida is weird, etc.:

```{r usa-square}
state = map_data('state')
state %>%
  ggplot(aes(x=long, y=lat, group=group)) +
  geom_polygon(fill=NA, color='black') +
  coord_fixed(ratio=1.3)
```

Instead, we want to use ggplot's [`coord_map`](http://ggplot2.tidyverse.org/reference/coord_map.html) function, which allows all kinds of cool projections. I'm just going to use the default (Mercator), because it's familiar:

```{r usa-mercator}
state %>%
  ggplot(aes(x=long, y=lat, group=group)) +
  geom_polygon(fill=NA, color='black') +
  coord_map()
```

Aah, now that looks right! But something weird happens when I try to use this back in the Europe map:

```{r europe-mercator-crop}
world %>%
  ggplot(aes(x=long, y=lat, group=group)) +
  geom_polygon(fill=NA, color='black') +
  coord_map(xlim=c(-10, 25),
            ylim=c(35, 65))
```

I think this could be considered a bug in how `coord_map` works. The solution [I found](http://cameron.bracken.bz/finally-an-easy-way-to-fix-the-horizontal-lines-in-ggplot2-maps) is to explicity clip the country shapes to the size of the map, which requires a polygons manipulation package:

```{r europe-smart-clip, message=FALSE}
library(PBSmapping)
world %>%
  # the PBSmapping package expects a data frame with these names
  rename(X=long, Y=lat, PID=group, POS=order) %>%
  clipPolys(xlim=c(-10, 25), ylim=c(35, 65)) %>%
  ggplot(aes(x=X, y=Y, group=PID)) +
  geom_polygon(fill=NA, color='black') +
  coord_map()
```

And so finally I could make the map I really wanted. Note the `keepExtra` option in `clipPolys`, which ensures that the `region` column isn't throw out:

```{r europe-nice}
world %>%
  rename(X=long, Y=lat, PID=group, POS=order) %>%
  clipPolys(xlim=c(-10, 25), ylim=c(35, 65), keepExtra=TRUE) %>%
  mutate(highlight=region %in% c('France', 'Netherlands')) %>%
  ggplot(aes(x=X, y=Y, group=PID, fill=highlight)) +
  geom_polygon(color='black') +
  coord_map() +
  scale_fill_manual(values=c('floralwhite', 'gray')) +
  theme_classic()
```

There's a bunch of stuff you can do with these maps: highlighting, adding points and lines, etc. [This post](http://eriqande.github.io/rep-res-web/lectures/making-maps-with-R.html) has some good examples. Happy mapping!
