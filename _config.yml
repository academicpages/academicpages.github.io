# Site configuration
# 1. Files excluded from Jekyll builds
# 2. Installed Gems
# 3. Gem settings
# 4. Jekyll settings
# 5. Collections
# 6. Jekyll collections settings
# 7. Site settings
# 8. Site favicons & manifest icons
# 9. Site navigation

# 1. Files excluded from Jekyll builds
exclude:
- README.md
- CODE_OF_CONDUCT.md
- CONTRIBUTING.md
- screenshot.png
- LICENSE
- CNAME
- Gemfile
- Gemfile.lock
- alembic-jekyll-theme.gemspec
- .jekyll-cache

# 2. Installed Gems
plugins:
- jekyll-sitemap
- jekyll-mentions
- jekyll-paginate
- jekyll-seo-tag
- jekyll-redirect-from
- jekyll-feed
- jekyll-commonmark
- jekyll-include-cache
- jemoji

# 3. Gem settings
paginate: 2 # jekyll-paginate > items per page
paginate_path: blog/page:num # jekyll-paginate > blog page
jekyll-mentions: https://twitter.com # jekyll-mentions > service used when @replying
twitter:
  username: DavidDarnes # jekyll-seo-tag > Owners twitter username
author: DavidDarnes # jekyll-seo-tag > default author
social: # jekyll-seo-tag > social overrides
  name: David Darnes # jekyll-seo-tag > real name
  links:  # jekyll-seo-tag > social aliases (sameAs)
    - https://twitter.com/DavidDarnes
    - https://www.facebook.com/daviddarnes
    - https://www.linkedin.com/in/daviddarnes
    - https://github.com/daviddarnes
# markdown: CommonMark # Markdown parse settings, CommonMark performs slightly better an others in build time
# commonmark:
  # options: ["SMART", "FOOTNOTES"]
  # extensions: ["strikethrough", "autolink", "table"]

# 4. Jekyll settings
sass:
  style: compressed # Style compression
permalink: pretty  # Permalink style (/YYYY/MM/DD/page-name/)
excerpt_separator: <!-- more --> # Marks end of excerpt in posts
timezone: Europe/London # Timezone for blog posts and alike

# 5. Collections
collections:
  posts:
    title: Posts # Needed for Siteleaf
    output: true
    description: "My thoughts and ideas" # The post list page content
    feature_text: |
      Welcome to the blog
    feature_image: "https://picsum.photos/2560/600?image=866"

# 6. Jekyll collections settings
defaults:
  -
    scope:
      path: ""
    values:
      image: "/assets/default-social-image.png" # Default image for sharing
  -
    scope:
      path: ""
      type: "posts"
    values:
      layout: post # Set the default layout for posts
  -
    scope:
      path: ""
      type: "pages"
    values:
      layout: page # Set the default layout for pages

# 7. Site settings
encoding: utf-8 # Make sure the encoding is right
lang: en-GB # Set the site language
title: "Alembic" # Site name or title, also used in jekyll-seo-tag
logo: "/assets/logos/logo.svg" # Site logo, also used in jekyll-seo-tag
description: "Alembic is a starting point for Jekyll projects. Rather than starting from scratch, this boilerplate is designed to get the ball rolling immediately" # Site description and default description, also used in jekyll-seo-tag
url: "https://alembic.darn.es" # Site url, also used in jekyll-seo-tag
baseurl: ""
repo: "https://github.com/daviddarnes/alembic"
email: "me@daviddarnes.com"
# disqus: "alembic-1" # Blog post comments, uncomment the option and set the site ID from your Disqus account
# date_format: "%-d %B %Y" # Blog post date formatting using placeholder formatting
# google_analytics: ""
# google_analytics_anonymize_ip: ""
# service_worker: false # Will turn off the service worker if set to false
# short_name: "Al" # The web application short name, defaults to the site title
css_inline: true # Will insert all styles into a single <style> block in the <head> element and remove the style <link> reference

# 8. Site favicons & manifest icons
favicons: # Favicons are also used in the manifest file. Syntax is 'size: path'
  16: '/assets/logos/logo@16px.png'
  32: '/assets/logos/logo@32px.png'
  96: '/assets/logos/logo@96px.png'
  120: '/assets/logos/logo@120px.png'
  144: '/assets/logos/logo@144px.png'
  180: '/assets/logos/logo@180px.png'
  512: '/assets/logos/logo@512px.png'
  1024: '/assets/logos/logo@1024px.png'

# 9. Site navigation
navigation_header:
- title: Home
  url: /
- title: Elements
  url: /elements/
- title: Blog
  url: /blog/
- title: Categories
  url: /categories/
- title: Search
  url: /search/
- title: Fork Alembic
  url: https://github.com/daviddarnes/alembic

navigation_footer:
- title: Created by David Darnes
  url: https://darn.es

social_links: # Appears in sidebar. Set the urls then uncomment and comment out as desired
  Twitter: https://twitter.com/DavidDarnes
  LinkedIn: https://www.linkedin.com/in/daviddarnes
  GitHub: https://github.com/daviddarnes
  link: https://darn.es
  RSS: /feed.xml

sharing_links: # Appear at the bottom of single blog posts, add as desired. The value can be 'true' or the desired button colour
  Twitter: "#0d94e7"
  facebook: "#3B5998"
  Email: true

# Load custom fonts from fonts.google.com etc
#
# TIP: Try to keep the number of urls as low to reduce the performance cost
#      If multiple fonts can be requested in a single url opt for this
fonts:
  preconnect_urls:
    - https://fonts.gstatic.com
  font_urls:
    - https://fonts.googleapis.com/css2?family=Merriweather:wght@400;700&display=swap
