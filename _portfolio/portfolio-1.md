---
title: "Budget Analyse in Python"
excerpt: "Inzicht krijgen over mijn jaarlijkse uitgaven door het analyseren <br> van mijn bankafschriften. <br/><img src='/images/budget.png'>"
collection: portfolio
---


Budgetteren is het financieel inzichtelijk maken van je inkomsten en uitgaven. 
Doordat ik erachter kom waar mijn geld maandelijks aan uitgegeven wordt kan ik beslissingen
nemen waarmee mogelijk geld mee kan worden bespaard.

In dit project analyseer ik mijn jaarlijkse uitgaven met behulp van de Python package Pandas.

Voor dit project wil ik antwoord geven op de volgende vragen:

* Hoeveel geld geef ik uit per maand wanneer ik reis met de trein?
* Hoeveel geld geef ik uit per maand aan boodschappen?

# Stap 1: Data verzamelen

Voor dit project maak ik gebruik van een csv bestand gedownload van de ING Bank.
Dit bestand bevat al mijn uitgaven van 01-06-2022 tot 01-06-2023.


<img src='/images/ing.png'>

# Stap 2: Data Bekijken

In deze stap wordt de data ingeladen in Pandas:

* Importeren van de package Pandas
* Inladen van het csv bestand 
* Het bekijken van de eerste 5 rijen om inzicht te krijgen welke kolommen wel/niet relevant zijn.


```python
# Import libraries
import pandas as pd
```


```python
#Read the data
data = pd.read_csv("budget.csv", sep = ',')
df = pd.DataFrame(data)  
df.head(3)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Datum</th>
      <th>Naam / Omschrijving</th>
      <th>Code</th>
      <th>Af Bij</th>
      <th>Bedrag (EUR)</th>
      <th>Mutatiesoort</th>
      <th>Mededelingen</th>
      <th>Tag</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>20230601</td>
      <td>KELKIT NIJMEGEN NLD</td>
      <td>BA</td>
      <td>Af</td>
      <td>9,60</td>
      <td>Betaalautomaat</td>
      <td>Pasvolgnr: 003 31-05-2023 21:21 Transactie: B4...</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>20230601</td>
      <td>KORENGOUD DE ECHTE BAKKER</td>
      <td>BA</td>
      <td>Af</td>
      <td>40,95</td>
      <td>Betaalautomaat</td>
      <td>Pasvolgnr: 003 31-05-2023 08:04 Transactie: B2...</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>20230601</td>
      <td>Klimcentrum Nijmegen B.V</td>
      <td>IC</td>
      <td>Af</td>
      <td>51,00</td>
      <td>Incasso</td>
      <td>Naam: Klimcentrum Nijmegen B.V Omschrijving: 2...</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>

# Stap 3: Data voorbereiding
Zoals te zien in de vorige weergave zijn de meeste kolommen helemaal niet relevant voor de analyse:

* Alleen relevante kolommen worden geselecteerd: Datum, Naam/Omschrijving en bedrag.
* De kolommen worden hernoemd zodat het makkelijker is om mee te werken.


```python
#Select only relevant columns and rename them
df.columns
df = df.rename(columns={'Naam / Omschrijving': 'Naam', 'Bedrag (EUR)': 'Bedrag'})
df = df[['Datum', 'Naam', 'Bedrag']]
df.tail(10)

