---
title: "HyClus Viz"
date: 2019-08-08
excerpt: "A simple example for HSI Clustering Visualization<br/><img src='/files/portfolio/HyClus/0-500x300.png'>"
collection: portfolio
---

This is a short project where computer science and electrical engineering students worked on the application of convolutional autoenconders and high dimensional data visualization techniques. We worked with samples characterized by hyperspectral images.


The Context
======

In the first execution of the Data Science Project course (Data Science Project CC5214) of the Department of Computer Science, of the Faculty of Physical and Mathematical Sciences of the University of Chile, our laboratory proposed the project "Clusterization and Identification of mineral species from Hyperspectral images". 

It is in this context 3 students worked on the formulation, analysis and evaluation of this project for processing real data of monthly composites from comminution feeders of 3 different productive sectors of a large mining company in active work nationwide.

In this project, the students were able to carry out the task of researching and implementing deep machine learning systems in the analysis of high-dimensional hyperspectral images. This work has made it possible to complement scientific and visualization tools that we are currently promoting and disseminating in the national mining industry.

From the results obtained by the team, the techniques for displaying clustering results using Big Data stand out, which have allowed us to improve our results reporting system.


The data
======

We work with hyperspectral image data. In these images, information on the spatial distribution of objects is combined with a deep characterization of the electromagnetic reflection of their components in hundreds of different bands of the spectrum.

![img](/files/portfolio/HyClus/0.png)



The acquisition System
------

We have two hyperspectral cameras. Each one is a scanline of hundreds of spatial pixels. One camera provides information in the VNIR (between 400 and 1000 nm), while the second provides bands in the SWIR (between 1000 and 2500 nm).
![img](/files/portfolio/HyClus/1a.jpg)


We have a mounting system for both cameras that allows them to be positioned on a conveyor belt. On this tray it is possible to position a variety of containers to handle various types of samples.
![img](/files/portfolio/HyClus/1.jpg)

The system is complemented with a set of lighting with halogen and Led sources in order to appropriately cover the reflectance spectrum in which the cameras can acquire information.
![img](/files/portfolio/HyClus/1b.jpg)

The acquisition
------

We have a set of samples, each characterized with DRX and DRF laboratory analysis. Due to the scope of this project, we will leave this information aside for the moment. Focusing only on the clustering of the data.

The set corresponds to one sample per month (monthly composition) during the year 2018. Furthermore, each sample comes from 3 different plants, and in two levels of different size.

This generates a set of 72 samples. Each sample is a set of granulated material.

For its hyperspectral characterization, a group of trays is distributed on the tray.

![img](/files/portfolio/HyClus/2.png)

Mapping the distribution of the samples is maintained

![img](/files/portfolio/HyClus/3.png)

In this way it is possible to segment and define the samples individually. From the captured image, individual containers are generated in HDF5 with each sample.

![img](/files/portfolio/HyClus/4.png)

Normally these containers, for each sample, provide a hyperspectral image that preserves both spatial and spectral information.

For this analysis we will omit the spatial information, only keeping the isolated spectra for each sample. This is possible due to the level of crushing of the material, since most of the spatial correlations have been lost at this level of pulverization.

The Clustering and Visualization
======

Samples
------

At this stage, for each granulometry level (average grain size in the sample), for each plant, and for each month, a number of pixels (spectra) are available that characterize the sample. Some of the distributions of the number of spectra are presented (more detailed information is confidential due to the origin of the data).

![img](/files/portfolio/HyClus/5.png)

![img](/files/portfolio/HyClus/6.png)


Spectra Examples
------

The spectral content of the samples is homogeneus, so clasical endmember identification is not a robust approach. In addition data is altered by enviromental conditions and outliers.

![img](/files/portfolio/HyClus/10.png)

Showing some spectra organized by the 3 plants (in the vertical axis) is clear that no simple separation of the data in this domain can be achieved without processing the info

![img](/files/portfolio/HyClus/11.png)

![img](/files/portfolio/HyClus/11b.png)

In the case of the granulometry (the grain sample size) a visual difference can be appreciated between the to groups

![img](/files/portfolio/HyClus/12.png)

![img](/files/portfolio/HyClus/12b.png)

In the case of sorting the spectra by the origin month, no visual organization is observed

![img](/files/portfolio/HyClus/13.png)

![img](/files/portfolio/HyClus/13b.png)



Deep Autoencoders 
------

For this work the use of the individual spectrum as the input was considered. A preliminary approach corresponded to apply a convolution autoencoder to attempt reduce the dimensionality of the hyperspectral data. Here, an initial hard reduction to 4 dimensions was considered by using keras from tensorflow. 

