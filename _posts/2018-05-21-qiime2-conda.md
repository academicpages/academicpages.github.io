---
title: Turning your qiime2 plugin into a conda package
permalink: /posts/2018/06/qiime2-plugin-conda
date: 2018-06-01
tags:
    - qiime2
    - coding
    - python
    - conda
    - portfolio
---

Once you've [made your first qiime2 plugin](/posts/2018/03/qiime2-plugin), you'll need to build it into a conda package and upload it to anaconda.org so others can easily install it.
This tutorial is intended for first-time python developers trying to put their package into conda, and specifically targeted toward people developing plugins for [QIIME 2](https://qiime2.org/).

# Quickstart

1\. Install `conda` and `conda-build`.    

2\. Make the files that make up the conda recipe (`meta.yaml`, which needs you to use your brain, and `build.sh` and `bld.bat` which you just copy from the internet)    

3\. Build your package with `conda-build` (if making a qiime2 plugin, you'll need additional channels).    

 ```
 conda-build pyinstrument/ \
  -c https://conda.anaconda.org/qiime2/label/r2018.4 \
  -c https://conda.anaconda.org/qiime2 \
  -c https://conda.anaconda.org/conda-forge \
  -c defaults \
  -c https://conda.anaconda.org/bioconda \
  -c https://conda.anaconda.org/biocore \
  --override-channels \
  --python 3.5
 ```

4\. Install your package locally.    

 ```
 conda install --offline /path/to/file.tar.bz2
 ````     

5\. Try using your package (if you're installing a qiime2 plugin, try running it in a qiime environment).    

6\. Upload to Anaconda.    

 ```
 anaconda upload /path/to/file.tar.bz2
 ```  

7\. Profit!     

# Documentation

Before you start, here is some useful documentation to be aware of.

The conda tutorials are short and informative. You should read the [tutorial using `skeleton`](https://conda.io/docs/user-guide/tutorials/build-pkgs-skeleton.html) first, then and then the tutorial on [building a package from scratch](https://conda.io/docs/user-guide/tutorials/build-pkgs.html), regardless of which way you plan to build your package.

# Step by step process

## Install conda and conda-build

Follow the [instructions](https://conda.io/docs/user-guide/tasks/build-packages/install-conda-build.html) to install and update `conda` and `conda-build`.

## Read the tutorials

Even if you'll be making your package from scratch, start with the ["building packages with skeleton" tutorial](https://conda.io/docs/user-guide/tutorials/build-pkgs-skeleton.html) and then read the ["building packages from scratch" one](https://conda.io/docs/user-guide/tutorials/build-pkgs.html).

## Make your conda recipe

Packages are specified in a `recipe`, which as far as I can tell means "a collection of files that describe what the package needs and how to install it." A detailed explanation of the files that you need can be found [here](https://conda.io/docs/user-guide/tasks/build-packages/recipe.html).
The recipe is just three files: `meta.yaml`, `build.sh`, and `build.bat`.       

- `meta.yaml` - This contains all the metadata in the recipe, and is the part that you need to use your human brain to fill out. Specifically, you need to tell `conda-build` where to find the source code (either a local path or to a github release), and you also specify the requirements that your package needs. Also, if you want to build a platform-independent version of your package, you specify this in here too.             
- `bld.bat` - this file commands the Windows commands to build the package. You can copy it from the [conda "from scratch" tutorial](https://conda.io/docs/user-guide/tutorials/build-pkgs.html#writing-the-build-script-files-build-sh-and-bld-bat).       
- `build.sh` - this file contains the macOS and Linux commands to build the package, i.e. just `python setup.py install`. You can also copy it from the [conda "from scratch" tutorial](https://conda.io/docs/user-guide/tutorials/build-pkgs.html#writing-the-build-script-files-build-sh-and-bld-bat).        

### meta.yaml

`meta.yaml` is the workhorse of package building, and is where you specify basically everything about your package.
The [conda "building packages" documentation](https://conda.io/docs/user-guide/tasks/build-packages/define-metadata.html) explains all the parts of this file and gives examples.

For the anyone new to the `yaml` data format, note that the top-level IDs in the file don't get filled out!

#### source

This tells `conda-build` where to look for the code when it builds your package.
You can point to either a github release or to a local path.
Note that the way building a package works is that `conda-build` looks for the code specified in the `source` part of `meta.yaml` and does some magic which produces a `.tar.bz2` file that contains your package.
This `.tar.bz2` file is the thing you upload to anaconda.org, and which people download when they run `conda install`.
This means that whatever location you point to in `source` doesn't need to be constantly updated.
It also means that if you make changes to your code, you have to manually re-build the package and re-upload it for those changes to show up on conda.

So, for simplicity's sake, it's often easier to just point `source` to the local path with your main package directory (i.e. the folder that has your `setup.py` file).
In this case, that looks like this:

```
source:
  path: ../
```

But you can also point it to a github *release*, like in the conda documentation example. You can find your releases (or make new ones) by going to your repo on github.com, clicking on `Release` (in the same bar as where your commits, branches, and contributors are shown), and following the directions there.

An important note that if you make and push changes to your code and re-build your package, `conda-build` will still be looking at whatever *release* you point it to - so you need to make a new release with your changes! (This cost me like an hour of debugging, d'oh!)

#### requirements

This part tells `conda-build` and `conda` what other packages your package needs. You need to populate this section yourself. Note that if you want to specify specific package versions, the syntax is `package_name >=version`, with no space between the `>=` and the version number.

[This requirements section](https://conda.io/docs/user-guide/tasks/build-packages/define-metadata.html#requirements) can have multiple sub-sections, but as far as I can tell all you really need (for a simple package, like a qiime2 plugin) are the `build:` and `run:` sections.
The `build` section has whatever packages are in your `setup.py` script (or whatever command is in your `build.sh` file), the `run` section has whatever packages you need to run your package.

#### architecture-independent package

I don't know very much about what's going on here, but if you don't do the following steps, your built conda package will only be installable on machines that have the same OS as yours.

The QIIME 2 developers briefly explained it as follows in [response to one of my questions](https://forum.qiime2.org/t/package-uploaded-to-anaconda-but-not-installable/4139/3?u=cduvallet):

> The [noarch package](https://conda.io/docs/user-guide/tasks/build-packages/define-metadata.html#architecture-independent-packages) lets you upload one build that is compatible on multiple platforms - the caveat here is that it is up to you to know if that is the case or not.

To make architecture-independent package, also add this to your `meta.yaml` file:

```
build:
	noarch: generic
```

If you do `noarch: python` instead, this indicates that your package can use either Python 2 *or* 3 (and is also architecture-independent).

### build files

There's no magic here if you already have a `setup.py` file, because the `build` files just call whatever command you call to install your package (e.g. `python setup.py install`).
The `build.sh` and `bld.bat` files are thus very simple, and can be copied from the [conda "from scratch" tutorial](https://conda.io/docs/user-guide/tutorials/build-pkgs.html#writing-the-build-script-files-build-sh-and-bld-bat).

Note: these are instructions for if you have something simple that can directly be installed with `python setup.py install`. I have no idea what happens if you have something more complicated that you need to do.

## Build your package

Go to your repo's root directory, and run `conda-build pyinstrument/`. This assumes you put your `meta.yaml` and build files in a folder called `pyinstrument`.

If you're working on a qiime plugin, that probably won't work, because you need to tell conda to look for things in lots of different channels and do some other stuff. Thankfully, the qiime2 [development docs](https://dev.qiime2.org/latest/publishing/) are helpful here!

To build a qiime2 plugin, the command you have to run is actually:

```
 conda-build pyinstrument/ \
  -c https://conda.anaconda.org/qiime2/label/r2018.4 \
  -c https://conda.anaconda.org/qiime2 \
  -c https://conda.anaconda.org/conda-forge \
  -c defaults \
  -c https://conda.anaconda.org/bioconda \
  -c https://conda.anaconda.org/biocore \
  --override-channels \
  --python 3.5
```

### Install your package

The [conda documentation](https://conda.io/docs/user-guide/tutorials/build-pkgs.html#building-and-installing) says you can now install your package with the `--use-local` flag:

```
conda install --use-local pyinstrument/
```

However, this didn't work for me (it says that the package isn't found). Rather than troubleshoot this, I found out that you can also install a package directly from the `tar.bz2` file that you just made with the `--offline` flag in `conda-build`.

If you go back to the output of your conda-build command, you should be able to find the path that this `.tar.bz2` file was saved to. Something like:

```
/Users/claire/anaconda/conda-bld/osx-64/q2_perc_norm-1.0-py35_0.tar.bz2
```

So you can try to install the package directly from this:

```
conda install --offline /Users/claire/anaconda/conda-bld/osx-64/q2_perc_norm-1.0-py35_0.tar.bz2
```

Ok, looks like that worked! Woooo!

### Test your package

If you're a noob like me and didn't include any unit tests in your package, you'll want to make sure that your package will actually work once it's installed.

A note that if you're developing a QIIME 2 plugin, you probably want to be in a new qiime environment so you don't mess things up too badly... (If you've forgotten, like I have, go to the Quickstart dev docs to remind yourself how to do this: https://dev.qiime2.org/latest/quickstart/)

```bash
wget https://raw.githubusercontent.com/qiime2/environment-files/master/latest/staging/qiime2-latest-py35-osx-conda.yml
conda env create -n qiime2-dev-condatest --file qiime2-latest-py35-osx-conda.yml
source activate qiime2-dev-condatest
```

Then, you can just type in `qiime` to your command line and see if (1) you get no errors and (2) your plugin shows up in the list of available plugins.

#### Troubleshooting `citations.bib` error

In my case, this didn't work. If I tried to run anything with qiime (e.g. `qiime list`), I got an error that it can't find my `citations.bib` file. That's because I need to tell `setuptools` that it needs to grab additional data beyond just `*.py` files, which it does automatically. Looking at the [cutadapt](https://github.com/qiime2/q2-cutadapt/blob/master/setup.py) plugin, looks like I just need to add this to `setup.py`:

```
setup(
    name="perc-norm",
	...
    package_data={
        'q2_perc_norm': ['citations.bib']
    }
)
```

(A small note: this file path should be given relative to the folder called `q2_perc_norm`, not to the main repo. Here, my citations file is in `~/github/q2_perc_norm/q2_perc_norm/citations.bib` and my `setup.py` file is in `~/github/q2_perc_norm/setup.py`. If you instead put `package_data={'q2_perc_norm': ['q2_perc_norm/citations.bib']}` in `setup.py`, it won't find the right file and you'll keep getting the same error.)

Now, I need to re-build and re-install and re-try.

If re-installing doesn't work, you might want to try clearing everything: uninstall your plugin, clear all the conda-build previous builds, and clear the conda cache. Then, try re-building, re-installing, and re-trying.

```
conda uninstall q2_perc_norm
conda build purge
conda clean --all
```

Another note that if the `source` in your `meta.yaml` points to a github release of your code, you should re-point this to a release that includes any changes you've made (i.e. if you've pushed changes to your github repo, you need to make a new release which includes those changes, and change the release that `meta.yaml` points to). This is why pointing to a local path might reduce some headaches!

# Upload it to Anaconda

Once you've successfully built and installed your package (or plugin) and made sure that it works as expected, the last step is to upload it to anaconda.

Following the [directions in the documentation](https://conda.io/docs/user-guide/tutorials/build-pkgs-skeleton.html#optional-uploading-packages-to-anaconda-org) (after making an anaconda.org account), it's really easy:

```
anaconda upload /Users/claire/anaconda/conda-bld/noarch/q2_perc_norm-2018.4.0-py35_0.tar.bz2
```

# Install the package from conda

Your final step is to try installing the package from conda. Make sure you've uninstalled any local versions that you have, and that you're not in the package's directory when you try to `conda install` your new package. You'll need to include your channel in the call to `conda install`, but you can just copy and paste this from [your package's installation instructions](https://anaconda.org/cduvallet/q2_perc_norm) on anaconda.org.

If you're working on a qiime2 plugin, you'll want to make sure you're in the qiime2 environment (otherwise, conda doesn't know where to find all the qiime2-related modules and packages) and with the latest version of qiime2.

```
source activate qiime2-2018.4
conda install -c cduvallet q2_perc_norm
```

Another "gotcha!" that got me is that if you want to see which packages are available in your channel (i.e. your account), you can run this command:

```
conda search -c <your_channel_name>
```

# Side note: including pip packages

If one of your requirements is a package on pip, you'll need to first put it into conda before you can make your plugin conda-installable. (From [this still open issue](https://github.com/conda/conda-build/issues/548) on conda, seems like this is currently the only way!)
This happened to me in building my [distribution-based OTU calling](https://github.com/cduvallet/q2-dbotu) plugin.

Thankfully, if the package is already pip-installable, this shouldn't be too difficult. `conda skeleton` can help you get started:

```
conda skeleton pypi dbotu
```

This makes a folder called `dbotu` with a `meta.yaml` file in it. Then, because it has the build command directly in the `meta.yaml` file, you can just try building a conda package from this directly:

```
conda-build meta.yaml
```

Note that if you need to look in different conda channels for certain requirements, this will break. You can fix it with something like:

```
conda-build meta.yaml -c conda-forge
```

Then, go through the process of building, testing, and uploading your package to anaconda.org.
After that, you can get back to developing your QIIME 2 plugin.
