#!/bin/bash

outfile="logs/publish_brain_$(date +"%Y%m%d%H%M").html"
/bin/python3 -m jupyter nbconvert --to html --execute publish_brain.ipynb --output $outfile \
    && firefox $outfile
