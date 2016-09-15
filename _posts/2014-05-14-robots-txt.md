---
id: 653
title: 'A dynamically-generated robots.txt: will search engine bots recognize themselves?'
date: 2014-05-14T01:37:02+00:00
author: stuart
guid: http://stuartgeiger.com/wordpress/?p=653
permalink: /posts/2014/05/robots-txt/
redirect_from:
  - /wordpress/2014/05/robots-txt/
  - /wordpress/?p=65
categories:
  - Blog Posts
tags:
  - algorithms
  - bots
  - communication
  - discourse
  - infrastructure
  - internet
  - philosophy
  - technology
---

In short, I built a script that dynamically generates a robots.txt file for search engine bots, who download the file when they seek direction on what parts of a website they are allowed to index. By default, it directs all bots to stay away from the entire site, but then presents an exception: only the bot that requests the robots.txt file is allowed full reign over the site. If Google&#8217;s bot downloads the robots.txt file, it will see that only Google&#8217;s bot gets to index the entire site. If Yahoo&#8217;s bot downloads the robots.txt file, it will see that only Yahoo&#8217;s bot gets to index the entire site. Of course, this is assuming that bots identify themselves to my server in a way that they recognize when it is reflected back to them.

<!--more-->

<span style="color: #292f33;">What is a robots.txt file? Most websites have one of these very simple file called &#8220;robots.txt&#8221; on the main directory of their server. The robots.txt file has been around for almost two decades, and it is now a standardized way of communicating what pages search engine bots (or crawlers) should and should not visit. Crawlers are supposed to request and download a robots.txt file from any website they visit, and then obey the directives mentioned in such a file. Of course, there is nothing which prevents a crawler from still crawling pages which are forbidden in a robots.txt file, but most major search engine bots behave themselves. </span>

<span style="color: #292f33;">In many ways, robots.txt files stand out as a legacy from a much earlier time. When was the last time you wrote something for public distribution in a .txt file, anyway? In an age of server-side scripting and content management systems, robots.txt is also one the few public-facing files a systems administrator will actually edit and maintain by hand, manually adding and removing entries in a text editor. A robots.txt file has no changelog in it, but its revision history would be a partial chronicle of a systems administrator&#8217;s interactions with how their website is represented by various search engines.</span><span style="color: #292f33;">You can specify different directives for different bots by specifying a user agent, and well-behaved bots are supposed to look for their own user agents in a robots.txt file and follow the instructions left for them. </span>As for my own, I&#8217;m sad to report that I simply let all bots through wherever they roam, as I use a sitemap.tar.gz file which a WordPress plugin generates for me on a regular basis and submits to the major search engines. So my robots.txt file just looks like this:

<pre><span style="color: #000000;">User-agent: *
</span>Allow: /</pre>

<span style="color: #292f33;">An interesting thing about contemporary web servers is that file formats no longer really matter as much as they used to. In fact, files don&#8217;t even have to exist as we they are typically represented in URLs. When your browser requests the page http://stuartgeiger.com/wordpress/2014/05/robots-txt, there is a directory called &#8220;wordpress&#8221; on my server, but everything after that is a fiction. There is no directory called 2014, no a subdirectory called 05, and no file called robots-txt that existed on the server before or after you downloaded it. Rather, when WordPress receives a request to download this non-existent file, it intercepts it and interprets it as a request to dynamically generate a new HTML page on the fly. WordPress queries a database for the content of the post, inserts that into a theme, and then has the server send you that HTML page &#8212; with linked images, stylesheets, and Javascript files, which often do actually exist as files on a server. The server probably stores the dynamically-generated HTML page in its memory, and sometimes there is caching to pre-generate these pages to make things faster, but other than that, the only time an HTML file of this page ever exists in any persistent form is if you save it to your hard drive. </span>

<span style="color: #292f33;">Yet robots.txt lives on, doing its job well. It doesn&#8217;t need any fancy server-side scripting; it does just fine on its own. Still, I kept thinking about what it would be like to have a script dynamically generate a robots.txt file on the fly whenever it is requested. Given that the only time a robots.txt file is usually downloaded is when an automated software agent requests it, there is something strangely poetic about an algorithmically-generated robots.txt file. It is something that would, for the most part, only ever really exist in the fleeting interaction between two automated routines. So of course I had to build one.</span>

The code required to implement this is trivial. First, I needed to modify how my web server interprets requests, so that whenever a request was made to robots.txt, the server would execute a script called robots.php and send the client the output as robots.txt. Modify the .htaccess file to add:

<pre><span style="color: #000000;">RewriteEngine On
RewriteBase /
RewriteRule ^robots.txt$ /robots.php</span></pre>

Next, the PHP script itself:

<pre>&lt;?php
header('Content-Type:text/plain');
echo "User-agent: *" . "\r\n";
echo "Allow: /" . "\r\n";
?&gt;
</pre>

Then I realized that this was all a little impersonal, and I could do better since I&#8217;m scripting. With PHP, I can easily query the user-agent of the client which is requesting the file, the identifier it sends to the web server. Normally, user agents define the browser that is requesting the page, but bots are supposed to have an identifiable user-agent like &#8220;Googlebot&#8221; or &#8220;Twitterbot&#8221; so that you can know them when they come to visit. Instead of granting access to every user agent with the asterisk, I made it so that the user agent of the requesting client is the only one that is directed to have full access.

<pre>&lt;?php
header('Content-Type:text/plain');
echo "User-agent:" . $_SERVER['HTTP_USER_AGENT'] . "\r\n";
echo "Allow: /" . "\r\n";
?&gt;</pre>

After making sure this worked, I realized that I needed to go out there a little more. If the bots didn&#8217;t recognize themselves, then by default, they would still be allowed to crawl the site anyway. robots.txt works on a principle of allow by default. So I needed to add a few more lines which made it so that the robots.txt file the bot downloaded would direct all **other** bots to **not** crawl the site, but give full reign to bots with the user agent it sent the server.

<pre>&lt;?php
 header('Content-Type:text/plain');
 echo "User-agent: *" . "\r\n";
 echo "Disallow: /" . "\r\n";
 echo "User-agent:" . $_SERVER['HTTP_USER_AGENT'] . "\r\n";
 echo "Allow: /" . "\r\n";
 ?&gt;</pre>

This is what you get if you download it in Chrome:

<pre>User-agent: *
Disallow: /
User-agent: Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36 
Allow: /</pre>

The restrictive version is now live, up at <http://www.stuartgeiger.com/robots.txt>. I&#8217;ve also put it up [on github](https://github.com/staeiou/robots.txt.php), because apparently that&#8217;s what cool kids do. I&#8217;m looking forward to seeing what will happen. Google&#8217;s webmaster tools will notify me if its crawlers can&#8217;t index my site, for whatever reason, and I&#8217;m curious if Google&#8217;s bots will identify themselves to my servers in a way that they will recognize.
