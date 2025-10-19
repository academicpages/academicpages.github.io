# My personal website

This repository hosts my personal web page at <https://onnokampman.com> (or as a redirect from <https://onnokampman.github.io>).
It is pretty basic, mostly to serve as a landing page to other websites and to host some essays.

This was forked (then detached) by [Stuart Geiger](https://github.com/staeiou) from the [Minimal Mistakes Jekyll Theme](https://mmistakes.github.io/minimal-mistakes/), which is © 2016 Michael Rose and released under the MIT License.
Big thanks to him and all contributors!
You can fork [his repository](https://github.com/academicpages/academicpages.github.io) yourself if you would like your own personal website.

## To run locally

Follow the below steps if you want to run the website locally.
That is, not through GitHub Pages, but to serve on your own computer.
It is very useful to be able to preview changes locally before pushing them to GitHub.

### Prerequisites

1. On MacOS, make sure HomeBrew is installed.
1. Make sure you have `ruby-dev`, `bundler`, and `nodejs` installed.
    I currently run `ruby v3.4.2`, `node v24.10.0`, and `bundler v2.6.7`.
    On MacOS the commands are:
    ```bash
    brew install ruby
    brew install node
    gem install bundler
    ```
    Or,
    `sudo apt install ruby-dev ruby-bundler nodejs` on Linux.
1. Run `bundle clean` to clean up the directory (no need to run `--force`)
1. Run `bundle install` to install ruby dependencies. If you get errors, delete `Gemfile.lock` and try again.

### Running the website

1. Run `jekyll serve -l -H localhost` to generate the HTML and serve it from `localhost:4000`. The local server will automatically rebuild and refresh the pages on change.
1. (alternatively) Run `bundle exec jekyll liveserve` to generate the HTML and serve it from `localhost:4000`. The local server will automatically rebuild and refresh the pages on change.
1. (alternatively) Run `bundle exec jekyll serve` to generate the HTML and serve it from `localhost:4000`.

<div class="notice--warning" markdown="1">
#### ⚠️ Warning
If you now get a notification about a security vulnerability, delete the Gemfile.lock file.
</div>

## References

1. [academicicons](https://jpswalsh.github.io/academicons/)
1. [Font Awesome](https://fontawesome.com)
