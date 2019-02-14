
import numpy as np 
import pandas as pd 

#df = pd.read_csv('ign.csv',delimiter = ',')
#df = pd.read_csv('pandas_tutorial_read.csv',delimiter = ';')
df = pd.read_csv('pandas_tutorial_read.csv', delimiter=';', names = ['my_datetime', 'event', 'country', 'user_id', 'source', 'topic'])
print(df)
print(df.head())
print("==================head is the top 5 =======================================")
print(df.tail())

print("===================tail is the last 5 ==================================")


print(df.sample(8))

print(df[['country', 'user_id']])

#from adwords 
print(df[df.source == 'AdWords'])


df.to_csv('new_data.csv', sep='\t')