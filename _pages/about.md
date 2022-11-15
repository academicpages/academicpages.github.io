---
permalink: /
title: "About me"
excerpt: "About me"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

I have completed Bachelor of Engineering in E&C department from Sardar Vallabhbhai Patel Institute of Technology (SVIT, Vasad). Currently I am working with 3D Surgical, as a project lead in the software R&D department. Having more than 4 years of experience in NDT (Non Destructive Testing) software development and hardware integration, Medical 3D rendering software development, embedded software development, Computer Vision, Artificial Intelligence, Image processing and custom imaging filter design. I am passionate about creating equitable spaces in our tech community and open to collaborate on imaging ,AI/ML based research.


## Badges

[![@dwijmistry11's Holopin board](https://holopin.me/dwijmistry11)](https://holopin.io/@dwijmistry11)


<!-- Include the library. -->
<script
  src="https://unpkg.com/github-calendar@latest/dist/github-calendar.min.js">
</script>

<!-- Optionally, include the theme (if you don't want to struggle to write the CSS) -->
<link
  rel="stylesheet"
  href="https://unpkg.com/github-calendar@latest/dist/github-calendar-responsive.css"
/>

<!-- Prepare a container for your calendar. -->
<div class="calendar">
    <!-- Loading stuff -->
    Loading the data just for you.
</div>

<script>
    GitHubCalendar(".calendar", "dwijmistry11");

    // or enable responsive functionality:
    GitHubCalendar(".calendar", "dwijmistry11", { responsive: true });

    // Use a proxy
    GitHubCalendar(".calendar", "dwijmistry11", {
       proxy (username) {
         return fetch(`https://your-proxy.com/github?user=${username}`)
       }
    }).then(r => r.text())
</script>