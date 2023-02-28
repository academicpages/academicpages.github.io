---
layout: archive-search
title: "Publications"
permalink: /publications/
author_profile: true
---

{% if author.googlescholar %}
You can also find my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a>.</u>
{% endif %}

{% include base_path %}

<html>
<head>

<h1>HEY</h1>
</head>
<body>
<div id="result">HELLO TEST</div>
<script>
<script type="text/javascript" src="data.json"></script>
        <script type="text/javascript" >
            function load() {
                var mydata = JSON.parse(data);
                alert(mydata.length);

                var div = document.getElementById('data');

                for(var i = 0;i < mydata.length; i++)
                {
                    div.innerHTML = div.innerHTML + "<p class='inner' id="+i+">"+ mydata[i].firstName +"</p>" + "<br>";
                }
            }
        </script>
</script>

</body>
</html>
<!-- {% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}
 -->
