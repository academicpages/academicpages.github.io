```{r setup, include=FALSE}
knitr::opts_chunk$set(echo = TRUE)
library(tidyverse)
library(tidyr)
library(kableExtra)
library(ggplot2)
library(dplyr)
library(HelpersMG)
library(choroplethr)
library(choroplethrMaps)
library(lubridate)
library(rmarkdown)
library(markdown)
```

 <!-- the chunk above was used for loading the necessary packages for this report.Some additional unused packages were also loaded. --> 
 
# COVID-19 Research Project

 <!-- above is project title --> 
 
### BIOL390: Reproducible Research, Summer 2020
**Copyright © (2020) Bethany Riess**
 <!-- above is copyright information -->
 
## A. Abstract (tl;dr)

 <!-- an abstract was labeled above with level two header and printed below --> 
 
COVID-19 research project evaluating the COVID-19 trends from states that never issued stay-at-home orders compared to states that did. The information gathered for this project took place from the beginning of the pandemic until August 16th, 2020.
	
## B. Introduction

 <!-- following the abstract, the header was placed on line 25(above) and the introduction to the project is printed below on line 27  --> 
 
COVID-19 (*Orthocoronavirinae*) is the name given to the virus that has caused a pandemic starting at the end of 2019. This virus is also known as SARS‑CoV‑2.First identified in December of 2019, the virus outbreak began in Wuhan, China and quickly spread throughout the globe. The World Health Organization (WHO) declared it an International Public Health Emergency ^[COVID-19 pandemic. (2020, August 14). Retrieved August 17, 2020, from https://en.wikipedia.org/wiki/COVID-19_pandemic] <!-- Sources were referenced using the footnote addin in the printed discussion. General information for covid-19 was collected from the internet, primarily from wikipedia. --> , and many states in the United States responded quickly, implementing regulations in hope of decreasing the spread of COVID-19, and slowing its effect on the population. Some states chose to shut down almost entirely, closing gyms, theaters, bowling alleys, restaurants, and much more. While many states were quick to issue stay-at-home orders, some states were determined to remain more open for the height of the pandemic. Seven states chose not to issue stay-at-home orders during the pandemic. These states were Arkansas, Iowa, Nebraska, North Dakota, South Dakota, Utah, and Wyoming.One of these states, South Dakota, did not even require the closure of any businesses (although in-person education at schools was closed in all 7 states.)^[States that did not issue stay-at-home orders in response to the coronavirus (COVID-19) pandemic, 2020. (n.d.). Retrieved August 16, 2020, from https://ballotpedia.org/States_that_did_not_issue_stay-at-home_orders_in_response_to_the_coronavirus_(COVID-19)_pandemic,_2020]  <!-- the timeframe of information is from December 2019, until August 16th 2020 which was the most recent data update from the source at the time of completing this project --> 

## C. Hypothesis

 <!-- The hypothesis follows the introduction and is labeled on line 29 as a level 2 header. The actual hypothesis is printed below --> 
The intention of the stay-at-home orders was to limit interactions from members of the population in hopes of avoiding contact that would spread COVID-19. Based on this idea, the states that did not issue stay-at-home orders should have higher rates of COVID-19 cases than the states that did issue a stay-at-home order. 

## D. Datasets used
 <!-- Following the hypothesis is information about the datasets that were used for this project. One data set was taken from the CDC's website (the link is in the project) and the other data set was from World Population Review, which is a website with data sets on population. The information for the population dataset was taken from 2020 Census estimates. --> 
The primary dataset used for this analysis is the "United States COVID-19 Cases and Deaths by State" compiled by the CDC and published on Data.CDC.gov^[United States COVID-19 Cases and Deaths by State. (n.d.). Retrieved August 16, 2020, from https://www.cdc.gov/covid-data-tracker/].Additionaly, the dataset "United States by Density" was collected from [World Population Review](https://worldpopulationreview.com/state-rankings/state-densities), which compiled the dataset based off US Census state population estimates.^[United States by Density 202. (n.d.). Retrieved August 16, 2020, from https://worldpopulationreview.com/state-rankings/state-densities]
 <!-- again, the datasets used are cited using footnotes--> 
 
## E. Description of analyses
 <!-- After the datasets were discussed, a level 2 header marks the description of analyses. The majority of work for this project is in this section. --> 

```{r , message = FALSE, echo = FALSE}
mapData <- read_csv("raw_data/US_MAP_DATA.csv", skip = 2) %>% 
    	filter(fips < 57, abbr != "US")
```
 <!-- using the raw data, I made smaller tables that were easy to reference with new names. I narrowed the raw data into two smaller tibbles tha I worked with for the rest of the project --> 
```{r popdata, message=FALSE,echo=FALSE}
popdata <- read_csv("raw_data/US_POP_DENS.csv")
```

```{r, message=FALSE, echo=FALSE}
totalDeathmap <- mapData %>%
	    rename(Total_Deaths = "Total Death", State = "jurisdiction") %>%
		summarise(region = str_to_lower(State), value = Total_Deaths) %>%
	write_csv("output_temp.dataset/deaths_by_state_map.csv")
```
 <!-- the chunk above this comment narrowed down one of the previous tibbles to an even more specific one which I again gave it's own name and saved it to my folder of more refined data. I then copied and pasted the above chunk below it and edited it to get deaths_per_100000 instead of total deaths. Both of these final datasets originated from the main one colleted off the cdc website  --> 
```{r , message = FALSE, echo = FALSE}
normalDeathmap <- mapData %>% 
		rename(State = "jurisdiction", Deaths_per_100000 = "Death_100k") %>%
        summarize(region = str_to_lower(State), value = Deaths_per_100000) %>%
	write_csv("output_temp.dataset/normalized_deaths_by_state_map.csv")
```

```{r, message=FALSE, echo=FALSE}
totalDeath <- mapData %>%
	    rename(Total_Deaths = "Total Death", State = "jurisdiction") %>%
		summarise(State, Total_Deaths) %>%
	write_csv("output_temp.dataset/deaths_by_state.csv")
```
 <!-- I did the same thing with the above and below chunks as stated in the comment on line 55, but these small datasets are summarized differently since they are not being used for the choropleths --> 
```{r , message = FALSE, echo = FALSE}
normalDeath <- mapData %>% 
		rename(State = "jurisdiction", Deaths_per_100000 = "Death_100k") %>%
        summarize(State, Deaths_per_100000) %>%
	write_csv("output_temp.dataset/normalized_deaths_by_state_map.csv")
```

```{r, statesvector, message=FALSE, echo=FALSE}
totalnostate <- totalDeath %>%
	filter(State == "Arkansas"| State == "Iowa"|State == "Nebraska"|State == "North Dakota" |State == "South Dakota"|State == "Utah"|State == "Wyoming")

normalnostate <- normalDeath %>%
		filter(State == "Arkansas"| State == "Iowa"|State == "Nebraska"|State == "North Dakota" |State == "South Dakota"|State == "Utah"|State == "Wyoming")
```
 <!-- the chunk starting on line 77 allowed me to create two new smaller datasets that I could layer on to a scatter plot by repeating "geom_point". That way I made the points stand out for the countries I was emphasizing. Below, they show as a different color and larger size than the other points. --> 

Seven states chose not to implement a stay-at-home order during the beginning of the COVID-19 pandemic. Under the assumption that the stay-at-home orders would reduce contact between people in a population, it could by hypothesized that the states which did implement the order would have less deaths than the states which did not. Figure 1, below, shows the total deaths per state. In this figure, the states with black dots are the state which did implement the order, while the dots in red mark the total deaths for the states which did not implement the order. On a log scale we can see that the states which did not implement the order had generally less fatalities than the states that did. 

```{r, message=FALSE, echo=FALSE, fig.cap= "**Figure 1:** Total deaths per state. States that did not implement a stay-at-home order are red."}
totalDeath %>%
	ggplot(aes(x = State, y = Total_Deaths)) +
	geom_point()+
	geom_point(data = totalnostate, aes(x = State, y = Total_Deaths), color = "red", size = 3)+
	theme_grey() +
	theme(axis.text.x = element_text(angle = 45, hjust = 1), legend.position = "none") +
	labs(title = "Total Deaths per State") +
	scale_y_log10()
```
 <!-- above is a standard scatter plot piped out of the dataset, but this includes a second "geom_point" that layers on more distinct points for the states I wanted to emphasize. This only worked for me when I piped the plot out of the dataset instead of including the dataset within the path of ggplot. --> 
 <!-- I chose to scale the above graph with log10 because the points were packed to densely to distinguish well before scaling it --> 
Total deaths in not a true indicator of effectiveness for the stay-at-home order, however, because other factors can play into the totals, such state size, population, and population density. A slightly better indicator of effectiveness of the stay-at-home order can be seen in Figure 2 below. Looking at Total Deaths per 100,000 people demonstrates fatality rates with more consideration of the population size. The black dots in the figure represent states that implemented a stay-at-home order and the red dots represent states that did not. 
 <!-- In the chunk below I used the same technique as above to point out the states I was talking about. I did not choose to scale this graph, though, because this way seemed a more accurate representation of the data--> 
```{r, message=FALSE, echo=FALSE, fig.cap= "**Figure 2:** Total deaths per 100k people per state. States that did not implement a stay-at-home order are in red"}
normalDeath %>%
ggplot(aes(x = State, y = Deaths_per_100000)) +
	geom_point() +
	geom_point(data = normalnostate, aes(x = State, y = Deaths_per_100000), color = "red", size = 3)+
	theme_grey() +
	theme(axis.text.x = element_text(angle = 45, hjust = 1), legend.position = "none") +
	labs(title = "Total Deaths per 100k People per State")
```

The following two state maps offer additional visual aids in understanding the deaths for each state. The abbreviations for the seven states that did not issue a stay-at-home order ar "AR", "IA", "NE", "ND", "SD", "UT", and "WY". These graphs show how the deaths in these seven states compare to neighboring states which did not implement the order, and share similar demographics. 
```{r , message = FALSE, echo = FALSE, fig.cap="**Figure 3:** Total deaths in each state."}
state_choropleth(totalDeathmap, title = "Total Deaths in Each State", legend = "Deaths") +
	scale_fill_brewer(palette = 2)
```
 <!-- all of the choropleths used were for states. The color palette is irrelevent in regards to the actual data but I chose to keep it the same for both choropleths that showed deaths for easier comparision, and the same for both choropleths showing population. --> 

```{r Total_death, message = FALSE, echo = FALSE, fig.cap="**Figure 4:** Deaths per 100k people in each state."}
state_choropleth(normalDeathmap, title = "Deaths per 100k in Each State", legend = "Deaths per 100k") +
	scale_fill_brewer(palette = 2) 
```

```{r , message = FALSE, echo = FALSE}
totalpop <- popdata %>%
		summarise(region = str_to_lower(State), value = Population) %>%
		write_csv("output_temp.dataset/totalpop_state.csv")
```
 <!-- I added some more chunks here to include the information needed for the population choropleths. these chunks do not produce anything directly in the html --> 
```{r , message = FALSE, echo = FALSE}
popdens <- popdata %>%
		summarise(region = str_to_lower(State), value = Density) %>%
		write_csv("output_temp.dataset/popdens_state.csv")
```
Comparing the two graphs below to the two graphs above we can see that most of the states which did not issue a stay-at-home order are also the states with lower populations and lower population densities. The states that had lower population densities are also the states that typically had lower fatality rates regardless of stay-at-home status.
```{r , message = FALSE, echo = FALSE,  fig.cap="**Figure 5:** Total population in each state."}
state_choropleth(totalpop, title = "Total Population for Each State", legend = "Population") +
	scale_fill_brewer(palette = 7)
```

 <!-- Matching palettes between the choropleth above and below allow for easier comparison of the two graphs.  --> 
```{r, message = FALSE, echo = FALSE,  fig.cap="**Figure 6:** Population density in each state."}
state_choropleth(popdens, title = "Population Density for Each State", legend = "Population per square mile") +
	scale_fill_brewer(palette = 8)
```

## F. Conclusions
 <!-- After all the data and analysis, the conclusion can be labeled with a level 2 header. The conclusion is printed below --> 
In conclusion, it would appear that states without a stay-at-home order did generally better than state with one. However, there are apparent trends in the success of states with low populations and low population densities. Additionally, the states that did not issue a stay-at-home order were also more likely to be states that had low populations and low population densities. Given the data, the null hypothesis cannot be rejected and the stay-at-home orders may or may not have been effective.

## G. Viewing this project
 <!-- the two links here ultimately link back to the repository for this project in Github, but the second link takes the route through my website that was made using github. --> 
The completed project files can be accessed online at (https://github.com/riessb12/COVID-19). The repo for this reproducible project is also publicly available at (https://riessb12.github.io/).
