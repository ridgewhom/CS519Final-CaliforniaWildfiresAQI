import pandas as pd
from IPython.display import display

df = pd.read_csv('./daily_aqi_by_county_2020.csv',parse_dates=["Date"])

df = df.loc[df['State Name'] == 'California']

#create FIPS code for each county

df['FIPS'] = df['State Code'].astype(str).str.zfill(2) + df['County Code'].astype(str).str.zfill(3)

df['Date'] = df['Date'].dt.strftime('%m/%d/%Y')
print(df)

df.to_csv('california_AQI.csv')