---
layout: post
title: Where are the Drains?
mathjax: true
---

A few months ago, I submitted a paper on the long-term changes in size distributions of prairie wetlands to Nature Geoscience. In short, I had claimed that there appeared to be a dramatic shift in size distributions that could not be accounted for via natural mechanisms and attributed this alteration to human modification of the landscape for agriculture. These can take many forms and may involve either the addition or removal of water to a given position in the landscape. I specifically mentioned that drainage channels  dug by farmers--think of dragging a plow or powered shovel through a field several times--are ubiquitous across the Dakotas and, if placed at the right time, could potentially explain our observational results. 

I received a rejection and though the comments were both well researched and actionable, there was one point which made me realize that there is a big blind spot in the regional literature on the interplay between agriculture and hydrology.

A [recent article by Owen McKenna](https://link-springer-com.proxy.lib.duke.edu/article/10.1007/s10584-017-2097-7) and other researchers at [Northern Prairie Wildlife Research Center](https://www.npwrc.usgs.gov/) was cited in the reviewer's comments because it noted that subsurface agricultural drainage permit data is [available](http://www.swc.nd.gov/info_edu/map_data_resources/drains/) for the state of North Dakota from the State Water Commission and the timing of these permits (after 2003, largely) directly contradicts the date at which I claimed the most substantial effect on the environment was observed (circa 2000). However, there was a very subtle point that was easily lost in this review which is that I was considering *all* types of agricultural drainage—not just subsurface drainage. I suspect that surface drainage channels are not captured at all since most drains are smaller than the size threshold required for permitting. I know this is the case because I have personally seen many farm drains with watersheds greater than 20 acres which have no record in the state database. Consequently, I am a bit skeptical of research or reviews that suppose that the state drainage data provides the whole story.

As far as I know, there are no good, publicly available datasets tabulating the location and extent of surface drains in the United States. This is unfortunate because they could potentially have an enormous impact on flatland hydrology.

This is both obstacle and opportunity - how can we identify tiny depressions in the landscape with remote sensing? 

## Finding Ditches

I have read a fair amount of literature on detecting linear drainage features in the landscape with elevation data; these often look at various gradient-derived metrics of landscape curvature. You can find a great example of this by Paola Passalacqua et al. at [this link](https://digitalcommons.usu.edu/cgi/viewcontent.cgi?article=1553&context=wats_facpub). For many situations, this approach will suffice. One caveat is that you need high-quality elevation data which may be from LiDAR. This is not always available (especially across the entire Prairie Pothole Region) and consequently we need to find other methods.

Last week, I was browsing through some sample imagery from [Planet Labs](https://www.planet.com/gallery/) and found something really interesting. I found a 1-month composite / average of some farmland in North Dakota that I am familiar with and saw that the drainage channels stuck out as clear as day due to snow accumulations:

{: style="text-align:center"}
![png](/images/snow_drains.png){:height="50%" width="50%"}

*The white lines extending across this field correspond exactly to the location of known drainage channels.*

If the drainage pattern was this obvious from a single image, then it's possible that we could algorithmically find it with lots of data. This could be a really promising way to get reliable data on surface drainage using nothing more than 3-5 m. satellite imagery. 