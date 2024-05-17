{% for year in sorted_publications_by_year %}
### {{ year.name }}
<table style="width:100%;border:0px;border-spacing:0px;border-collapse:separate;margin-right:auto;margin-left:auto;">
  {% for post in year.items %}
  <tr>
    <td style="border: none; padding:2.5%;width:25%;vertical-align:middle;max-width:100px;max-height:100px">
      <img src="/{{post.image}}" alt="project image" style="width:auto; height:auto; max-width:100%;" />
    </td>
    <td style="border: none; padding:2.5%;width:75%;vertical-align:middle">
      <h3>{{post.title}}</h3>
      {{post.authors}}
      <em>{{post.venue}}</em>, {{ post.date | date: "%Y" }}.
      <br>
      {{post.affiliation}}
      <br>
      <div class="publication-links">
        {% if post.paperurl %}
          <a href="{{post.paperurl}}"><i class="fas fa-file-alt"></i> [paper]</a>
        {% endif %}
        {% if post.page %}
          <a href="{{post.page}}"><i class="fas fa-globe"></i> [website]</a>
        {% endif %}
        {% if post.code %}
          <a href="{{post.code}}"><i class="fas fa-code"></i> [code]</a>
        {% endif %}
        {% if post.video %}
          <a href="{{post.video}}"><i class="fas fa-video"></i> [video]</a>
        {% endif %}
        {% if post.poster %}
          <a href="{{post.poster}}"><i class="fas fa-image"></i> [poster]</a>
        {% endif %}
        {% if post.slides %}
          <a href="{{post.slides}}"><i class="fas fa-slideshare"></i> [slides]</a>
        {% endif %}
        {% if post.dataset %}
          <a href="{{post.dataset}}"><i class="fas fa-database"></i> [dataset]</a>
        {% endif %}
      </div>
      <p></p>
      {{ post.excerpt }}
    </td>
  </tr>
  {% endfor %}
</table>
{% endfor %}