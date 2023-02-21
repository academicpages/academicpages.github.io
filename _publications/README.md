# Setting up the environment
This only needs to be done once


## Switch to CUDA 11

You will need CUDA 11 for training. 


## Create the environment 

First install conda (if you haven't) and activate conda.
```
conda config --add channels conda-forge
conda config --add channels pytorch
conda config --add channels nvidia
conda config --add channels dglteam
conda create -n ml4co --file environment.txt
conda activate ml4co
pip cache purge
pip install -r requirements.txt -f https://pytorch-geometric.com/whl/torch-1.7.0+cu110.html
```

Also need to install from source an updated version of ecole and could be downloaded from here: https://drive.google.com/file/d/1EbnUlgdnJotCKAyh8M9hqsMvaIvIP0Sq/view?usp=share_link


# Collecting the dataset
Here we assume we are running on a cluster with Slurm. 
Run data collection on a problem set
```
python LNS/LNS.py --problem-set=INDEPENDENT_SET_HARD  --num-solve-steps=30 --neighborhood-size=200 --time-limit=300000 --destroy-heuristic=LOCAL_BRANCHING --mode=COLLECT --submitit=1
```
Here we are collecting data with the expert Local Branching for 30 iterations with neighborhood size 200. The per-iteration runtime limit is hard-coded in the code for 2 hours (can be changed there). So the total time limit needs to be set to be at least 30*2*3600 seconds. Setting submitit=1 will run data collection for all instances found for the problem set, otherwise it will run for only 1 instance (this is useful when you when to debug or fine-tune parameters). 

There are also a set of ready datasets on our Google Drive.

## Train the models
You will need to modify the function call to `train(DATASET_NAME, gnn_type=gat, feat='feat2',loss = 'nt_xent')`, mainly you will need to give a name to your dataset and its location in the code.

After that, simply run (after adjusting the paths to the datasets).
`python LNS/train_neural_LNS.py`

## Test the models

Run this command to test the model
```
python LNS/LNS.py --problem-set=INDEPENDENT_SET_HARD  --num-solve-steps=1000000 --neighborhood-size=200 --time-limit=3600 --destroy-heuristic=ML::GREEDY::CL --mode=TEST_ML_feat2 --gnn-type=gat --model=PATH_TO_MODEL --submitit=1
```
Here, we can set the num-solve-steps to infinity so that it runs w.r.t the time-limit provided. Destroy heuristics must have prefix `ML::SAMPLE` or `ML::GREEDY` (depending on the sampling methods you use, for contrastive learning we recommend GREEDY) and can have mostly arbitrary suffix for your own naming purposes. Again submitit=1 will run testing for all instances and could be set to 0 for debugging or testing single instance.
(Note for myself, need to fix something with mode=TEST_ML_feat2.)
