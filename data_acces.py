import pandas as pd

def load_dataframe():
    return pd.read_csv('filos.csv')

def get_filos():
    df = load_dataframe()
    filter_df = df.iloc[:, :2]
    return filter_df.to_dict(orient='index')


def add_filo(dic):
    df = load_dataframe()
    print(df)
    new_row = pd.Series(dic)
    df.loc[len(df)] = new_row
    df.to_csv('filos.csv', index=False)
    print(df)


'''def edit_filo():
    pass'''


def delete_filo(index):
    df = load_dataframe()
    print(df)
    df2 = df.drop(index)
    df2.to_csv('filos.csv', index=False)
    print(df2)

if __name__ == '__main__':
    print(get_filos())