```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Datum</th>
      <th>Naam</th>
      <th>Bedrag</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>673</th>
      <td>20220603</td>
      <td>Domino's Pizza</td>
      <td>14,90</td>
    </tr>
    <tr>
      <th>674</th>
      <td>20220603</td>
      <td>AH to go 5865 Utrech UTRECHT NLD</td>
      <td>12,80</td>
    </tr>
    <tr>
      <th>675</th>
      <td>20220603</td>
      <td>AH to go Utrecht 5865 UTRECHT</td>
      <td>4,00</td>
    </tr>
    <tr>
      <th>676</th>
      <td>20220602</td>
      <td>IZ STRIK IJS NIJMEGEN NLD</td>
      <td>4,70</td>
    </tr>
    <tr>
      <th>677</th>
      <td>20220602</td>
      <td>ALBERT HEIJN 1021 NIJMEGEN NLD</td>
      <td>22,84</td>
    </tr>
    <tr>
      <th>678</th>
      <td>20220601</td>
      <td>AH to go 5865 Utrech UTRECHT NLD</td>
      <td>3,00</td>
    </tr>
    <tr>
      <th>679</th>
      <td>20220601</td>
      <td>AH to go 5873 Utrech UTRECHT NLD</td>
      <td>10,00</td>
    </tr>
    <tr>
      <th>680</th>
      <td>20220601</td>
      <td>AH to go 5865 Utrech UTRECHT NLD</td>
      <td>2,00</td>
    </tr>
    <tr>
      <th>681</th>
      <td>20220601</td>
      <td>ALBERT HEIJN 1878 ARNHEM NLD</td>
      <td>8,35</td>
    </tr>
  </tbody>
</table>
</div>



# Stap 4: Data opschonen

Om data te kunnen analyseren moet de data in de juiste format zijn:

* Data in kolom bedrag wordt gewijzigd van komma naar punt.
* Data in kolom bedrag van data type string naar data type float.
* Data in kolum datum van data type string naar data type datetime.


```python
df['Bedrag'] = df['Bedrag'].str.replace(',', '.')
df['Bedrag'] = df['Bedrag'].astype(float)
```


```python
df['Datum'] = df['Datum']=pd.to_datetime(df['Datum'],format='%Y%m%d')
df.dtypes
```




    Datum     datetime64[ns]
    Naam              object
    Bedrag           float64
    dtype: object



# Stap 5: Data analyseren part 1

Om erachter te komen hoeveel geld ik uitgeef per maand aan boodschappen en treinreizen is het nodig om
elke transactie te identificeren:

* Elke rij wordt onderzocht die gaat over boodschappen of treinreizen.

* Een nieuwe kolom wordt aangemaakt genaamd categorie. In deze kolom worden rijen weergegeven die gaan over treinreizen, boodschappen of overige.


```python
def add_category(row):
    name = ''
    if 'ah' in row.lower():
        name = 'boodschappen' 
    elif 'albert heijn' in row.lower(): 
        name = 'boodschappen'
    elif 'spar' in row.lower():
        name = 'boodschappen'
    elif 'coop' in row.lower():
        name = 'boodschappen'
    elif 'jumbo' in row.lower():
        name = 'boodschappen'
    elif 'ns groep' in row.lower():
        name = 'treinreizen'
    else:
        name = 'overige'
    return name

```


```python
df['categorie'] = df.Naam.apply(add_category)
```


```python
df.tail(20)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Datum</th>
      <th>Naam</th>
      <th>Bedrag</th>
      <th>categorie</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>663</th>
      <td>2022-06-13</td>
      <td>SWAPFIETS BY BUCKAROO</td>
      <td>14.90</td>
      <td>overige</td>
    </tr>
    <tr>
      <th>664</th>
      <td>2022-06-10</td>
      <td>Thuisbezorgd.nl via Takeaway.com</td>
      <td>19.25</td>
      <td>overige</td>
    </tr>
    <tr>
      <th>665</th>
      <td>2022-06-10</td>
      <td>NS GROEP IZ NS REIZIGERS</td>
      <td>241.39</td>
      <td>treinreizen</td>
    </tr>
    <tr>
      <th>666</th>
      <td>2022-06-08</td>
      <td>5814 NM AH to go NIJMEGEN NLD</td>
      <td>2.00</td>
      <td>boodschappen</td>
    </tr>
    <tr>
      <th>667</th>
      <td>2022-06-08</td>
      <td>AH to go 5865 Utrech UTRECHT NLD</td>
      <td>10.00</td>
      <td>boodschappen</td>
    </tr>
    <tr>
      <th>668</th>
      <td>2022-06-08</td>
      <td>AH to go 5873 Utrech UTRECHT NLD</td>
      <td>3.00</td>
      <td>boodschappen</td>
    </tr>
    <tr>
      <th>669</th>
      <td>2022-06-08</td>
      <td>ABN AMRO Bank NV</td>
      <td>17.00</td>
      <td>overige</td>
    </tr>
    <tr>
      <th>670</th>
      <td>2022-06-08</td>
      <td>ABN AMRO Bank NV</td>
      <td>12.81</td>
      <td>overige</td>
    </tr>
    <tr>
      <th>671</th>
      <td>2022-06-08</td>
      <td>ABN AMRO Bank NV</td>
      <td>14.81</td>
      <td>overige</td>
    </tr>
    <tr>
      <th>672</th>
      <td>2022-06-06</td>
      <td>Thuisbezorgd.nl via Takeaway.com</td>
      <td>22.45</td>
      <td>overige</td>
    </tr>
    <tr>
      <th>673</th>
      <td>2022-06-03</td>
      <td>Domino's Pizza</td>
      <td>14.90</td>
      <td>overige</td>
    </tr>
    <tr>
      <th>674</th>
      <td>2022-06-03</td>
      <td>AH to go 5865 Utrech UTRECHT NLD</td>
      <td>12.80</td>
      <td>boodschappen</td>
    </tr>
    <tr>
      <th>675</th>
      <td>2022-06-03</td>
      <td>AH to go Utrecht 5865 UTRECHT</td>
      <td>4.00</td>
      <td>boodschappen</td>
    </tr>
    <tr>
      <th>676</th>
      <td>2022-06-02</td>
      <td>IZ STRIK IJS NIJMEGEN NLD</td>
      <td>4.70</td>
      <td>overige</td>
    </tr>
    <tr>
      <th>677</th>
      <td>2022-06-02</td>
      <td>ALBERT HEIJN 1021 NIJMEGEN NLD</td>
      <td>22.84</td>
      <td>boodschappen</td>
    </tr>
    <tr>
      <th>678</th>
      <td>2022-06-01</td>
      <td>AH to go 5873 Utrech UTRECHT NLDt</td>
      <td>3.00</td>
      <td>overige</td>
    </tr>
    <tr>
      <th>679</th>
      <td>2022-06-01</td>
      <td>AH to go 5873 Utrech UTRECHT NLD</td>
      <td>10.00</td>
      <td>boodschappen</td>
    </tr>
    <tr>
      <th>680</th>
      <td>2022-06-01</td>
      <td>AH to go 5865 Utrech UTRECHT NLD</td>
      <td>2.00</td>
      <td>boodschappen</td>
    </tr>
    <tr>
      <th>681</th>
      <td>2022-06-01</td>
      <td>ALBERT HEIJN 1878 ARNHEM NLD</td>
      <td>8.35</td>
      <td>boodschappen</td>
    </tr>
  </tbody>
