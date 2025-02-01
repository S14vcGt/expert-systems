import pandas as pd

df = pd.read_csv('filos.csv')


def get_filos():
    filter_df = df.iloc[:, :2]
    return filter_df.to_dict(orient='index')


def add_filo(dic):
    new_row = pd.Series(dic)
    df.loc[len(df)] = new_row
    df.to_csv('filos.csv', index=False)
    print(df)


'''def edit_filo():
    pass'''


def delete_filo(index):
    df2 = df.drop(index)
    df2.to_csv('filos.csv', index=False)
    print(df)


if __name__ == '__main__':
    print(get_filos())
