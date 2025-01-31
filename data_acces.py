import pandas as pd

df = pd.read_csv('filos.csv')

def get_filos():
    return dict(zip(df.index, df['Phylum']))

def get_filos_description():
    pass#todo el empalme que sea del indice y la descripcion, no del filo y la desc

def add_filo():
    pass

def edit_filo():
    pass

def delete_filo():
    pass

if __name__ == '__main__':
    print(get_filos())