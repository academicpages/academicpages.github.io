---
title: "[Tableau] Average rent prices in Ireland"
excerpt: "Dashboard of historical Average Rent Prices Ireland<br/>
<img src='https://raw.githubusercontent.com/jvilchesf/portfolio.github.io/refs/heads/main/images/portfolio_viz_1_tableau_Ireland.png' width = 300 height = 300 >"
collection: portfolio
---

## Overview  

The objective of this project is to create a visualization to compare rent prices in Ireland across different years and regions of the country.  
The deliverable is a Tableau Dashboard, which has been uploaded to the Tableau Public server.

The country of Ireland, where I lived for two years, was going through a housing crisis, and I wanted to understand how significant this crisis was in terms of rent prices. I also wanted to know the percentage by which prices had increased since COVID.

## Tools and technologies

* To approach this small project I used:
    * Python: Using the requests and pandas libraries, I successfully retrieved from a public repository, got geo coordinates and structured the data.
    * Tableau: Using Tableau I created a dashboard to show the data already structured.

## Workflow Diagram

* This diagram is intended to provide an overview of the workflow.

<div style="text-align: center;">
    <img src="https://raw.githubusercontent.com/jvilchesf/portfolio.github.io/refs/heads/main/images/Workflow_diagram.png" alt="Workflow Diagram" width="200" height="200">
</div>

## Dataset Description and Methodology

### Source: https://data.cso.ie/ 
- URL Rent prices: https://data.cso.ie/table/RIA02
- URL Census: https://data.cso.ie/table/F1001


### Rent Prices Dataset - 300.000+ rows

| **Column**            | **Description**                                      |
|------------------------|------------------------------------------------------|
| STATISTIC Label        | Type of statistic measured (e.g., average rent).     |
| Year                  | Year of the data.                                    |
| Number of Bedrooms    | Number of bedrooms in the property.                  |
| Property Type         | Type of property (e.g., apartment, house).           |
| Location              | Geographical area of the property.                   |
| UNIT                  | Unit of measurement (e.g., Euros, square meters).    |
| VALUE                 | The numerical value of the statistic.                |

### Census Dataset - 200+ rows

| **Column**            | **Description**                                      |
|------------------------|------------------------------------------------------|
| Statistic Label       | Type of statistic measured (e.g., population).       |
| CensusYear            | The year the census data was collected.              |
| County                | The county where the data is associated.             |
| Sex                   | Gender category (e.g., Male, Female).                |
| UNIT                  | Unit of measurement (e.g., people, percentage).      |
| VALUE                 | Numerical value of the statistic.   


### Preprocessing: Steps taken to clean, transform, or augment the data.

* **Clean Rent Data:** 
    * Format column names
    * Drop unnecessary columns
    * Remove null values 
    * Group Data  

                ```python
                # Function to clean and process the Rent dataset
                def CleanDataRent(dfRent):
                # Rename columns to make them more concise and consistent
                dfRent = dfRent.rename(columns={
                    'Number of Bedrooms': 'Number_of_bedrooms',  # Replace spaces with underscores
                    'Property Type': 'Property_Type',
                    'VALUE': 'Price'
                })

                # Drop unnecessary columns that are not relevant for the analysis
                dfRent = dfRent.drop(columns=['STATISTIC Label', 'UNIT'])

                # Define a condition to clean rows with unwanted or null values in the dataset
                # Remove rows where 'Number_of_bedrooms' or 'Property_Type' contains unwanted values
                indexDropRentBed = dfRent[
                    (dfRent['Number_of_bedrooms'] != 'All bedrooms') |  # Exclude "All bedrooms" rows
                    (dfRent['Property_Type'] != 'All property types')   # Exclude "All property types" rows
                ].index

                # Remove rows where 'Price' is empty while other key fields have valid values
                indexDropRentPrice = dfRent[
                    (dfRent['Price'] == '') &                              # Empty price
                    (dfRent['Year'].notnull()) &                          # Valid year
                    (dfRent['Location'].notnull()) &                      # Valid location
                    (dfRent['Number_of_bedrooms'] == 'All bedrooms') &    # All bedrooms specified
                    (dfRent['Property_Type'] == 'All property types')     # All property types specified
                ].index

                # Drop the identified rows from the DataFrame
                dfRent = dfRent.drop(indexDropRentBed)
                dfRent = dfRent.drop(indexDropRentPrice)

                # Group the data by 'Number_of_bedrooms' and 'Property_Type', summing up the 'Price' column
                df_group = dfRent.groupby(['Number_of_bedrooms', 'Property_Type'])['Price'].sum()

                # Return the cleaned Rent DataFrame
                return dfRent

* **Clean Census Data:**    

    *   Drop unnecessary columns
    *   Format column names
    *   Parse columns data type  

                ```python
                # Function to clean and process the Census dataset
                def CleanDataCens(dfCensus):
                    # Group the dataset by 'UNI' and sum the 'Male' column (example, might be placeholder logic)
                    df_group = dfCensus.groupby(['UNI'])['Male'].sum()

                    # Drop unnecessary columns that are not relevant for the analysis
                    dfCensus = dfCensus.drop(columns=['STATISTIC', 'Statistic', 'TLIST(A1)', 'UNI'])

                    # Rename columns to make them more meaningful and consistent
                    dfCensus = dfCensus.rename(columns={
                        'C02779V03348': 'CensusCountyIndex',  # Rename unclear column to a meaningful name
                        'Male': 'CensusMale',
                        'Female': 'CensusFemale',
                        'Both sexes': 'CensusBothSex',
                        'CensusYear': 'Year'
                    })

                    # Parse the 'CensusBothSex', 'CensusMale', and 'CensusFemale' columns as integers,
                    # filling null values with 0 before conversion
                    dfCensus['CensusBothSex'] = dfCensus['CensusBothSex'].fillna(0).astype('int64')
                    dfCensus['CensusMale'] = dfCensus['CensusMale'].fillna(0).astype('int64')
                    dfCensus['CensusFemale'] = dfCensus['CensusFemale'].fillna(0).astype('int64')

                    # Group the data by 'Year' and 'County', summing up the 'CensusBothSex' column
                    censusGroup = dfCensus.groupby(['Year', 'County'])['CensusBothSex'].sum()

                    # Return the cleaned Census DataFrame
                    return dfCensus

