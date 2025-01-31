import pandas as pd

df = pd.read_csv('filos.csv')

def get_filos():
    return dict(zip(df.index, df['Phylum']))

def get_filos_description():
    return dict(zip(df.index, df['descripcion']))

def find_all_filos():
    return dict(zip(df['Phylum'],df['descripcion']))

def add_filo(dic):
    new_row = pd.Series(dic)
    df.loc[len(df)] = new_row
    df.to_csv('filos.csv', index=False)
    print(df)

def edit_filo():
    pass

def delete_filo():
    pass

if __name__ == '__main__':
    print(get_filos())