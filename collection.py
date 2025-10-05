import numpy as np 
import pandas as pd 


def load_data(path = r'C:\ProductionReady_MLModel\rent_apartments.csv'):
    return pd.read_csv(path)

''' 
# test: 
data = load_data()
print(data)
'''

