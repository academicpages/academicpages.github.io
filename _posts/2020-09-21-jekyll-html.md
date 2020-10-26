---
title: Jekyll and HTML Widgets
output:
  md_document:
    variant: gfm
    preserve_yaml: TRUE
knit: (function(inputFile, encoding) {
  rmarkdown::render(inputFile, encoding = encoding, output_dir = "../_posts") })
date: 2020-09-19
permalink: /posts/2020/09/jekyll-html
excerpt_separator: <!--more-->
toc: true
image: /images/posts/jekyll-html/map.png
tags:
  - jekyll
  - rmarkdown
  - data
  - visualization
---



I’m currently compiling a list of university-affiliated programs
designed to help prepare students for graduate study in political
science and assist them in the process of applying to graduate school (a
labyrinthine and opaque process in many regards). Since travel costs can
be a deciding factor for some students when deciding whether to apply to
these programs, I thought it would be nice to also put them on a map.

<!--more-->

While just plotting them on a map is easy, since it will be on a web
page, I figured why not also embed links to each program in the map as
well. In theory this is easy thanks to R packages like
[leaflet](https://rstudio.github.io/leaflet/), which leverages the
(unsurprisingly named) [leaflet](https://leafletjs.com/) JavaScript
library for interactive webmaps. However, because I use
[Jekyll](https://jekyllrb.com/) instead of [Hugo](https://gohugo.io/)
for my site, I can’t just use the
[blogdown](https://bookdown.org/yihui/blogdown/) R package and have
everything magically work.

Steven Miller’s tutorial on [integrating R Markdown and
Jekyll](http://svmiller.com/blog/2019/08/two-helpful-rmarkdown-jekyll-tips/)
is the starting point my own use of R Markdown and Jekyll, so check that
out first for a quick primer on how to use R Markdown to render `.Rmd`
files into the `.md` files that Jekyll uses to render your website. This
approach works fantastically well for static images, and requires just a
little tweaking to make interactive widgets like leaflet maps work.

# Leaflet

We’ll use three packages to create our map. The tidyverse is pretty
well-documented at this point, but I use it to write efficient and
readable code. `tidygeocoder` is a geocoder that can use a variety of
geocoding services and works well with data frames and tibbles. Finally,
`leaflet` is what we’ll use to create our actual map widget.

``` r
library(tidyverse)
library(tidygeocoder)
library(leaflet)
```

First, we need to load our data. This is a CSV file of program
information that I’ve compiled myself.

``` r
## read in data
predoc <- read_csv('predoc.csv')

## inspect the data
predoc
```

    ## # A tibble: 9 x 4
    ##   Institution          Name                     Location      URL                                   
    ##   <chr>                <chr>                    <chr>         <chr>                                 
    ## 1 University of South… POIR Predoctoral Summer… Los Angeles,… https://dornsife.usc.edu/poir/predoct…
    ## 2 Duke University      Ralph Bunche Summer Ins… Durham, NC, … https://www.apsanet.org/rbsi          
    ## 3 UC San Diego         START                    La Jolla, CA… https://grad.ucsd.edu/diversity/progr…
    ## 4 MIT                  MSRP                     Cambridge, M… https://oge.mit.edu/graddiversity/msr…
    ## 5 UC Irvine            SURF                     Irvine, CA, … https://grad.uci.edu/about-us/diversi…
    ## 6 University of Washi… NSF REU: Spatial Models… Tacoma, WA, … https://www.tacoma.uw.edu/smed/nsf-re…
    ## 7 University of North… NSF REU: Civil Conflict… Denton, TX, … https://untconflictmgmtreu.wordpress.…
    ## 8 Princeton University Emerging Scholars in Po… Princeton, N… https://politics.princeton.edu/gradua…
    ## 9 Harvard University   PS-Prep                  Cambridge, M… https://projects.iq.harvard.edu/ps-pr…

First, we need to get latitude and longitude coordinates from our place
names to plot them on a map. We’ll use the `geocode()` function, where
the first argument is a data frame containing a column with the location
information we want to use. The second argument is `address`, which
tells the geocoder to use the information stored in the Address column
of our data frame, and then `method = 'osm'` dispatches it to the Open
Street Map geocoder,
[Nominatim](https://wiki.openstreetmap.org/wiki/Nominatim).

Next, we’ll use `mutate()` to create a new variable to hold the popup
text a user will see when they click on a point. I want to provide the
university name, the program’s name, and then a link to the program’s
information page. I use the `str_c()` function to combine the
Institution and Name columns, and then I use *another* call to `str_c()`
to format the URL. This second call looks like `str_c('<a href="', URL,
'" target="_PARENT">Program Info</a>')`, where URL is the name of the
URL field. It combines the standard start of an HTML anchor tag (`<a
href="`) with the URL itself, adds the link text of “Program Info”, and
then closes the tag. The one unusual element is `target="_PARENT"` in
the anchor tag. This is necessary to make any links a user clicks open
normally, instead of within the frame used to embed it into the page
(more on that [later](#frame-it)).

Once we’ve prepped our popup text, we just pass the data frame to
`leaflet()`, add a background map (I’ve used a styled map, but you can
also get the default map with `addTiles()`), and then the markers
themselves. The one tricky part of `addMarkers()` is that it expects its
arguments as one-sided formulas, not just variable names like tidyverse
functions. `geocode()` has created lat and long columns, so pass those
through as well as our label column, and we’re good to go.

## Map it

Putting all the above code together in a pipeline looks like this:

``` r
## prep and plot
predoc %>% 
  geocode(address = Location, method = 'osm') %>% ## gecode locations
  mutate(lab = str_c(Institution, Name,
                     str_c('<a href="', URL, '" target="_PARENT">Program Info</a>'),
                     sep = '<br>')) %>% # paste fields into popup text
  leaflet() %>% # create leaflet map widget
  addProviderTiles(providers$CartoDB.Positron) %>% # add muted palette basemap
  addMarkers(lng = ~ long, lat = ~ lat, popup = ~ lab) # add markers with popup text
```

Unfortunately this code produces an error that stops R Markdown dead in
its tracks; like, the-`error = T`-knitr-chunk-option-won’t-even-save-you
dead in its tracks. What gives? R Markdown is supposed to be able to
render interactive widgets no problem. The issue is that R Markdown can
render those widgets for HTML output, but since we’re creating a [GitHub
Flavored Markdown](https://github.github.com/gfm/) document that Jekyll
then turns into HTML, R Markdown chokes. It can’t embed an HTML widget
into a plain text markdown document. Luckily there is a way around this,
but it involves an extra step and dealing with some file paths.

# R Markdown, HTML widgets, and Jekyll

To make things work, we have to manually save the HTML from our widget,
and then embed it into our resulting markdown document. Then, when
Jekyll renders the markdown to HTML, it will be visible in the final
HTML files that comprise your website. This involves telling R where to
save the HTML, then referencing it using raw HTML code in our markdown
document. We’re going to do this with the
[htmlwidgets](https://github.com/ramnathv/htmlwidgets) R package.

``` r
## load htmlwidgets to save map widget
library(htmlwidgets)

## prep and plot
predoc %>% 
  geocode(address = Location, method = 'osm') %>% ## gecode locations
  mutate(lab = str_c(Institution, Name,
                     str_c('<a href="', URL, '" target="_PARENT">Program Info</a>'),
                     sep = '<br>')) %>% # paste fields into popup text
  leaflet() %>% # create leaflet map widget
  addProviderTiles(providers$CartoDB.Positron) %>% # add muted palette basemap
  addMarkers(lng = ~ long, lat = ~ lat, popup = ~ lab) %>% # add markers with popup text
  saveWidget(here::here('/files/html/posts', 'predoc_map.html')) # save map widget
```

The code is identical to that above, with the addition of the file line
that saves the map widget as an HTML file called `predoc_map.html` in
`/files/html/posts` using the `saveWidget()` function. You’ll notice I
use the `here()` function from the
[here](https://github.com/jennybc/here_here) R package to supply the
`file` argument to `saveWidget()`. `here` is great because it very
intelligently finds the top level of whatever project you’re working on
and then constructs file paths from there. It has a number of ways to
determine where a project ‘starts’, but for us it works because our
website is a git repo and contains a `.git` directory.

## Frame it

All that’s left to do is embed the map widget in the page using an
[iframe](https://www.w3schools.com/tags/tag_iframe.asp). iframes allow
you to embed an HTML page inside of another HTML page. Since
`saveWidget()` saved our map widget as an HTML file that’s nothing but
our map, we can then embed it into our page using an iframe. Jekyll
allows raw HTML in markdown files which it ignores and passes through
untouched into the final HTML files it produces. Here’s the code I used
for the map in this post.

``` html
<iframe src="/files/html/posts/predoc_map.html" height="600px" width="100%" style="border:none;"></iframe>
```

The main argument is `src="..."`, which tells the iframe what content it
will contain. Notice that this is the same file path I just specified
above in `saveWidget()`. As long as that directory exists in your
website repo, everything will work smoothly. There are three important
arguments in addition to the content of the iframe itself:

  - `height` is how tall you want the iframe to be; here I’ve specified
    it in pixels, but you can also use inches, centimeters, or
    percentages as you’ll see below
  - `width` is how wide you want the iframe to be; I’ve used a
    percentage here because the
    [AcademicPages](https://academicpages.github.io/) template is
    responsive and will resize itself on smaller screens
  - `style` is where I tell the iframe not to include a border so it
    blends seamlessly with the rest of the page

# The finished product

Here’s what the final map looks like. If you didn’t know the extra
effort it took, it would blend seamlessly into the page. Theoretically
this *should* work for any HTML widget, like those produced by the
`plotly` R package. If you haven’t checked `plotly` out, you really
should. It can turn `ggplot2` plots into interactive widgets with a
single line of code\!

<iframe src="/files/html/posts/predoc_map.html" height="600px" width="100%" style="border:none;">

</iframe>