</table>
</div>



# Stap 5: Data analyseren part 2

Om erachter te komen hoeveel geld ik uitgeef per maand aan boodschappen en treinreizen moet de data worden gegroepeerd worden in maanden:

* Een nieuwe tabel maken met de kolommen Maand, Bedrag Trein en Bedrag Boodschappen


```python
trein = df[df.categorie.str.contains('treinreizen')]
trein = trein.groupby(df.Datum.dt.month)['Bedrag'].sum()
trein_bedrag = trein.tolist()
```




    [64.83,
     291.72,
     136.75,
     10.05,
     5.6,
     241.39,
     254.91,
     65.27,
     111.87,
     166.74,
     122.38,
     109.01]




```python
boodschappen = df[df.categorie.str.contains('boodschappen')]
boodschappen = boodschappen.groupby(df.Datum.dt.month)['Bedrag'].sum()
boodschappen_bedrag = boodschappen.tolist()
```


```python
#calculate sum of spendings grouped by month
maand = df.groupby(df.Datum.dt.month)['Bedrag'].sum()
maand = maand.to_frame()
maanden = ['jan 23', 'feb 23', 'mar 23', 'apr 23', 'may 23', 'jun 22','jul 22', 'aug 22', 'sep 22', 'okt 22', 'nov 22', 'dec 22']
maand['Maanden'] = maanden
maand['Bedrag Trein'] = trein_bedrag
maand['Bedrag Boodschappen'] = boodschappen_bedrag
maand = maand.reset_index(drop=True)
maand.set_index('Maanden', inplace=True)
new_index = ['jun 22', 'jul 22', 'aug 22', 'sep 22', 'okt 22', 'nov 22', 'dec 22', 'jan 23', 'feb 23', 'mar 23', 'apr 23', 'may 23'] 
maand = maand.reindex(new_index)
maand = maand[['Bedrag Trein', 'Bedrag Boodschappen']]
maand
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Bedrag Trein</th>
      <th>Bedrag Boodschappen</th>
    </tr>
    <tr>
      <th>Maanden</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>jun 22</th>
      <td>241.39</td>
      <td>314.11</td>
    </tr>
    <tr>
      <th>jul 22</th>
      <td>254.91</td>
      <td>184.99</td>
    </tr>
    <tr>
      <th>aug 22</th>
      <td>65.27</td>
      <td>200.12</td>
    </tr>
    <tr>
      <th>sep 22</th>
      <td>111.87</td>
      <td>167.90</td>
    </tr>
    <tr>
      <th>okt 22</th>
      <td>166.74</td>
      <td>131.01</td>
    </tr>
    <tr>
      <th>nov 22</th>
      <td>122.38</td>
      <td>118.52</td>
    </tr>
    <tr>
      <th>dec 22</th>
      <td>109.01</td>
      <td>185.37</td>
    </tr>
    <tr>
      <th>jan 23</th>
      <td>64.83</td>
      <td>185.23</td>
    </tr>
    <tr>
      <th>feb 23</th>
      <td>291.72</td>
      <td>132.22</td>
    </tr>
    <tr>
      <th>mar 23</th>
      <td>136.75</td>
      <td>242.68</td>
    </tr>
    <tr>
      <th>apr 23</th>
      <td>10.05</td>
      <td>246.42</td>
    </tr>
    <tr>
      <th>may 23</th>
      <td>5.60</td>
      <td>341.21</td>
    </tr>
  </tbody>
</table>
</div>




```python
#De treinreis kosten kloppen niet helemaal. Het bedrijf waarvoor ik werk heeft namelijk mijn reiskosten terugbetaald vanaf de maand februari, 
# dus de kosten over de treinreizen zijn alleen relevant voor de maanden juni 2022 tot januari 2023.
maand_trein =  maand.loc['jun 22': 'jan 23']
maand_trein
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Bedrag Trein</th>
      <th>Bedrag Boodschappen</th>
    </tr>
    <tr>
      <th>Maanden</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>jun 22</th>
      <td>241.39</td>
      <td>314.11</td>
    </tr>
    <tr>
      <th>jul 22</th>
      <td>254.91</td>
      <td>184.99</td>
    </tr>
    <tr>
      <th>aug 22</th>
      <td>65.27</td>
      <td>200.12</td>
    </tr>
    <tr>
      <th>sep 22</th>
      <td>111.87</td>
      <td>167.90</td>
    </tr>
    <tr>
      <th>okt 22</th>
      <td>166.74</td>
      <td>131.01</td>
    </tr>
    <tr>
      <th>nov 22</th>
      <td>122.38</td>
      <td>118.52</td>
    </tr>
    <tr>
      <th>dec 22</th>
      <td>109.01</td>
      <td>185.37</td>
    </tr>
    <tr>
      <th>jan 23</th>
      <td>64.83</td>
      <td>185.23</td>
    </tr>
  </tbody>
