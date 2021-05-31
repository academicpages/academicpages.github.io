---
title: 'Visualización del crecimiento urbano'
date: 2021-05-28
permalink: /posts/2021/05/blog-post-buildings/
tags:
  - Python
  - Geopandas
  - Catastro
---

Siguiendo la idea viral de [Dominic Royé](https://dominicroye.github.io/en/2019/visualize-urban-growth/)
de crear una visualización en R del crecimiento de las ciudades a partir de los datos del
[Catastro](http://www.catastro.meh.es/webinspire/index.html), en este post os muestro cómo llevarlo a cabo usando Python y el paquete
de datos espaciales Geopandas.  

{% if post.excerpt != post.content %}
    <a href="{{ site.baseurl }}{{ post.url }}">Read more</a>
{% endif %}

El desarrollo del script está basado en la código de [Jorge Monge](https://github.com/Jorge-Monge/cadastral_mapping)
que ha sido adaptado para poder ser usado con cualquier ciudad de España.   


[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/rtalaverag/cadastral_buildings/HEAD)


Para cambiar la ciudad a visualizar sólo hay que cambiar la variable ``` province = "Granada" ```
por la provincia en la que se encuentra la ciudad a representar, y ``` city = "Granada" ```
con la ciudad que queremos representar. El buffer original está adaptado para la
representación de Granada, pero se puede variar cambiando el valor ``` dist_buffer = 2000 ```
en la sección relativa a **City buffer and intersect**  



![alt text](/images/posts/Granada.png)