```python
from tensorflow.keras import layers, models, callbacks
from sklearn.preprocessing import MinMaxScaler, minmax_scale
X_max_min = MinMaxScaler().fit_transform(X)

_input = layers.Input(shape=(X.shape[1],))

encoded = layers.Dense(128, activation='tanh', kernel_initializer='orthogonal')(_input)
encoded = layers.Dense(64, activation='tanh', kernel_initializer='orthogonal')(encoded)
encoded = layers.Dense(32, activation='tanh', kernel_initializer='orthogonal')(encoded)
encoded = layers.Dense(16, activation='tanh', kernel_initializer='orthogonal')(encoded)


encoded = layers.Dense(4, activation='tanh', kernel_initializer='orthogonal')(encoded)

encoded = layers.Dense(16, activation='tanh', kernel_initializer='orthogonal')(encoded)
encoded = layers.Dense(32, activation='tanh', kernel_initializer='orthogonal')(encoded)
decoded = layers.Dense(64, activation='tanh', kernel_initializer='orthogonal')(encoded)
decoded = layers.Dense(128, activation='tanh', kernel_initializer='orthogonal')(decoded)
decoded = layers.Dense(X.shape[1], activation='sigmoid')(decoded)

autoencoder = models.Model(_input, decoded)
autoencoder.compile(optimizer='rmsprop', loss='binary_crossentropy')

```

With the respective fitting:

```python
kwargs = dict(monitor='val_loss')
kwargs.__setitem__('patience', 5)
kwargs.__setitem__('verbose', 1)

_early = callbacks.EarlyStopping(**kwargs)

kwargs = dict(monitor='val_loss')
kwargs.__setitem__('patience', 3)
kwargs.__setitem__('min_lr', 1e-6)
kwargs.__setitem__('verbose', 1)
kwargs.__setitem__('mode', 'auto')

learnig_rate = callbacks.ReduceLROnPlateau(**kwargs)

_callbacks = [_early, learnig_rate]

autoencoder.fit(X_max_min, X_max_min,
                epochs=30, verbose=2,
                batch_size=256, callbacks=_callbacks,
                shuffle=True,
                validation_split=0.1)


```

```python
Epoch 00021: ReduceLROnPlateau reducing learning rate to 1e-06.
1101/1101 - 8s - loss: 0.6287 - val_loss: 0.6062
Epoch 22/30
1101/1101 - 8s - loss: 0.6287 - val_loss: 0.6062
Epoch 23/30
1101/1101 - 9s - loss: 0.6287 - val_loss: 0.6062
Epoch 24/30
1101/1101 - 8s - loss: 0.6287 - val_loss: 0.6062
Epoch 25/30
1101/1101 - 8s - loss: 0.6287 - val_loss: 0.6062
Epoch 26/30
1101/1101 - 8s - loss: 0.6287 - val_loss: 0.6062
Epoch 27/30
1101/1101 - 8s - loss: 0.6287 - val_loss: 0.6062
Epoch 28/30
1101/1101 - 8s - loss: 0.6287 - val_loss: 0.6062
Epoch 29/30
1101/1101 - 8s - loss: 0.6287 - val_loss: 0.6062
Epoch 30/30
1101/1101 - 8s - loss: 0.6287 - val_loss: 0.6062
<tensorflow.python.keras.callbacks.History at 0x7fbcc7ac5208>
```


Reduced Spectra by Autoencoder (4 bands)
------

After the encoded representation of the data, it is possible to recreate the visualization of the spectra grouped by the avaible categories.

Grouped by Plant 

![img](/files/portfolio/HyClus/21.png)

Grouped by Size

![img](/files/portfolio/HyClus/22.png)

Grouped by Month

![img](/files/portfolio/HyClus/24.png)

Example of a decoded spectrum from the autoencoder

![img](/files/portfolio/HyClus/25.png)


Reduced Spectra by Autoencoder (16 bands)
------

Again, it is possible to recreate the visualization of the spectra grouped by the avaible categories for the data encoded to 16 bands.

Grouped by Size 

![img](/files/portfolio/HyClus/31.png)

Grouped by Plant

![img](/files/portfolio/HyClus/32.png)

Grouped by Month

![img](/files/portfolio/HyClus/33.png)

Example of a decoded spectrum from the autoencoder

![img](/files/portfolio/HyClus/34.png)


TNSE
======

