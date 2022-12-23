{% assign pub_list = site.data.citations | sort: "Year" | reverse %}
{% assign style = include.style | downcase | default: "apa" %}
{% assign include_link = include.link %}

{% if include.venue %}
  {% assign venues = include.venue | downcase | split: ";" %}
{% endif %}

{% if include.year %}
  {% assign years = include.year | split: ";" %}
{% endif %}

{% if include.title_search %}
  {% assign searchterms = include.title_search | downcase | split: ";" %}
{% endif %}

{% if include.venue_search %}
  {% assign venue_searchterms = include.venue_search | downcase | split: ";" %}
{% endif %}

{% if include.author %}
  {% assign authors = include.author | downcase | split: ";" %}
{% endif %}

{% assign counter = 0 %}


<ol>
{% for citation in pub_list %}
  {% if include.venue %}
    {% assign publication = citation.Publication | downcase %}
    {% if venues contains publication %}
      {% assign is_venue = true %}
    {% else %}
      {% assign is_venue = false %}
    {% endif %}
  {% else %}
    {% assign is_venue = true %}
  {% endif %}
  
  {% if include.year %}
    {% if years contains citation.Year %}
      {% assign is_year = true %}
    {% else %}
      {% assign is_year = false %}
    {% endif %}
  {% else %}
    {% assign is_year = true %}
  {% endif %}
  
  {% if include.title_search %}
    {% assign title = citation.Title | downcase %}
    {% assign is_search = false %}
    {% for term in searchterms %}
      {% if title contains term %}
        {% assign is_search = true %}
      {% endif %}
    {% endfor %}
  {% else %}
    {% assign is_search = true %}
  {% endif %}
  
  {% if include.venue_search %}
    {% assign venue = citation.Publication | downcase %}
    {% assign is_venue_search = false %}
    {% for term in venue_searchterms %}
      {% if venue contains term %}
        {% assign is_venue_search = true %}
      {% endif %}
    {% endfor %}
  {% else %}
    {% assign is_venue_search = true %}
  {% endif %}
  
  {% if include.author %}
    {% capture citation_Authors %}
      {% for element in citation %}
        {% if forloop.first %}
          {{ element[1] }}
        {% endif %}
      {% endfor %}
    {% endcapture %}
    {% assign author_list = citation_Authors | downcase %}
    {% assign is_author = false %}
    {% for author in authors %}
      {% if author_list contains author %}
        {% assign is_author = true %}
      {% endif %}
    {% endfor %}
  {% else %}
    {% assign is_author = true %}
  {% endif %}

  {% if is_venue and is_year and is_search and is_author and is_venue_search %}
    {% capture citation_Authors %}
      {% for element in citation %}
        {% if forloop.first %}
          {{ element[1] }}
        {% endif %}
      {% endfor %}
    {% endcapture %}
  
    {% assign size = citation_Authors | size | minus: 2 %}
    {% assign pub_authors = citation_Authors | slice: 0, size | split: ";" %}


    {% assign last_names = "" %}
    {% assign first_names = "" %}
    {% for name in pub_authors %}
      {% assign first_last = name | split: "," %}
      {% assign first_names = first_names | append: first_last[1] %}
      {% assign last_names = last_names | append: first_last[0] %}
      {% if forloop.last == false %}
        {% assign last_names = last_names | append: ";" %}
        {% assign first_names = first_names | append: ";" %}
      {% endif %}
    {% endfor %}
    {% assign first_names = first_names | split: ";" %}
    {% assign last_names = last_names | split: ";" %}

    {% assign formatted_author_list = "" %}

    {% if style == "mla" or style == "chicago" %}
      {% for first_name in first_names %}
        {% if forloop.first == true %} 
          {% assign formatted_author_list = formatted_author_list | append: last_names[forloop.index0] | append: ", " | append: first_name | append: ";" %}
        {% elsif forloop.first == true and forloop.last == true %}
          {% assign formatted_author_list = formatted_author_list | append: last_names[forloop.index0] | append: ", " | append: first_name %}
        {% elsif forloop.last == true %}
          {% assign formatted_author_list = formatted_author_list | append: first_name | append: " " | append: last_names[forloop.index0] %}
        {% else %}
          {% assign formatted_author_list = formatted_author_list | append: first_name | append: " " | append: last_names[forloop.index0] | append: ";" %}
        {% endif %}
      {% endfor %}
    {% elsif style == "apa" or style == "harvard" or style == "vancouver"%}
      {% for first_name in first_names %}
        {% assign first_initial = first_name | slice: 1 %}
        {% assign formatted_author_list = formatted_author_list | append: last_names[forloop.index0] | append: ", " | append: first_initial %}
        {% if style == "apa" or style == "harvard" %}
          {% assign formatted_author_list = formatted_author_list | append: "." %}
        {% endif %}
        {% if forloop.last == false %}
          {% assign formatted_author_list = formatted_author_list | append: ";" %}
        {% endif %}
      {% endfor %}
    {% endif %}
    
    {% if include_link==true %}
      {% assign url = citation.Title | cgi_escape | prepend: "https://scholar.google.com/scholar?q=" %}
      {% capture title_link %}<a href="{{ url }}">{{citation.Title}}</a>{% endcapture %}
    {% else %}
      {% assign title_link = citation.Title %}
    {% endif %}
    
    {% if style == "mla" %}
      <li>
        {{ formatted_author_list | split: ";" | array_to_sentence_string }}. "{{ title_link }}." <em>{{citation.Publication}}</em> ({{citation.Year}}).
      </li>
    {% elsif style == "apa" %}  
      <li>
        {{ formatted_author_list | split: ";" | array_to_sentence_string: "&"}} ({{citation.Year}}). {{ title_link }}. <em>{{citation.Publication}}</em>.
      </li>
    {% elsif style == "chicago" %}
      <li>
        {{ formatted_author_list | split: ";" | array_to_sentence_string }}. "{{ title_link }}." <em>{{citation.Publication}}</em> ({{citation.Year}}).
      </li>
    {% elsif style == "harvard" %}
      <li>
        {{ formatted_author_list | split: ";" | array_to_sentence_string }}, {{citation.Year}}. {{ title_link }}. <em>{{citation.Publication}}</em>.
      </li>
    {% elsif style == "vancouver" %}
      <li>
        {{ formatted_author_list | split: ";" | join: ", " }}. {{ title_link }}. {{citation.Publication}}. {{citation.Year}}.
      </li>
    {% endif %}
    
    {% if include.limit %}
      {% assign counter = counter | plus: 1 %}
      {% if counter == include.limit %}
        {% break %}
      {% endif %}
    {% endif %} 
    
  {% endif %}
{% endfor %}
</ol>
