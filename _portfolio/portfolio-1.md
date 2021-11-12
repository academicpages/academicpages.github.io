---
title: "Scraping www.wto.org"
excerpt: "Using Python and Selenium in the extraction of Non-tariff measures with certain criteria.<br/><img src='/images/logo_en.gif'>"
collection: portfolio
---

>### Scraper for:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**[www.wto.org](https://www.wto.org)**  

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*The codes are published on [my GitHub](https://github.com/raulsedano2410) you can find [**this scraper**](https://github.com/raulsedano2410/Scraper-www.wto.org) and [many others](https://github.com/raulsedano2410?tab=repositories)*


 >### Sub page to work:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **[i-tip.wto.org/goods/Forms/TableView.aspx](https://i-tip.wto.org/goods/Forms/TableView.aspx)**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*This pivot table was complicated at the beginning, but it was managed to understand it perfectly.*

>### About:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **[Non-tariff measures](https://i-tip.wto.org/goods/Forms/TableView.aspx)**  

*&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;What are "non-tariff measures" (NTMs)?  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;As the term suggests, NTMs may include any policy measures other than tariffs that can impact trade flows. At a broad level, NTMs can usefully be divided into three categories.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;A first category of NTMs are those imposed on imports. This category includes import quotas, import prohibitions, import licensing and customs procedures, and administration fees. A second category of NTMs are those imposed on exports. These include export taxes, export subsidies, export quotas, export prohibitions and voluntary export restraints.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;These first two categories encompass NTMs that are applied at the border, either to imports or to exports. A third and final category of NTMs are those imposed internally in the domestic economy. Such behind-the-border measures include domestic legislation covering health / technical / product / labor / environmental standards, internal taxes or charges, and domestic subsidies.*  

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
*[Complete documentation here](https://www.wto.org/english/res_e/reser_e/ersd201201_e.pdf)*

>### Objective

* Create a database of non-tariff measures (NTMs), based on some important criteria for the development of your study.

>### Imputs

1. Measure/Notification
     

     |Code|Measure|Requiriment|
     |---|---|---|
     |A|Sanitary and Phytosanitary|Emergency|
     |A|Sanitary and Phytosanitary|Regular|
     |B|Technical Barriers to Trade|Regular|
     |D1|Anti dumping|-|
     |D2|Countervailing|-|
     |D31|Safeguards|-|
     |D32|Special Safeguards|-|
     |E32|Quantitative Restrictions|-|
     |E61|Tariff-rate quotas|-|
     |P7|Export Subsides|-|
     |H1,P2|State Trading Enterprices|-|
  
2. Date(s)
 - Measures taken during period of time
     - From 01/01/1988 to 31/12/2020  
     - [x] initiated
     - [x] entered into force  



  

3.  Member(s) imposing the measure  
     * First instance
          * a imposes on b
     * Second instance
          * b imposes on a  

     (a) Peru 


     (b) List of countries

     |         List        |        Of         |    Countries       |
     |         ----        |       ----        |      ----          |
     |        Germany      |  Saudi Arabia, Kingdom of the | Argentina |
     |        Australia    |   Austria         |    Bolivia         |
     |        Brazil       |     Bulgaria      |    Belgium         |
     |        Canada       |     Chile         |     China          |
     |        Cyprus       |    Colombia       | Korea, Republic of |
     |        Costa Rica   |    Cuba           | Denmark            |
     |        Ecuador      |    El Salvador    | Slovenia           |
     |        Spain        |    United States of America | Estonia  |
     |        Russian Federation | Finland     | France             |
     |        Greece       |    Guatemala      | Honduras           |
     |        Hong Kong    |    China          | Hungary            |
     |        India        |    Indonesia      | Ireland            |
     |        Iceland      |    Italy          | Japan              |
     |        Latvia       |    Malaysia       | Malta              |
     |        Mexico       |    Nicaragua      | Norway             |
     |        Panama       |    Paraguay       | Netherlands        |
     |        Peru         |    Poland         | Portugal           |
     |        United Kingdom | Czech Republic  | Dominican Republic |
     |        Slovak Republic | Romania        | Sweden             |
     |        Switzerland  |    Thailand       | Trinidad and Tobago |
     |        Turkey       |    Uruguay        | Bolivarian Republic of Venezuela |
     |        Viet Nam.    |                   |                    |


4. Product(s) affected by the measure
     * All/Any
5. Keywords
     * All/Any

>### Tools  

* Jupyter Notebook
* Python 3.8
* Library

```python
     from selenium.webdriver.support.ui import Select
     from selenium import webdriver
     from selenium.webdriver.common.keys import Keys
     from selenium.webdriver.common.action_chains import ActionChains
     from selenium import webdriver
     from selenium.webdriver.support.ui import WebDriverWait
     from selenium.webdriver.support import expected_conditions as EC
     from selenium.webdriver.common.by import By

     import pandas as pd
     from pandas import Series,DataFrame
     from pandas import ExcelWriter

     import time
     from time import sleep

     import os
     
     import win32com.client
```  

>### Output:  

In the selection and cleaning of Data they asked me to separate SA Codes of 6 digits or more with certain characteristics, I will leave a file (in Spanish) as a production sample

<p><a href="../files/Peru-World.xlsx" download> Click to Download </a></p>


> ### Important:
>---
>The investigation on non-tariff measures is still in progress  
>and has not been published by its author,  
>at the moment I can only share my collaboration as Scraper and data cleaner.  
>I am sure it will be a great job that I will soon share
>barely authorized.
