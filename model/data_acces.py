import pandas as pd
import os 

df = pd.read_csv('/workspaces/expert-systems/model/filos.csv')

def get_filos():
    return dict(zip(df.index, df['Phylum']))

print(get_filos())