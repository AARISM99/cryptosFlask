from asyncio import sleep
import pandas as pd
import hvplot.pandas
from path import Path
import plotly.express as px
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from datetime import datetime
import time

from csv_to_json import csv_to_json
from mongdb import insertJsonFile


# csv_file_path = "data/market_crypto_data_t.csv"
csv_prep_file_path = "data/prep_market_crypto_data_test.csv"
prep_json_file_path = "data/prep_market_crypto_data_test.json"



def is_float(element) -> bool:
    try:
        float(element)
        return True
    except ValueError:
        return False

def prep_numb(s):
    s = str(s)
    # removing punctuation and symbols
    #s = s.replace('.','')
    s = s.replace(',','')
    s = s.replace('€','')
    s = s.replace('$','')
    s = s.replace('%','')
    s = s.replace(' ','')
    # s = s.split('-')

    if any(c.isalpha() for c in s) == True:
        x = str(0.0)

    elif is_float(s) == True :
      x = float(s)
    
    else :
      x = s

    # print(x)
    return x

def prep_date(d):
    # format = "%b %d, %Y"
    # try:
    #     date = time.strptime(d,format)
    # except:
    #     date = d
    # return date
    return d

def prep_rank(r):
    if is_float(r) == True:
        x = int(r)
    else:
        x = r
    return x

def prep_percentage(d):
    try:
        x = str(d).replace('%','')
    except:
        x = str(0.00)
    return prep_numb(x)

def clustering(csv_file_path):

    # Load the crypto_data.csv dataset.
    df = pd.read_csv(csv_file_path, index_col='Unnamed: 0')
    print(df.head(20))

    # df['Rank'] = df['Rank'].map(prep_rank)
    # df['Name'] = df['Name'].map
    # df['Company']
    df['marketCap'] = df['marketCap'].map(prep_numb)
    df['fullyDilutedMarketCap'] = df['fullyDilutedMarketCap'].map(prep_numb)
    df['price'] = df['price'].map(prep_numb)
    df['price_change_24h'] = df['price_change_24h'].map(prep_numb)
    df['price_change_percentage'] = df['price_change_24h'] / df['price'] * 100
    df['price_change_percentage'] = df['price_change_percentage'].map(prep_numb)
    df['volume_24h'] = df['volume_24h'].map(prep_numb)
    df['volume24hInMarketCap'] = df['volume24hInMarketCap'].map(prep_numb)
    df['dominance'] = df['dominance'].map(prep_percentage)
    df = df.rename(columns={'dominance': 'dominance'})
    # df.drop(columns='Dominance')
    df['circulatingSupply'] = df['circulatingSupply'].map(prep_numb)
    df['maxSupplyValue'] = df['maxSupplyValue'].map(prep_numb)
    df['totalSupplyValue'] = df['totalSupplyValue'].map(prep_numb)
    df['yesterday_low'] = df['yesterday_low'].map(prep_numb)
    df['yesterday_high'] = df['yesterday_high'].map(prep_numb)
    df['yesterday_open'] = df['yesterday_open'].map(prep_numb)
    df['yesterday_close'] = df['yesterday_close'].map(prep_numb)
    df['yesterday_change'] = df['yesterday_change'].map(prep_percentage)
    df['yesterday_volume'] = df['yesterday_volume'].map(prep_numb)
    df['high_24h'] = df['high_24h'].map(prep_numb)
    df['low_24h'] = df['low_24h'].map(prep_numb)
    df['high_7d'] = df['high_7d'].map(prep_numb)
    df['low_7d'] = df['low_7d'].map(prep_numb)
    df['high_30d'] = df['high_30d'].map(prep_numb)
    df['low_30d'] = df['low_30d'].map(prep_numb)
    df['high_90d'] = df['high_90d'].map(prep_numb)
    df['low_90d'] = df['low_90d'].map(prep_numb)
    df['high_52w'] = df['high_52w'].map(prep_numb)
    df['low_52w'] = df['low_52w'].map(prep_numb)
    df['high_all_time'] = df['high_all_time'].map(prep_numb)
    df['low_all_time'] = df['low_all_time'].map(prep_numb)
    df['high_all_time_date'] = df['high_all_time_date'].map(prep_date)
    df['low_all_time_date'] = df['low_all_time_date'].map(prep_date)
    # df['date']

    df.to_csv(csv_prep_file_path)

    # print(df.head(30))

    csv_to_json(csv_prep_file_path,prep_json_file_path)

    insertJsonFile(prep_json_file_path)