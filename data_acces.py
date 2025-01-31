import pandas as pd

df = pd.read_csv('model/filos.csv')

def get_filos():
    return dict(zip(df.index, df['Phylum']))

if __name__ == '__main__':
    print(get_filos())