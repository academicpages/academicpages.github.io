---
title: 'Building evolution'
date: 2021-05-28
permalink: /posts/2021/05/blog-post-buildings/
tags:
  - Python
  - Geopandas
  - Catastro
---

<div align="justify"> Siguiendo la idea viral de Dominic Royé (https://github.com/dominicroye) de crear
una visualización en R del crecimiento de las ciudades a partir de los datos del
Catastro, en este post os muestro cómo llevarlo a cabo usando Python y el paquete
de datos espaciales Geopandas.  

El desarrollo del script está basado en la código de Jorge Monge
(https://github.com/Jorge-Monge/cadastral_mapping) que ha sido adaptado para
poder ser usado con cualquier ciudad de España. </div>

<div align="center"> [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/rtalaverag/cadastral_buildings/HEAD) </div>

<div align="justify"> Para cambiar la ciudad a visualizar sólo hay que cambiar la variable ``` "province" ```
por la provincia en la que se encuentra la ciudad a representar, y ``` "city" ``` con la
ciudad que queremos representar. El buffer original está adaptado para la
representación de Granada, pero se puede variar cambiando el valor ``` "dist_buffer" ```
en la sección relativa a ``` **City buffer and intersect** ```  </div>

![alt text](/images/posts/Granada.png)
