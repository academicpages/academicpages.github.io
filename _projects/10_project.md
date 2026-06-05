---
layout: page
title: project 10
description: A project with an introduction section
img: assets/img/5.jpg
importance: 5
category: work
project_intro: true
icons:
  - file: javascript/javascript-original.svg
    site: devicons
  - file: processing
    site: skillicons
  - file: https://www.espressif.com/sites/all/themes/espressif/images/logo-guidelines/primary-vertical-logo.png
repository:
  - alshedivat/al-folio
---

# Project Intros

A simple way to efficiently display your github project, or any other project as well!

To add a project intro just set `project_intro` to `true` in the front matter. Also add icons to display the tech-stacks used in the project. Finally add relevant repositories to be displayed right below the intro.

```yml
---
project_intro: true
icons:
  - file: javascript/javascript-original.svg
    site: devicons
  - file: processing
    site: skillicons
  - file: https://www.espressif.com/sites/all/themes/espressif/images/logo-guidelines/primary-vertical-logo.png
  repository:
    - alshedivat/al-folio
---
```

# Icons

Adding more icons is very simple. `icon` is a list, and each item on the list has a `file` and a `site`. The `file` is the icon file which will be displayed, `site` is the directory from where this file will be displayed.

However, using `site` is optional. If the item doesn't contain a value for site, al-folio will automatically detect and decide whether the link is an absolute URL to some icon on a different website, or a relative URL to an image inside the repository.

Right now, the only eligible options for `site` is `devicons` and `skillicons`

# Repository

`repository` is also a list of all the repositories that can be displayed. Each item needs to be written in the following format: `owner/repository`.

After this, al-folio will automatically generate a card with the proper theme. It will also create a link that will redirect viewers to the repository whenever they click the card.
