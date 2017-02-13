A Github Pages template for academic websites. This was forked (then detached) by [Stuart Geiger](https://github.com/staeiou) from the [Minimal Mistakes Jekyll Theme](https://mmistakes.github.io/minimal-mistakes/), which is © 2016 Michael Rose and released under the MIT License. See LICENSE.md.

I think I've got things running smoothly and fixed some major bugs, but feel free to file issues or make pull requests if you want to improve the generic template / theme.

# Instructions

1. Fork this repository
1. Rename it "yourusername.github.io"
 * Do this in the settings menu (top right, below watch/star/fork buttons)
 * Check it is running in the "Github Pages" section of the settings page.
1. Update variables in _config.yml to match your site
 * url is especially important
1. Update files in _pages directory to set top-level 
1. Update/delete sample files for different kinds of collections 
 * The files for each item are in _talks, _teaching, _publications, _portfolio, and _posts for each item in these collections
 * Delete the sample files (no need to delete the directory) if you do not want a kind of collection in your site
1. Update top menu bar (to add/remove items) by editing _data/navigation.yml
1. Run talkmap.ipynb (must have repository cloned) to generate talkmap
