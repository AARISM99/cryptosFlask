import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans

csvFilePath = "crypto_data.csv"

data = pd.read_csv(csvFilePath)

# print(data.head())

#remove na
data.dropna(inplace=True)
data.drop('Unnamed: 0', axis = 1, inplace=True) 

df = data[['TO_USDT','Price','Variation24h','Haut24h','Bas24h','Volume24h','Volume24h_USDT']]



print("\n")
print(df.head())
print("\n")

def prep(s):
    
    # removing punctuation and symbols
    #s = s.replace('.','')
    s = s.replace(',','')
    s = s.replace('€','')
    s = s.split(' ')
    # s = s.split('-')

    # return first value
    # or the mean between the two
    if len(s) == 1:
        return float(s[0])
    else: # if we have two values, compute the average
        first = float(s[0])
        second = s[1]
        second = second.replace('+','')
        second = second.replace('%','')

    return second
    #return (min_price+max_price)/2


# # preparing data
# df = df[df['Price'].str.contains('[a-zA-Z]') == False]
df['Price'] = df['Price'].map(prep)
df['Variation24h(%)'] = df['Variation24h'].map(prep)
df['Haut24h'] = df['Haut24h'].map(prep)
df['Bas24h'] = df['Bas24h'].map(prep)
df['Volume24h'] = df['Volume24h'].map(prep)
df['Volume24h_USDT'] = df['Volume24h_USDT'].map(prep)

print("\n")
print(df.head())
print("\n")

plt.scatter(df['TO_USDT'],df['Variation24h(%)'])

