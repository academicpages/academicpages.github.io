[![Build Status](https://travis-ci.org/awood/hawkins.png?branch=master)](https://travis-ci.org/awood/hawkins)

# Hawkins
Hawkins is a [Jekyll](http://jekyllrb.com) 3.1+ plugin that incorporates
[LiveReload](http://www.livereload.com) into the Jekyll "serve" process.

## How to Use
Add the following into your `Gemfile`

```
group :jekyll_plugins do
  gem 'hawkins'
end
```

Then run `jekyll liveserve` to serve your files.  The `liveserve` commands takes
all the arguments that `serve` does but with a few extras that allow you to
specify the port that LiveReload runs on or how long LiveReload will wait.  See
the --help for more information.

## How It Works
Hawkins uses a WEBrick servlet that automatically inserts a script tag into a
page's `head` section.  The script tag points to a LiveReload server running on
the same host (by default on port 35729).  That server serves `livereload.js`
over HTTP and also acts as a WebSockets server that speaks the LiveReload
protocol.

If you don't have a browser that implements WebSockets, you can use the
`--swf` option that will have Hawkins load a Flash file that implements
WebSockets.

## Using `--ignore`

LiveReload errs on the side of reloading when it comes to the message it gets.
If, for example, a page is ignored but a CSS file linked in the page isn't, the
page will still be reloaded if the CSS file is contained in the message sent to
LiveReload.  Additionally, the path matching is very loose so that a message to
reload "/" will always lead the page to reload since every page starts with "/".

## A Note on SSL/TLS
If you tell Jekyll to serve your files over SSL/TLS (by specifying the
`--ssl-cert` and `--ssl-key` options), then LiveReload will attempt to use
SSL/TLS as well.  If you are using a certificate that a browser would not
normally accept (e.g.  self-signed or issued by an unknown certificate
authority), you will need to create an exception for the server and port
that Jekyll is serving content over and also for the server and port that
LiveReload is running on.  Generally speaking, these exceptions will be
"127.0.0.1:4000" and "127.0.0.1:35729".

## A Note on Compatibility

Hawkins does not currently work on JRuby.  I'm working on figuring out why, but
be forewarned.

## Thanks
Lots of thanks to [guard-livereload](https://github.com/guard/guard-livereload)
and [rack-livereload](https://github.com/johnbintz/rack-livereload) which
provided a lot of the code and ideas that Hawkins uses.  And of course thanks to
the Jekyll team and LiveReload team for providing outstanding software.

## Copyright
Copyright (c) 2014 Alex Wood. See LICENSE.txt for further details.

