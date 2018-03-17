Reclassifying NH Lakes


```import matplotlib.pyplot as plt
import geopandas as gpd
```

### File path below

```
fp = "C:/Users/Kaitlyn/Desktop/GeoPython/Reclass/data/NH_lakes_polygons.shp"
```
```
data = gpd.read_file(fp)
```

### Examining the columns. I'm going to get rid of irrelevant columns in the shapefile.

```
data.head(2)
```
```
selected_cols = ['COUNTY', 'AREA', 'LAKE', 'geometry']
data = data[selected_cols]
```

#### Now I'm going to plot the data by area

```
data.plot(column='AREA', linewidth=0.05)
```

#### Remove any white space
```
plt.tight_layout()
```

### Create custom classifier - everything under 1 sq km in one class, everything else in another

```
def binaryClassifier(row, source_col, output_col, threshold):
    if row[source_col] < threshold:
        row[output_col] = 0
    else:
        row[output_col] = 1
    return row
```

#### Calculating the area of lakes and converting from meters into sq km

```
data['area_km2'] = data['AREA'] / 1000000
```
```
l_mean_size = data['area_km2'].mean()
```

### Create an empty column for the classifier to reside
```
data['small_big'] = None
```

### Now apply the classifier to the data:

```
data = data.apply(binaryClassifier, source_col='area_km2', output_col='small_big', threshold=l_mean_size, axis=1)
```

### And here is the resulting plot:
```
data.plot(column='small_big', linewidth=0.05, cmap="seismic")
```

### Save the file as a new shapefile:
```
outfp_data = r"C:/Users/Kaitlyn/Desktop/GeoPython/Reclass/NH_lakes.shp"
data.to_file(outfp_data)
```