* **Data Augmentetion:**    

    *   Create a "Location" column base on State/Province.
    *   Use "Location" to get "Latitued" and "Longittued

                ```python
                # Function to add standardized location information and geographic coordinates to the DataFrame
                def add_location(dfRent):
                    # Create a new column 'State/Province' initialized with 'Location' values
                    dfRent['State/Province'] = dfRent['Location']
                    # Initialize 'cityCountMark' column to store 'City' or 'County' classification
                    dfRent['cityCountMark'] = ''

                    # Iterate over each row in the DataFrame
                    for index, row in dfRent.iterrows():
                        County = row['State/Province']
                        # If 'State/Province' contains a comma, split and take the second part
                        if ',' in County:
                            dfRent.at[index, 'State/Province'] = County.split(',')[1].strip()
                        else:
                            # Otherwise, split by space and take the first part
                            dfRent.at[index, 'State/Province'] = County.split(' ')[0]

                    # Append ' County' to 'State/Province' values
                    dfRent['State/Province'] = dfRent['State/Province'] + ' County'
                    # Apply 'cityCountMark' function to classify each location
                    dfRent['cityCountMark'] = dfRent.apply(cityCountMark, axis=1)
                    # Update 'Location' field using 'updateLocation' function
                    dfRent['Location'] = dfRent.apply(updateLocation, axis=1)
                    # Set 'Country' field to 'Ireland'
                    dfRent['Country'] = 'Ireland'

                    # Group by 'Location' and sum the 'Price' column
                    dfRent_location = dfRent.groupby(['Location'])['Price'].sum().reset_index()
                    # Apply 'get_coordinates' function to retrieve latitude and longitude for each location
                    dfRent_location['Coordinates'] = dfRent_location['Location'].apply(get_coordinates)
                    # Split 'Coordinates' into separate 'Latitude' and 'Longitude' columns
                    dfRent_location[['Latitude', 'Longitude']] = pd.DataFrame(dfRent_location['Coordinates'].tolist(),
                                                                            index=dfRent_location.index)

                    # Merge the coordinates back into the original DataFrame
                    dfRent = dfRent.merge(dfRent_location[['Location', 'Coordinates', 'Latitude', 'Longitude']], on='Location',
                                        how='left')

                    # Return the updated DataFrame
                    return dfRent  

## 5 Methodology
    
### Data Visualization Workflow:

* I used Tableau to create three main visuals to analyze how rent prices have changed over the years:
    * A map visualization to filter data by each county in Ireland.  

    <img src="https://raw.githubusercontent.com/jvilchesf/portfolio.github.io/refs/heads/main/images/portfolio_viz_1_TabeauMap.png" alt="Map" width="500" height="600">

    * A horizontal bar chart to compare the year-over-year differences in average rent prices.

    <img src="https://raw.githubusercontent.com/jvilchesf/portfolio.github.io/refs/heads/main/images/portfolio_viz_1_TabeauHorizontalMap.png" alt="Map" width="500" height="600">

    * A text table to display detailed data for each city within each county.

    <img src="https://raw.githubusercontent.com/jvilchesf/portfolio.github.io/refs/heads/main/images/portfolio_viz_1_TabeauTextTable.png" alt="Map" width="500" height="600">


## 6 Results and Insights
*   The graph makes it easy to see that prices began increasing around 2015, not just after COVID, with rising trends observed across all counties.
*   Most of the largest counties, such as Dublin and those surrounding it, as well as Cork, Limerick, and Galway, have higher prices and show similar behavior.  

## 7 Code Repository  
The code for this project is hosted on GitHub. You can access the repository via the following link:  

[Housing Rent Analysis in Ireland - GitHub Repository](https://github.com/jvilchesf/Housing_rent_Ireland/tree/main)  

## 8 Visualizations  
The interactive Tableau dashboard showcasing the analysis can be accessed below:  


[RTB Average Monthly Rent in Ireland - Tableau Dashboard](https://public.tableau.com/app/profile/jose.miguel.vilches.fierro/viz/RTBAverageMonthlyRentIreland/Dasboard_1_test#1)
