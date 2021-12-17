import pandas as pd
from IPython.display import display

df = pd.read_csv('./Wildfire.csv',parse_dates=['Date Started','Date Contained'])

#create FIPS code for each county

df['Lat-Lon'] = df['Lat-Lon'].map(lambda x: x.lstrip('[').rstrip(']').strip())
df[['Lat','Lon']] = df['Lat-Lon'].str.split(",",expand=True)
df['Date Started'] = df['Date Started'].dt.strftime('%m/%d/%Y')
df['Date Contained'] = df['Date Contained'].dt.strftime('%m/%d/%Y')



print(df)

df.to_csv('california_fire.csv')