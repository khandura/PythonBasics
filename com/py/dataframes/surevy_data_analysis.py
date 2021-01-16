import pandas as pd

data_file = r'D:\CODEBASE\Python\PythonBasics\data\survey_results_public.csv'


def read_file_as_dataframe():
    return pd.read_csv(data_file)


def split_message(msg):
    print(f'{"*" * 10} {msg} {"*" * 10}')


def access_data_from_dataframe():
    df = read_file_as_dataframe()
    split_message('all columns from dataframe')
    print(df.columns)

    split_message('access single column data')
    print(df['Hobbyist'])

    split_message('get the count of distinct data for a column')
    print(df['Hobbyist'].value_counts())


access_data_from_dataframe()