[T-distributed Stochastic Neighbor Embedding(t-SNE)](https://towardsdatascience.com/t-distributed-stochastic-neighbor-embedding-t-sne-bb60ff109561) lies in the category of unsupervised dimensionality reduction techniques, that applies a non-linear dimensionality reduction approach where the focus is on keeping the very similar data points close together in lower-dimensional space.

The approach was developed as an unsupervised machine learning algorithm for visualization by [Laurens van der Maaten](https://en.wikipedia.org/w/index.php?title=Laurens_van_der_Maaten&action=edit&redlink=1) and [Geoffrey Hinton](https://en.wikipedia.org/wiki/Geoffrey_Hinton). It is relevant that outliers do not impact t-SNE. 


![img](/files/portfolio/HyClus/40.png)

In this strategy, the probability density of a pair of points is proportional to its similarity. For nearby data points, 

\\[ p(j \| i) \\] 

will be relatively high, while for points widely separated, p(j &#124; i) will be lower.

![img](/files/portfolio/HyClus/41.png)

A central stage of the technique requires to find a low-dimensional data representation that minimizes the mismatch between Pᵢⱼ and qᵢⱼ using gradient descent based on Kullback-Leibler divergence(KL Divergence)

[More details can be found in the repository of the t-SNE project, from its author](https://lvdmaaten.github.io/tsne/)


We will reduce to two dimensions the visualization from t-SNE.

```python
from sklearn.preprocessing import LabelEncoder

def tsne_scatter(x, colors, class_names):
    palette = np.array(sns.color_palette("hls", len(class_names)))
    figure = plt.figure(figsize=(8, 8))
    ax = plt.subplot(aspect='equal')
    sc = ax.scatter(x[:,0], x[:,1], lw=0, s=40, 
                    c=palette[LabelEncoder().fit_transform(colors)])
    plt.xlim(-25, 25); plt.ylim(-25, 25)
    ax.axis('off'); ax.axis('tight')
    for class_name in class_names:
        xtext, ytext = np.median(x[colors == class_name, :], axis=0)
        txt = ax.text(xtext, ytext, class_name, fontsize=18)
        txt.set_path_effects([
            PathEffects.Stroke(linewidth=5, foreground="w"),
            PathEffects.Normal()])
```

TSNE for our HSI data reduced by PCA
------

```python
X, y = random_sampling(X_reduced_pca, labels_triplets[:, 1], 5000)
X_train_embedded = TSNE(n_components=2, perplexity=40).fit_transform(X)
tsne_scatter(X_train_embedded, y, np.unique(y))
```

Grouped by Size 

![img](/files/portfolio/HyClus/61.png)

Grouped by Plant

![img](/files/portfolio/HyClus/62.png)

Grouped by Month

![img](/files/portfolio/HyClus/63.png)



TSNE for the Convolutional Autoencoder (4 Bands)
------

Grouped by Size 

![img](/files/portfolio/HyClus/71.png)

Grouped by Plant

![img](/files/portfolio/HyClus/72.png)

Grouped by Month

![img](/files/portfolio/HyClus/73.png)




TSNE for the Convolutional Autoencoder (16 Bands)
------


Grouped by Size 

![img](/files/portfolio/HyClus/81.png)

Grouped by Plant

![img](/files/portfolio/HyClus/82.png)

Grouped by Month

![img](/files/portfolio/HyClus/83.png)



Data splitted by grain size
======

In order to improve the process, the data will be splitted by the size category. Then samples with granulometry "Minus 100" will be grouped in a set will the other set will to consider the data of granulometry "Plus 100"

TSNE M100 for the Convolutional Autoencoder (16 Bands)
------

Clustering of data set M100 Labelled by Plant of origin

![img](/files/portfolio/HyClus/91.png)

Clustering of data set M100 For the Plant 1, labelled by Month

![img](/files/portfolio/HyClus/92.png)

Clustering of data set M100 For the Plant 2, labelled by Month

![img](/files/portfolio/HyClus/93.png)

Clustering of data set M100 For the Plant 3, labelled by Month

![img](/files/portfolio/HyClus/94.png)


TSNE P100 for the Convolutional Autoencoder (16 Bands)
------

Clustering of data set P100 Labelled by Plant of origin

![img](/files/portfolio/HyClus/96.png)

Clustering of data set P100 For the Plant 1, labelled by Month

![img](/files/portfolio/HyClus/97.png)

Clustering of data set P100 For the Plant 2, labelled by Month

![img](/files/portfolio/HyClus/98.png)

Clustering of data set P100 For the Plant 3, labelled by Month

![img](/files/portfolio/HyClus/99.png)


Classification of the available categories
======

As a reference k-means elbow method was computed to compare the number of clusters for the global data. For all representations the number of clusters estimated was consistent.

```python
from sklearn.cluster import KMeans

def compute_elobow(data, title):
    errors = list()
    for k in tqdm_notebook(range(1, 10)):
        km = KMeans(n_clusters=k, n_jobs=-1)
        km.fit(data)
        errors.append(km.inertia_)
    plot_elbow(errors, title)

def plot_elbow(errors, title):
    fig, ax = plt.subplots()
    ax.plot(np.arange(1, len(errors) + 1), errors)
    ax.set_title(title)
    ax.set_xlabel('K')
    ax.set_ylabel('SSE')
    plt.show() 

```

![img](/files/portfolio/HyClus/100.png)







