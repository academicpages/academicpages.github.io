---
layout: single
permalink: /coding/netcdf/
author_profile: false
title: <center>NetCDF ANALYSIS
sidebar:
  nav: "sidenav"
toc: true
---
&nbsp;

If you are a scientist working on GeoSciences, which I am glad you are, you might find yourself dealing with a lot of NetCDF files for your project(s). In this Web I will guide you through some basics on how to manipulate these NetCDF files effectively. To start with, I would suggest you some useful softwares to visualize NetCDF files. 

## What is NetCDF
[NetCDF](http://www.unidata.ucar.edu/software/netcdf/) is a set of software libraries and self-describing, machine-independent data formats that support the creation, access, and sharing of array-oriented scientific data. NetCDF was developed and is maintained at Unidata. Unidata provides data and software tools for use in geoscience education and research. Unidata is part of the University Corporation for Atmospheric Research (UCAR) Community Programs (UCP). Unidata is funded primarily by the National Science Foundation.The NetCDF source-code is hosted at [GitHub](http://github.com/Unidata/netcdf-c).

## HDFVIEW

If you are working on Windows based system, [HDFVIEW](https://www.hdfgroup.org/) is a superb software to visualize metdata and data inside a netCDF file. You can even have a first bite of the data in image and so on. The Tree Viewer (or panel) shows the objects in each open file, and supports the navigation and editing of those objects. Multiple files can be viewed and edited, and both HDF4 and HDF5 files can be opened. The viewing and editing operations work for both HDF4 and HDF5, although some operations cannot be implemented for HDF4. For more detailed description of how to use it, see the [HDFVIEW overview](https://support.hdfgroup.org/products/java/hdfview/UsersGuide/ug04treeview.html).


## ncdump command for UNIX users
The ncdump tool generates the CDL text representation of a netCDF dataset on standard output, optionally excluding some or all of the variable data in the output. The output from ncdump is intended to be acceptable as input to ncgen. Thus ncdump and ncgen can be used as inverses to transform data representation between binary and text representations. 
ncdump uses '_' to represent data values that are equal to the _FillValue attribute for a variable, intended to represent data that has not yet been written. If a variable has no _FillValue attribute, the default fill value for the variable type is used unless the variable is of byte type.

UNIX syntax for invoking ncdump:
<pre>
% ncdump  [ -c | -h]  [-v var1,...]  [-b lang]  [-f lang] [-l len]  [ -p fdig[,ddig]]  [ -n name]  [input-file]
</pre>
Please refere [here](http://www.bic.mni.mcgill.ca/users/sean/Docs/netcdf/guide.txn_79.html) for the meaning of the command option.
For example, say you have a NetCDF named foo.nc, to Show the header information in the output, you do 
<pre>
% ncdump -h foo.nc
</pre>

## ncview for NetCDF visualizaiton on UNIX
Ncview is a visual browser for netCDF format files. It is very simple to ue and can display the content of netCDF files graphicaly. Typically you would use ncview to get a quick and easy, push-button look at your netCDF files. You can view simple movies of the data, view along various dimensions, take a look at the actual data values, change color maps, invert the data, etc. It runs on UNIX platforms under X11, R4 or higher. For more information, check out the README file; you can also see a representative screen image (GIF, 66K) of ncview in action. 
[Download the source](ftp://priede.bf.lu.lv/pub/TIS/apskatei/ncview/ncview-2.1.1.tar.gz) for version 2.1.1
A tutorail on how to use it can be found [here]()
 
To use it, at the command prompt, just type "ncview" followed by the name of your netcdf file:
<pre>
% ncview foo.nc
</pre>
Two windows will appear, the control window and the display window. 

 **<span style="color:red">Focus now, the following sessions introduce several useful programs designed to facilitate manipulation and analysis of self-describing data stored in the netCDF format</span>**
 
 
LOL,I am stil working on the following session
## NetCDF Operators(NCO)
## Climate Data Operators (CDO)
## NCAR command language (NCL)
