---
layout: gallery
title: A Very Basic Example
no_menu_item: true # required only for this example website because of menu construction
support: [jquery, gallery]
---

At the end of our wonderful three week road trip at the West Coast of the US, we spent about four days in the wonderful city of San Francisco. The city's well known for the Golden Gate Bridge and its fog, but has so much more up its sleeve!

This is an example gallery. All images licensed under [CC-BY-NC-SA license][license]. Check the [Git Repo][repo] for a copy of this license.

{% include gallery-layout.html gallery=site.data.galleries.san-francisco %}

[license]: http://creativecommons.org/licenses/by-nc-sa/4.0/
[repo]: https://github.com/opieters/jekyll-gallery-example
