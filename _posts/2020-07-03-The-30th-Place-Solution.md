# 30th place solution in Kaggle

This post is also available in the [Kaggle forums](https://www.kaggle.com/c/trends-assessment-prediction/discussion/163744).

First of all thanks to the organizers to putting together this challenging and interesting competition!

I've seen many good and well written and well developed solutions on the challenge ... mine is neither. But I just wanted chip in, as I might have used some feature engineering that hasn't been used as widely. Unfortunately I don't have the time right now to dig into it in detail, but will just give you a rough description about what I did.

## Reflections

A personal note on how I perceived the challenge. I was really exciting to see this challenge, this should lie in my area of expertise, so why not give it a try. So I did, wrote a for my terms successful EDA notebook, got into the data and somehow got to 13th place. But, as people noted, there was not much going on in terms of discussion etc., so I might have gotten a
bit complacent with my position and did not develop much further. Also I might have gotten a bit annoyed, because I couldn't get my errors on `domain1_var1` and the `domain2` vars done as much as I liked.

Then life happened, vacation, deadlines, an online hackathon. Not much space for the challenge, and suddenly there are 10 days left, I have a deadline coming up, and find myself around place 50th on the leaderboard. So some panic sets in and also some craziness, so I rewrote the analysis, and preprocessing from scratch, run all the different models. Stack them up and well suddenly it's place 34, and 30 on the private leaderboard - my best competition so far.

## Preprocessing and Features

### Targets

1. I decided to perform stratified cross-validation on my data, so I used `KNN(n_clusters=15)` on
the target variables, setting the missing values to 0, so that this will be taken
into account for the stratification approach.
2. Then I imputed the missing data using `sklearn.impute.IterativeImputer` to get
values there. This seemed to be a good balance for me between discarding the data
or just filling in a constant. However, I didn't really look into the imputations
afterwards...

### Preprocessing and Feature Engineering

* `loading.csv` - Discarded `IC_20` - Seemed to be very different between train and test (discussions and kernels)
* `fnc.csv` - Reordering the data for use with `nilearn.connectome.vec_to_sym_matrix`
* Extracting data from the 4D feature maps. I have a kernel out-there showing how this can be done using different
`Masker` objects using `nilearn.input_data`. I extracted the sets `schaeffer` (400 brain regions),
`msdl`, and `basc` (197 regions) here.
* Graph-based features: Several publications also focus on using graph-theory based descriptions of functional
connectivity as features for machine learning classifiers. So I used the "Brain Connectivity Toolbox", `bct.py`
to derive features. These were just a ton of global and local descriptions, also at different thresholdings of the
connectivity matrices (derived from `fnc`). Around 1700 features in total (with sometimes really bad numerical
issues), which I somehow hacked away in the preprocessing before my stacking data. This will be named `fnc_graph`.
* Combined data, I also created the set `loadfnc`, combining `fnc` and `loading` data, and `loadmsdl` combining
`msdl` and `loading`. Finally, I also used a `loadnoise` set, where I added some random intercept and Gaussian noise
to the `loading` data (differently for each subset). If that helped at all, I couldn't unfortunately test.

## Stacking, stacking, stacking

I stacked tons of models (32 for each feature) using different regression approaches, and
sometimes different preprocessing. `ConnectivityMeasure` (shortened to `CM`).
is a class from `nilearn.connectome`,
that can be used to transform a `n x t` matrix in to a `n x n` connectivity matrix, using differnt
kinds of connectivity. The nice thing is, it also fits into sklearn-pipelines as a vectorized version
of the matrix is possible.

| Data Set | Preprocessing SVR, LGBM | Preprocessing Regression |
| -------- | ----------------------- | ------------------------ |
| `basc`   | CM(tangent), PCA(whiten=True), RobustScaler() | CM(correlation), PCA(whiten=True) |
| `msdl`   | CM(tangent), PCA(whiten=True), RobustScaler() | CM(correlation), PCA(whiten=True) |
| `schaeffer`   | CM(tangent), PCA(whiten=True), RobustScaler() | CM(correlation), PCA(whiten=True) |
| `fnc`   | PCA(whiten=True) | abs(fnc) < 0.15 = 0,  PCA(whiten=True) |
| `fnc_pca`   | None | abs(fnc) < 0.15 = 0,  None |
| `loading` | RobustScaler() | RobustScaler() |
| `fnc_graph` |Numerical fixes, PCA(whiten=True), RobustScaler() | Numerical fixes, PCA(whiten=True), RobustScaler() |
| `loadmsdl` | PCA(whiten=True), RobustScaler() | PCA(whiten=True), RobustScaler() |
| `loadfnc` | RobustScaler() | RoubstScaler() |
| `loadnoise` | RobustScaler() | RobustScaler()|

### SVR

I used sklearns `SVR` using both a linear and a rbf kernel on the datasets `basc`, `msdl`, `schaeffer`, `fnc_pca`, `loading`, and `fnc_graph`. To figure out the best parameters I applied `skopt.BayesianSearchCV` with 35 iterations (objective mean absolute error). Parameters optimized where `C`, `epsilon` and `n_components` for PCAs.

So here are 2 x 6 = 12 models.

### Regression

In this competition I somehow came to like the `LassoLars` regression of sklearn. So that's what I am using here. The feature selection of it seemed to help actually.
Running models on `basc`, `msdl`, `schaeffer`, `fnc`, `loading`, `fnc_graph`, `loadmsdl`, `loadfnc`, and `loadnoise`. This time optimizing mean squared error using `BayesianSearchCV` for `alpha` and `n_components`.

So 9 models.

### LightGBM

Same datasets as for `Regression`. Optimizing tree parameters and PCA, best model defined by mean absolute error.

Another 9 models.

### 2D CNN

I also tried to get some more spatial information into the model as well
so I set up a small 2D CNN having:

* Conv2D Layer, with ReLU activation
* Maxpooling (2, 2)
* Flatten
* Dropout()
* Dense(1)

Where the number of `filters`, `kernel_size`, `Dropout`, `learning_rate`, and the `loss` (mae, mse), where found through `BayesianSearchCV`.

## Training and Prediction

I used the same approach for all models and the final stacking model:

1. Optimize hyperparameters on 5-Folds.
2. Retrain model on CV-Data
3. Evaluate on hold-out set
4. Retrain on all data
5. Predict on test set.

The final stacking model was again a `LassoLars` regression, on the outputs of the 31 models. I actually preprocessed the predictions, by slapping a `RobustScaler` in just for good measure.

## Thoughts

I learned quite a lot from the competition, but have to say that I am not really satisfied with what I did (my best competition so far...), and see a lot of room for improvement.

### Work smarter

I think the most annoying part for me is, that I just stacked tons of models. In the end not even thinking much about *why* I am doing it. I just wanted to get that 0.001 Leaderboard boost, to get a little edge. But, if I had invested my time more into careful tuning, preprocessing, and careful model selection, I think I would have gotten more out in the last weekend of the competition, than I did here. In the end, I was mostly waiting for models to finish running and to start the next set of long calculations.

### Evaluate, evaluate, evaluate

So far, my intuition on evaluating locally and avoiding overfitting got me quite far (I got my first silver medal basically because of an incredibly heavy shake up of the leaderboard, pushing me a couple of 100 places or so to the top). Here I think I was actually quite lucky - see the forum posts where people discuss about the lack of a shake up.

### Get a team

Next time I am in this situation, I think I will team up. Also I apologize to the people who contacted me and I didn't get back to. Here it was mostly bad timing, but I think there is some much to gain in terms of insights, when you can discuss your solutions :)

And of course much more. 