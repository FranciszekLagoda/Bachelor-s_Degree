def get_IMF_data(period, country, code, name, time_start, time_end, series='IFS'):
    import requests, re
    import pandas as pd
    import json
    # building the url to access the data
    base = f'http://dataservices.imf.org/REST/SDMX_JSON.svc/CompactData/{series}/'
    time = f'?startPeriod={time_start}&endPeriod={time_end}'
    url = f'{base}{period}.{country}.{code}.{time}'

    # send the request
    rq = requests.get(url)
    if rq.status_code == 200:
        try:
            response = rq.json()
            series = response['CompactData']['DataSet']['Series']
            temp_dic = series.get('Obs')

            df = pd.DataFrame.from_dict(temp_dic).rename(
                columns={
                    '@OBS_VALUE': 'Value',
                    '@OBS_STATUS': 'Status'
                }
            )

            # collect the necessary data into a pandas dataframe
            df['Country'] = series.get('@REF_AREA')
            df['Indicator'] = series.get('@INDICATOR')
            df['Base Year'] = series.get('@BASE_YEAR')
            df['Unit Value'] = '10e' + series.get('@UNIT_MULT')

            # Modify the Period extraction with the correct parsing
            df['Period'] = pd.to_datetime([f"{row.split('-')[0]}-{row.split('-')[1][1]}-01" for row in df['@TIME_PERIOD']], format='%Y-%m-%d')

            df.drop('@TIME_PERIOD', axis=1, inplace=True)
            df["Value"] = df["Value"].astype("float")  # Change 'double' to 'float'
            df['Index name'] = name
            
            # Sort values and rearrange columns
            df.sort_values(by=['Indicator', 'Country', 'Period'], axis=0, inplace=True)
            df = df[['Index name', 'Indicator', 'Base Year', 'Unit Value', 'Country', 'Period', 'Value']]

        except Exception as e:
            print(f"Error for {country} {code}: {url}. Exception: {e}")
            df = pd.DataFrame()
    else:
        print(f"Request failed with status code: {rq.status_code}")
        df = pd.DataFrame()
    
    return df


def get_IMF_code(series='IFS',search_term='gross domestic product'):
    import requests, re
    key = f'DataStructure/{series}'
    url = 'http://dataservices.imf.org/REST/SDMX_JSON.svc/'

    dimension_list = requests.get(f'{url}{key}').json()['Structure']['KeyFamilies']['KeyFamily']['Components']['Dimension']

    key = f"CodeList/{dimension_list[2]['@codelist']}"

    code_list = requests.get(f'{url}{key}').json()['Structure']['CodeLists']['CodeList']['Code']

    # create a disctionary of index codes and corresponding names
    code_dict = {}

    for code in code_list:
        if (search_term in code['Description']['#text'].lower()):
            code_dict[code['@value']] = code['Description']['#text']

    # print dictionary
    return(code_dict)
    