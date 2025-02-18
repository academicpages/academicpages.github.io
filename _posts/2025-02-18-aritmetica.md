---
title: 'Aritmética de la ausencia: niños desaparecidos en Ecuador, 2017-2024'
date: 2025-02-18
permalink: /posts/2025/02/aritmetica/
tags:
 - Desaparecidos
 - Ecuador
---


En estos tiempos salvajemente tristes y tristemente grotescos, la disección de las heridas sociales mediante datos se ha convertido en quizá la única liturgia razonable para intentar hacer sentido de nuestra eterna catástrofe nacional. 

En esta expedición analítica, me aventuro en la más perturbadora de las métricas sociales: la desaparición de niños. Para ello, me armo—y me protejo—con la objetividad impasible de *Python* y la reconfortante distancia que el código proporciona frente a esta tragedia.

## 1. Cosechando desaparecidos  
Extraje el registro oficial de los menores ecuatorianos catalogados como "desaparecido" o bien "desaparecido y encontrado muerto (en circustancias no atribuibles a accidentes)", mediante el portal web "Datos Abiertos"—esta suerte de confesionario donde nuestros gobernantes depositan las estadísticas sobre sus fracasos institucionales. Con ello, importamos bibliotecas y cargamos el registro:

```python
# Importar bibliotecas
import pandas as pd
import folium
from folium.plugins import HeatMapWithTime

# Cargar datos
ruta_archivo = r"desaparecidos.csv"
data = pd.read_csv(ruta_archivo, encoding='latin1')
```



## 2. La alquimia temporal  
La primera hechicería reside en transmutar registros crudos en series temporales:

```python
# Convertir fecha y filtrar rango
data['Fecha'] = pd.to_datetime(data['Fecha'], format='%m/%d/%Y')
data = data[(data['Fecha'] >= '2017-01-01') & (data['Fecha'] <= '2024-12-31')]
data = data.sort_values('Fecha')  # Ordenar cronológicamente

# Crear secuencia de días (2007-01-01 a 2023-12-31)
fechas = pd.date_range(start='2017-01-01', end='2024-12-31', freq='D').strftime('%Y-%m-%d').tolist()
```

Esto incluye un remuestreo diario para resolución temporal fina—cada observación representando no solo un número, sino un día en que el hijo de alguien no volvió a casa.


## 3. Termodinámica de las desapariciones
Dada la secuencia de fechas de desapariciones, damos dos pasos extra: primero, extraemos información geográfica de longitud y altitud de cada desaparición; y, segundo, empleamos técnicas de visualización geoespacial con *folium*. De esa manera, podemos generar un mapa de datos acumulativos *diarios* durante un período de ocho ochos, desde 2017 hasta 2024—es lo que hay disponible en "Datos Abiertos", pero ya realicé una solicitud de información.

```python
# Generar datos acumulativos diarios
heat_data = []
puntos_acumulados = []

for fecha in fechas:
    # Filtrar datos 
    mask = data['Fecha'].dt.strftime('%Y-%m-%d') <= fecha
    puntos_dia = data[mask][['Latitud', 'Longitud']].values.tolist()
    
    puntos_acumulados = puntos_dia  # Actualizar acumulado 
    heat_data.append(puntos_acumulados.copy())

# Crear mapa
mapa = folium.Map(
    location=[data['Latitud'].mean(), data['Longitud'].mean()],
    zoom_start=7,
    tiles='CartoDB positron'
)

# Añadir heatmap con deslizante
HeatMapWithTime(
    heat_data,
    index=fechas,
    radius=10,
    auto_play=False, 
    min_speed=10,
    max_speed=50,
    gradient={0.3: 'blue', 0.6: 'yellow', 0.7: 'red'}
).add_to(mapa)

# Guardar
mapa.save(r"\heatmap_diario_acumulativo.html")
```

Con estos pasos —reproducibles desde la comodidad de su hogar— he parido este mapa audiovisual, coronado por el himno patrio como banda sonora de lo inexplicable: como estadística, durante el período 2017-2024, contabilicé un total de 738 menores "desaparecidos" o "desaparecidos pero encontrados muertos (en circustancias no atribuibles a accidentes)". Un promedio de 92 desapariciones al año.

*Prima facie*, las desapariciones de niños, niñas y adolescentes parecen coincidir con la conocida cartográfica del narcotráfico y del crimen organizado —coincidencias geográficas de las que ciertos políticos prefieren no hablar. Pero, ¿qué sé yo, un simple esclavo de variables que no ha tenido mejor que hacer que transmutar *pequeñas ausencias* en pequeños píxeles?

Aquí la verdadera pregunta es ¿qué ve usted, querido conciudadano? ¿La danza salvaje del crimen organizado, o simples estadísticas sin patrón alguno?

<div style="text-align: center;">
<div style="background-color: #dddddd; padding: 8px;">
<strong>
Desaparecidos: Niños, niñas y adolescentes (2017-2024)
</strong>
</div>
<div style="text-align: center;">
<video width="100%" controls>
  <source src="https://arduinotomasi.github.io/assets/videos/desaparecidos.mp4" type="video/mp4">
</video>
</div>