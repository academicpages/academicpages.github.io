---
layout: academic
permalink: /
excerpt: "Adam Umra — research in integrated sensing and communication, machine learning for signal processing, and reconfigurable intelligent surfaces at Ruhr University Bochum."
author_profile: false
redirect_from:
  - /about/
  - /about.html
---

<section class="profile" aria-labelledby="profile-name">
  <h1 id="profile-name">Adam Umra</h1>
  <p class="profile-subtitle">Doctoral Researcher at Ruhr University Bochum</p>
  <div class="profile-intro">
    <div class="profile-copy">
      <p>I am a doctoral researcher at the <a href="https://www.dks.ruhr-uni-bochum.de/">Chair of Digital Communication Systems</a> at <a href="https://www.ruhr-uni-bochum.de/en">Ruhr University Bochum</a>, Germany.</p>
      <p>My research focuses on <strong>integrated sensing and communication (ISAC)</strong>, <strong>machine learning for signal processing</strong>, and <strong>localization and tracking</strong>. I work on cognitive radar, reconfigurable intelligent surfaces, and reliable wireless communication.</p>
      <p>I received my B.Sc. in 2021 and M.Sc. in 2023 in Electrical Engineering and Information Technology from Ruhr University Bochum.</p>
    </div>
    <figure class="profile-photo">
      <img src="{{ '/images/profile.jpg' | relative_url }}" alt="Adam Umra" width="8256" height="5504" fetchpriority="high">
      <figcaption>&copy; RUB, Marquard</figcaption>
    </figure>
  </div>
  <ul class="profile-links" aria-label="Contact and profiles">
    <li><a href="mailto:{{ site.author.email }}">Email</a></li>
    <li><a href="{{ site.author.googlescholar | escape }}">Google Scholar</a></li>
    <li><a href="https://www.linkedin.com/in/{{ site.author.linkedin }}">LinkedIn</a></li>
    <li><a href="https://github.com/{{ site.author.github }}">GitHub</a></li>
    <li><a href="https://www.dks.ruhr-uni-bochum.de/de/profiles/adam-umra/">University profile</a></li>
  </ul>
</section>

<section aria-labelledby="news">
  <h2 id="news" class="section-heading">News</h2>
  <p class="news-hint" id="news-hint">Latest updates · scroll for more ↓</p>
  <div class="news-box" role="region" aria-labelledby="news" aria-describedby="news-hint" tabindex="0">
  <ul class="news-list">
    {% assign news = site.data.news | sort: "date" | reverse %}
    {% for item in news %}
    <li><time datetime="{{ item.date }}">{{ item.label }}</time><span>{{ item.text | markdownify | remove: '<p>' | remove: '</p>' }}</span></li>
    {% endfor %}
  </ul>
  </div>
</section>

<section aria-labelledby="publications">
  <h2 id="publications" class="section-heading">Publications</h2>
  <p class="section-intro">Journal articles, conference papers, and recent preprints. See also my <a href="{{ site.author.googlescholar | escape }}">Google Scholar profile</a>.</p>
  {% assign publications = site.data.publications_generated | default: site.data.publications %}
  {% assign publication_years = publications | group_by: 'year' | sort: 'name' | reverse %}
  {% for year in publication_years %}
  <section class="publication-year" aria-labelledby="publications-{{ year.name }}">
    <h3 id="publications-{{ year.name }}" class="publication-year-heading">{{ year.name }}</h3>
    <ol class="publication-list">
    {% assign papers = year.items | sort: 'sort_date' | reverse %}
    {% for paper in papers %}
    <li class="publication">
      <h4>{{ paper.title | escape }}</h4>
      <p class="publication-authors">{{ paper.authors | escape | replace: 'Adam Umra', '<strong>Adam Umra</strong>' }}</p>
      <p class="publication-venue"><em>{{ paper.venue | escape }}</em> · {{ paper.year }}{% if paper.status %} <span class="publication-status">{{ paper.status }}</span>{% endif %}</p>
      <ul class="publication-links" aria-label="Links for {{ paper.title | escape }}">
        {% assign reading_links = paper.display_links | default: paper.links %}
        {% for link in reading_links %}
        {% unless link.url contains 'doi.org/' %}
        <li><a href="{{ link.url | escape }}">{{ link.label }}</a></li>
        {% endunless %}
        {% endfor %}
      </ul>
    </li>
    {% endfor %}
    </ol>
  </section>
  {% endfor %}
</section>

<section aria-labelledby="experience">
  <h2 id="experience" class="section-heading">Experience</h2>
  <ul class="experience-list">
    <li>
      <p class="entry-meta">Feb. 2024–present · Bochum, Germany</p>
      <h3>Research Associate, Ruhr University Bochum</h3>
      <p>Research Associate at the <a href="https://www.dks.ruhr-uni-bochum.de/">Chair of Digital Communication Systems</a>.</p>
    </li>
    <li>
      <p class="entry-meta">Mar. 2022–Mar. 2023 · Bochum, Germany</p>
      <h3>Working Student in Wireless Communication / Connected Cars</h3>
      <p class="entry-organization">Volkswagen Infotainment GmbH</p>
      <p>Research in C-V2X, support for the team’s work in standardization organizations, and tool development in Python.</p>
    </li>
  </ul>
  <h3 class="experience-subheading">Education</h3>
  <ul class="experience-list">
    <li>
      <p class="entry-meta">Oct. 2021–Oct. 2023 · Ruhr University Bochum</p>
      <h4>M.Sc. in Electrical Engineering and Information Technology</h4>
      <p>Focus on communication technology, radio frequency, and artificial intelligence.</p>
    </li>
    <li>
      <p class="entry-meta">Oct. 2018–Oct. 2021 · Ruhr University Bochum</p>
      <h4>B.Sc. in Electrical Engineering and Information Technology</h4>
    </li>
  </ul>
</section>
