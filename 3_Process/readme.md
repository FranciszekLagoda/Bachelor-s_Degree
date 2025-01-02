# Process
The third step of analysis involves cleaning and organizing data to make it ready to use and reviewing literature to extract all necessary knowledge.

## Methodology
### For data bases
1. Transform data into right type
2. Check the data errors
3. Document cleaning process
4. Choose tools to data analysis
5. Make notes about collected literature


## Polish International Trade
1. [SQL query](/3_Process/scripts/polish_trade_gus_table.sql) cleaned up data, added them to data base called "trade" and created indexes for more efficient queries.
2. I have not found any data errors. I have tried many queries using 'GROUP BY' and 'COUNT' functions, and all the data was displayed as expected.
3. I filtered database dictionary and with excel and PowerQuery created separated tables for every category in dictionary [link](/3_Process/processed_data/polish_trade_gus_dict). Then I added additional information to dictionaries using ChatGpt 4o and PowerQuery.
4. I exported dictionaries to separated csv files and loaded them to database with [SQL query](/3_Process/scripts/polish_trade_gus_dict_table.sql).