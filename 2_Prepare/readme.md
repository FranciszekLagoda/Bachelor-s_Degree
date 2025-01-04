# Prepare
The second step of analysis involves finding the necessary data, identifying how it's organized, and determining its credibility. In the context of scientific research, this involves finding adequate literature and high-value data.

## Roadmap
1. Identify the essential keywords
2. Find and store adequate scientific papers
3. Collect statistic data and store it appropriately
4. Determine the credibility of the data

## 1. Identify the essential keywords
Keywords are important when searching for scientific papers in scientific databases. I have grouped keyword based on categories. 
### International Trade
* International Trade, Trade, WTO, World Trade Organization
### Polish Trade
* Polish Trade, Polish export, Polish import

### Economic crisis
* Lagging Indicators, Economic Indicators,, Financial Crisis, Causes of Crisis, GDP, Gross Domestic Product, Inflation

## 2. Find and store adequate scientific papers
Sources are stored in .bib format [here](/2_Prepare/sources/literature.bib) and all sources are described in a .md file [here](/2_Prepare/sources/literature.md).


## Collect statistic data and store it appropriately
Here I described how I have accessed data and how used databases are structured. 
### GUS database
#### The structure of the database
Data is organized into separate categories. Number of this categories is depends on the level of data processing. There are highly processed datasets with many categories and those in simple data base format. For my use I've chosen high-value dataset.

#### Preparing data
1. I downloaded to 'data_raw' folder, data from polish statistical office "baza danych o wysokiej wartości GUS" about polish export and import of goods from 2012 to 2023 using available in google chrome extension for downloading many files from one site.
2. Using [python script](/2_Prepare/scripts/data_to_database.py) I imported all data to [local data base](/2_Prepare/scripts/create_trade_raw_table.sql), created in PostgresQL and pre-cleaned them.
3. Because ot the data structure it was necessary to create o dictionary so I downloaded it from GUS's website.

### IMF database
#### The structure of the database
The database is stored in json and it can be acceded with API. To access specific data it is important to know it: 
* Dataset, a.k.a. Series - a data set containing economic indices.
* Indicator - a set of time-indexed numeric values that represent an economic index or metric.
* Dimension - metadata for all indicators in an IMF data series. For example, in IMF series, most common are:
    * Area (eg. USA)
    * Frequency (e.g., Yearly)
    * Period (e.g., from 2012 to 2023)
#### Preparing data
1. Based on example prepared by Irina Klein, I created my own function to access data that I am interested in with API
2. The result of this API is a data frame  with index name, indicator, Base Year, Unit Value, Country, Period and Value.

#### Sources
* Irina Klein - IMF Data Discovery and Collection | PyData Global 2022 | https://www.youtube.com/watch?v=sAwQgbfSbjw
* International Monetary Found - Selected Online IMF Data Sources | https://www.imf.org/external/np/ds/matrix.htm
* Irina Klein - Extraction of International Financial Statistics data from the International Moneraty Fund |2023| https://github.com/Economic-and-Financial-Data-Discovery/imfdatapy/blob/master/demo/JSON_RESTful_API_IFS_GDP_example.ipynb