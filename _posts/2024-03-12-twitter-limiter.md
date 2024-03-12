---
title: 'How to limit the number of Twitter posts in your timeline using JavaScript'
date: 2024-03-12
venue-type: blog
permalink: /posts/2024/03/twitter-limiter/
tags:
  - blog-post
  - fun
  - tooling
# image: '/files/unsplash/duy-pham-Cecb0_8Hx-o-unsplash.jpg'
# imagealt: 'people holding shoulders sitting on wall'
# imageoffset: "25%"
# imagecredit_id: '@miinyuii'
# imagecredit_name: 'Duy Pham'
---

I have a bit of a problem scrolling too much of the awesome content on Twitter. There are just too many other people creating cool ideas and software! At first I justified it by the fact that I find academic papers (my feed is curated to mostly academic CS/ML/SE), but now I admit it's too much!
In a bid to waste more time in order to waste less time, I created a [simple script](https://gist.github.com/bstee615/1f4aa8a6d63dc74aff53dac17d287d91) that puts an extra UI onto each post in my Twitter feed:
- For the first five posts, it numbers them to remind me how many I've browsed.
- After that, it blocks them out with a reminder of the limit I set (currently I keep it at five posts).

Here's what the result looks like:
![A screenshot of twitter.com showing the post numbering and limiting features.](/files/twitter_limiter_demo.png)

Here's the link to the script: [JavaScript for Twitter Post Limiter · GitHub](https://gist.github.com/bstee615/1f4aa8a6d63dc74aff53dac17d287d91).
I currently import it automatically with [ViolentMonkey](https://violentmonkey.github.io/).
Plans are to turn it into a FireFox extension (once conference deadline season is over 🙃).
Hope it's useful!