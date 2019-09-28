---
date: '2016-05-22'
slug: does-more-people-mean-more-culture
title: Does more people mean more culture?
---

I was wondering, if you have more people, does that mean you produce more "culture"? This question arose during a discussion I was having with two friends. I had proposed that it wasn't surprising that you can more easily find [Russian music](http://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Dpopular&field-keywords=russian+music&rh=n%3A5174%2Ck%3Arussian+music) (21,000 hits on Amazon) than [Greek music](http://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Dpopular&field-keywords=greek+music&rh=n%3A5174%2Ck%3Agreek+music) (6,000 hits) not necessarily because the Russians are more "musical" than the Greeks but simply because there are many more Russians (Russian has 147 million people) than Greeks (Greece has 11 million).

This is a complicated idea. The number of albums on Amazon measures the popularity of that type of music in the US rather than the total amount (or "quality") of music produced by an entire country. That popularity could be the result of purchases made by people living in the US who have a background in that country (viz., how big are the Russian and Greek diasporas?), or it could be the result of the appeal that style of music has for those living in the US who do _not_ have a background in that music (e.g., Irish music may have a disproportionate number of albums because many of those albums are in a language many Americans understand).

I tried the simple thing: just ignore all these complications and see what comes out. I used wikipedia's [list of populations](https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population) and [list of adjectival forms](https://en.wikipedia.org/wiki/List_of_adjectival_and_demonymic_forms_for_countries_and_nations) for countries and scraped Amazon's CDs & Vinyl category. (I wasn't very careful when curating these lists: I just used the adjectival form even when it was probably unfamiliar to Americans, e.g., Malagasy for "from Madagascar".)

The results on a normal scale look crazy because there are three huge outliers: Japan has a large population (127 million) but a _huge_ number of albums (almost a million), while China and Indian have huge populations (1.4 and 1.3 billion) but modest numbers of albums (6,000 and 14,000). The remaining countries in a blob that one might go so far as to call "line-like" on log-log axes:

[![Rplot](http://scottolesen.com/wp-content/uploads/2016/05/Rplot-300x285.png)](http://scottolesen.com/wp-content/uploads/2016/05/Rplot.png)

(I'm not surprised the US is "below the line": searching for "American music" on Amazon doesn't give many "world music" hits.)

Conclusion: Inconclusive. I would imagine that adding GDP and/or immigration history (i.e., size of diaspora in US) might produce a better model.