</table>
</div>



# Stap 6: Data visualiseren

Een bar plot laat zien hoeveel geld er maandelijks wordt uitgegeven aan reizen en boodschappen.


```python
boodschappen.mean()
```




    204.14833333333334




```python
maand_trein['Bedrag Trein'].mean()
```




    142.04999999999998




```python
#bar treinreizen

bar2 = maand_trein.plot.bar(y='Bedrag Trein', rot=0, figsize=(10,5),  color = 'red')
bar2.axhline(142, color='grey', lw=0.5, ls='--')
bar2.legend(['Gemiddelde','Bedrag Trein'])
bar2 

```




    <AxesSubplot:xlabel='Maanden'>




    
<img src='/images/output_25_1.png'>
    



```python
#bar boodschappen
bar3 = maand.plot.bar(y='Bedrag Boodschappen', rot=0, figsize=(10,5),  color = 'blue')
bar3.axhline(204, color='grey', lw=0.5, ls='--')
bar3.legend(['Gemiddelde','Bedrag Boodschappen'])
bar3 
```




    <AxesSubplot:xlabel='Maanden'>




    
<img src='/images/output_26_1.png'>
    


# Stap 7: Conclusie

## Hoeveel geld geef ik uit per maand aan boodschappen?

De boodschappen grafiek laat zien dat mijn uitgaven die ik samen maak met mijn vriendin hard zijn gestegen na februari.
Dit is mogelijk te verklaren door de inflatie, maar het kan ook zo zijn dat ik toen meer geld ben gaan uitgeven doordat ik
een betere baan had vanaf februari en toen meer verdiende dan daarvoor.

Ik ben verrast dat ik vooral in mei meer geld heb uitgegeven dan daarvoor en verder onderzoek is nodig om te verklaren waarom mijn kosten zoveel zijn gestegen 
ten opzichte van de maanden ervoor (100 euro meer). 

Ik ben wel blij met mijn gemiddelde. 200 euro ligt namelijk onder de uitgaven van de gemiddelde Nederlander. Volgens het [Nibud](https://www.hypotheek.nl/nieuws/geld/gemiddelde-uitgaven-per-maand-huishouden/#:~:text=Gemiddelde%20maandelijkse%20kosten%20voor%20boodschappen&text=1%20persoon%3A%20%E2%82%AC%20237,kind%20van%209%2D13%20jaar) is de gemiddelde uitgaven per persoon 
218 euro (gebaseerd op uitgaven van 2 personen).

## Hoeveel geld geef ik uit per maand aan de trein?

Ik geef best veel geld uit voor de trein. Na verder onderzoek door te kijken naar mijn NS treintransacties (niet opgenomen in deze analyse) ben ik erachter gekomen
dat ik gemiddeld 52 euro uitgeef per maand voor reizen met de trein in het weekend. Ik heb daarom besloten om een NS Weekend Abbonement te nemen van 34 euro per maand 
waardoor ik 18 euro per maand kan besparen met reizen.



