ReadMe for ImageAssess.exe -- Image Retargeting Quality Assessment(Liu et al. EUROGRAPHICS 2011)
------------------------------------------------------------------------
If you use this program, please cite the following paper in your research:

[1] Yong-Jin Liu, Xi Luo, Yu-Ming Xuan, Wen-Feng Chen, Xiao-Lan Fu. 
Image Retargeting Quality Assessment. 
Computer Graphics Forum (regular issue of Eurographics 2011), 
Vol. 30, No. 2, pp. 583-592, April 2011.
------------------------------------------------------------------------
ImageAssess.exe needs five parameters as input:
ImageAssess oriImg regImg salOri salReg saveTxt

oriImg:Input an original image. e.g. "E:\\ImageAssess\\oriImg.png"

regImg:Input an retargeted image. e.g. "E:\\ImageAssess\\regImg.png"

salOri:Input the saliency map of the original image. e.g. "E:\\ImageAssess\\salOri.png"

salReg:Input the saliency map of the retargeted image. e.g. "E:\\ImageAssess\\salReg.png"

saveTxt:The text file name to save the result score. e.g. "E:\\ImageAssess\\result.txt"

Note: AttRunDemo.bat runs an example
------------------------------------------------------------------------
For the salient map, you can define the map by yourself depending on the application.
Currently we use one of the two methods:
(2) Graph based visual saliency: http://www.klab.caltech.edu/~harel/share/gbvs.php
(3) Using a simple user interface to interactively specify the salient map 
------------------------------------------------------------------------
This program is compiled using VC++ 2010. If some .dll are absent in your computer, 
you may also need the Microsoft Visual C++ 2010 Redistributable Package:
http://www.microsoft.com/download/en/details.aspx?id=5555