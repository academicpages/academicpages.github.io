---
title: Developing a qiime2 plugin for non-developers
permalink: /posts/2018/03/qiime2-plugin
date: 2018-03-27
tags:
    - python
    - coding
    - microbiome
    - qiime2
    - portfolio
---

As a side project from the meta-analysis, we developed a method to [correct for batch effects in microbiome case-control studies](https://doi.org/10.1371/journal.pcbi.1006102).
When we posted the preprint on biorxiv, Greg Caporaso emailed Sean and asked him if he'd like to put our method into qiime2.
I happily volunteered - I'd heard a presentation about qiime2 and was super pumped about their plugin setup, where anyone can incorporate their method into qiime's suite of tools, and I was excited to see how doable it was.
The learning curve was a little steep at first, but not as bad as I expected!
Here, I've cleaned up my notes into a guide through my development process.
I hope this is helpful to others like me, who aren't trained computer scientists/developers, but who are keen and able to learn the programming stuff to make their tools more useful to more people.

# Developing a plug-in for dummies

A first reminder that for any qiime2 functions to work, you need to be in the qiime2 virtual environment. If you're trying to run things and getting errors like `ImportError: No module named qiime2`, then you're probably not in the right environment.

After following the qiime [installation instructions](https://docs.qiime2.org/2018.2/install/native/#install-qiime-2-within-a-conda-environment):

```
source activate qiime2-2018.2
```

It's also very helpful to look through multiple existing plugins to get a sense of how other people have done things. I recommend looking at more than one example, since this will give you a sense of which parameters/setup/styles are required, and which are flexible. Plugins that were really helpful to me when I made this were the [q2-ghost-tree](https://github.com/JTFouquier/q2-ghost-tree) user-created plugin, as well as the massive [q2-diversity](https://github.com/qiime2/q2-diversity) plugin (specifically the `q2_diversity.beta_group_significance` for its example using `MetadataColumn[Categorical]` data.

## Getting started (babby's first plugin)

### Make the repo and basic files

First, make your repo. In the main directory, make a `setup.py` file that gives some broad info about your plugin to-be.

Within the repo, make a directory with the same name as your plugin. In this folder, make your `plugin_setup.py` file.

`plugin_setup.py` is where you register all the functions/methods/visualizers that your plugin will have. In other words, these will be the things that your plugin *does*, the things you type after your plugin name (for example, `perc-norm percentile-normalize` for the registered `percentile-normalize` function).

### Basic debugging

Once you have your content set in `plugin_setup.py`, it's good to start with some basic debugging to make sure there are no errors:

```
python plugin_setup.py
```

Note for debugging: if you want to run a script (e.g. `plugin_setup.py`) directly, make sure to add your main repo directory to your `PYTHONPATH` so that anything you import from your project in the scripts is discoverable.

```
export PYTHONPATH=~/github/q2-perc-norm/
```

For example, it looks like the common practice is to have a file for each method in the same directory as `plugin_setup.py`. In the plugins I used as examples, these files are typically named `._method_name.py`, and are imported at the top of `plugin_setup.py` (e.g. `from._method_name import method_name`). This import statement only works if the folder is in your `PYTHONPATH`.

As an alternative to messing with your `PYTHONPATH`, which is easy to forget to do each time, you can use `pip install -e .` from the main directory which contains `setup.py`.
From what I understand, this installs an editable version in development mode in your current directory (you'll see an `egg-info` directory after you run this).

### Install the plugin

When you're ready to actually try doing stuff, you'll need to run `python setup.py install` (from the main repo folder) for your qiime plugin to be callable from the command line.

```
python setup.py install
```

If you've made updates to your plugin's command line interface, don't forget to [clear the cache](https://docs.qiime2.org/2018.2/plugins/developing/#testing-your-plugin-with-q2cli-during-development) (`qiime dev refresh-cache`) before running this!

Note that the name of your plugin is what you put in your `plugin_setup.py` file:

```
plugin = Plugin(
    name='perc-norm',
    ...
    )
```

You can double check that it worked by just typing `qiime` on the command line and seeing if your plugin shows up. Then, you can just try running the plugin:

```
qiime perc-norm
```

This will show you the general plugin info, and you should see all of the functions that you registered at the bottom:

```
(qiime2-2018.2) 19:24-claire:~/$ qiime perc-norm

Usage: qiime perc-norm [OPTIONS] COMMAND [ARGS]...

  Description: This QIIME 2 plugin performs a model-free normalization
  procedure where features (i.e. bacterial taxa) in case samples are
  converted to percentiles of the equivalent features in control samples
  within a study prior to pooling data across studies.

  Plugin website: http://www.github.com/cduvallet/q2-perc-norm

  Getting user support: Raise an issue on the github repo:
  https://github.com/cduvallet/q2-perc-norm

  Citing this plugin: Sean Gibbons, Claire Duvallet, and Eric Alm.
  "Correcting for batch effects in case-control microbiome studies". bioRxiv
  (2017) https://doi.org/10.1101/165910

Options:
  --help  Show this message and exit.

Commands:
  percentile-normalize  Percentile normalization
```

Then you can try running each function and see if the inputs are what you want them to be:

```
(qiime2-2018.2) 19:24-claire:~/$ qiime perc-norm percentile-normalize

Usage: qiime perc-norm percentile-normalize [OPTIONS]

  Converts OTUs in case samples to percentiles of their distribution in
  controls.

Options:
  --i-table ARTIFACT PATH FeatureTable[RelativeFrequency]
                                  The feature table containing the samples
                                  which will be percentile normalized.
                                  [required]
  --m-metadata-file MULTIPLE PATH
                                  Metadata file or artifact viewable as
                                  metadata. This option may be supplied
                                  multiple times to merge metadata.
                                  [required]
  --m-metadata-column MetadataColumn[Categorical]
                                  Column from metadata file or artifact
                                  viewable as metadata. Sample metadata column
                                  which has samples labeled as "case" or
                                  "control". Samples which are not labeled are
                                  not included in the output table.
                                  [required]

...

  --help                          Show this message and exit.
```

Woop! The plugin was set up correctly!

### Side note on MetadataColumn[Categorical]

I specified a `MetadataColumn[Categorical]` required parameter in my `plugin_setup.py` function, and I wasn't sure how this would be parsed or treated by the underlying code. It turns out that qiime automatically parses it and turned into the two inputs you see: `--m-metadata-file` and `--m-metadata-column`. This is how I made the metadata an input to my function (in `_percentile_normalize.py`):

```
def percentile_normalize(table: biom.Table,
                         metadata: qiime2.CategoricalMetadataColumn,
                         n_control_thresh: int=10,
                         otu_thresh: float=0.3) -> biom.Table:
```

I used some functions I found in another qiime plugin to ensure that sample IDs in the metadata and OTU table matched, and then converted the metadata column into a pandas Series object.

```
metadata = metadata.filter_ids(table.ids(axis='sample'))
metadata = metadata.drop_missing_values()
table = table.filter(metadata.ids)
metadata = metadata.to_series()
```

The developers on the qiime2 forum were REALLY helpful to figure this out, since there currently isn't really much documentation on the different qiime2 data types.

## Testing your plugin

### Get your toy data ready

Now that babby's first plugin is set up, you'll want some toy data to play with. My plugin needs a metadata file and an OTU table. Metadata files can be passed in directly as tab-separated, but OTU tables need to first be converted to qiime artifacts. Unfortunately, it's not [currently](https://forum.qiime2.org/t/tsv-to-featuretable/2349) possible to directly import a tsv feature table so we'll have to go through biom format first.

Note that OTUs need to be in rows and samples are in columns for these biom tables (even though I can't find this clearly stated in the biom format documentation, grr). Also, you need to make sure you've converted to relative abundance already.

I wrote a script on the repo to make a fake OTU table. Run it or download the tables from my [repo](https://github.com/cduvallet/q2-perc-norm/tree/master/test_data).

```
python make_fake_data.py
```

Then I need to prepare my test data for qiime:

```
biom convert -i test_otu_table.transpose.txt -o test_otu_table.transpose.biom --table-type="OTU table" --to-hdf5
qiime tools import --input-path test_otu_table.transpose.biom --type 'FeatureTable[RelativeFrequency]' --source-format BIOMV210Format --output-path test_otu_table.transpose.qza
```

A note that `qiime tools` has a useful suite of tools to play around and double check your data, if you're getting errors.

### Run plugin and compare against existing code

I want to make sure that my plugin is behaving like I expect it to. First, I run Sean's github code:

```
python ~/github/percentile_normalization/percentile_norm.py -i test_otu_table.txt -case test_case_samples.txt -control test_control_samples.txt -o test_out.percentile_sean.txt
```

And I can run percentile normalization on the qiime artifact.

```
qiime perc-norm percentile-normalize --i-table test_otu_table.transpose.qza --m-metadata-file test_metadata.txt --m-metadata-column DiseaseState --o-perc-norm-table test_out.percentile_qiime.qza
qiime tools export test_out.percentile_qiime.qza --output-dir test_out_qiime
mv test_out_qiime/feature-table.biom test_out.percentile_qiime.biom
rm -r test_out_qiime
biom convert -i test_out.percentile_qiime.biom -o test_out.percentile_qiime.txt --to-tsv
```

Then, if I load up the two output OTU tables in python, I see that their values for the originally non-zero entries are identical. Wahoo!

```
import pandas as pd

sean = pd.read_csv('test_out.percentile_sean.txt', sep='\t', index_col=0)
qiime = pd.read_csv('test_out.percentile_qiime.txt', sep='\t', index_col=0, skiprows=1)
qiime = qiime.T

sean[qiime.columns] == qiime
```

Ta da! A plugin that works just like normal python code!
