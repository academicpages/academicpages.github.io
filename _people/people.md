---
layout: archive
permalink: /people/
---

# Our Team

![CHBH](/images/IMG_1640.JPG)  

<ul class="people-list">
  {% assign sorted_people = site.people | sort: 'order' %}
  {% for person in sorted_people %}
    <li class="person-item">
      {% if person.photo %}
        <div class="person-photo">
          <img src="{{ person.photo }}" alt="{{ person.title }}">
        </div>
      {% endif %}
      <div class="person-info">
        <a href="{{ person.url }}" class="person-name">{{ person.title }}</a>
        <p>{{ person.excerpt | markdownify }}</p>
        
        <!-- Social Media Links -->
        <div class="social-links">
          <ul>
            {% if person.twitter %}
              <li><a href="{{ person.twitter }}" target="_blank">Twitter</a></li>
            {% endif %}
            {% if person.linkedin %}
              <li><a href="{{ person.linkedin }}" target="_blank">LinkedIn</a></li>
            {% endif %}
            {% if person.scholar %}
              <li><a href="{{ person.scholar }}" target="_blank">Google Scholar</a></li>
            {% endif %}
          </ul>
        </div>
        
      </div>
    </li>
  {% endfor %}
</ul>

