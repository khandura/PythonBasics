"""this script contains the basic operations demo of dataframe using pandas"""
from datetime import datetime

import pandas as pd

# pd.set_option('max_columns', 100)
# pd.set_option('max_rows', 100)
from IPython.core.display import display

data_file = r'D:\CODEBASE\Python\PythonBasics\data\survey_results_public.csv'
emp_data_file = r'D:\CODEBASE\Python\PythonBasics\data\employees.csv'
date_formatter = "%Y%m%d"


def split_message(msg):
    print(f'{"*" * 10} {msg} {"*" * 10}')


def fetch_dataset_as_dict():
    # create dictionary
    employees = {
        'name': ['Akhilesh', 'Priyanka', 'Navil', 'Ashok', 'Alex', 'Rainish'],
        'profile': ['Dev', 'Dev', 'Manager', 'Manager', 'Lead', 'Support'],
        'skill': ['Python', 'Java', 'Python', 'Java', 'Python', 'Java'],
        'salary': [50000, 80000, 120000, 180000, 130000, 75000],
        'date of joining': [datetime.strptime('20150821', date_formatter),
                            datetime.strptime('20180212', date_formatter),
                            datetime.strptime('20160415', date_formatter),
                            datetime.strptime('20100611', date_formatter),
                            datetime.strptime('20170202', date_formatter),
                            datetime.strptime('20170415', date_formatter)]
    }
    return pd.DataFrame(employees)


def read_file_to_dataframe():
    df = read_file_as_dataframe()

    # print type of dataframe
    print(type(df))

    # get number of columns and rows
    rows, cols = df.shape
    print(f'dataframe have - {cols} columns and {rows} rows')

    # get complete info about dataframe
    print(df.info())

    # set the number of rows and columns you want to display
    pd.options.display.max_columns = 5
    pd.options.display.max_rows = 5
    print(df)

    # print top 5 element or any number of rows by passing the number to head()
    # print(df.head())
    print(df.head(10))


def read_file_as_dataframe():
    return pd.read_csv(emp_data_file)


def create_df_from_dict():
    # convert dict into df
    emp_df = fetch_dataset_as_dict()
    print(f'employee dataframe :\n {emp_df}')
    print(f'employee names :\n {emp_df["name"]}')


def access_data_from_df():
    df = read_file_as_dataframe()

    # get the column names
    col_names = df.columns
    print(f'columns : {col_names}')
    print(type(col_names))


def data_access_notations():
    emp_df = fetch_dataset_as_dict()
    print(emp_df)

    # access using [] operator
    print(f'accessing column name using df["col_name"] operator')
    names = emp_df['name']
    print(names)
    doj = emp_df['date of joining']
    print(doj)
    print(f'accessing multiple columns using df[["col1", "col2"]] operator')
    emp_name_and_profile_df = emp_df[['name', 'profile']]
    print(emp_name_and_profile_df)

    # access using . operator
    print(f'accessing column name using df.col_name operator')
    names = emp_df.name
    print(names)
    # below statement will throw error as we can't access column name with space in it with . notation
    # doj = emp_df.date of joining
    # print(doj)
    # print(f'accessing multiple columns using df.col1, col2 operator')
    # emp_name_and_profile_df = pd.DataFrame(emp_df.name, emp_df.profile)
    # print(emp_name_and_profile_df)


def access_data_using_loc():
    df = fetch_dataset_as_dict()
    print(df)
    # access rows and cols using df.loc[row or [list or rows], col or [list of cols]]
    split_message('single row and col')
    emp_name_df = df.loc[0, 'name']
    print(emp_name_df)
    split_message('all rows for single col')
    all_emp_name_df = df.loc[:, 'name']
    print(all_emp_name_df)
    split_message('multiple rows nd cols')
    emp_name_and_profile_df = df.loc[[0, 1], ['name', 'profile']]
    print(emp_name_and_profile_df)


def access_data_by_index():
    df = fetch_dataset_as_dict()
    split_message('data with default index')
    print(df.loc[0])

    split_message('update the index')
    df.set_index('name', inplace=True)
    print(df)

    split_message('access data using updated index')
    print(df.loc['Akhilesh'])


def filter_dataframe_data():
    emp_df = fetch_dataset_as_dict()
    split_message('employee data')
    print(emp_df)

    split_message('filter employees who are dev')
    devs = emp_df['profile'] == 'Dev'
    print(emp_df.loc[devs])

    split_message("filter employees who's skill is Python and they earn > 70000 ")
    emp_python_skill_hig_sal = (emp_df['skill'] == 'Python') & (emp_df['salary'] > 70000)
    print(emp_df.loc[emp_python_skill_hig_sal])


# read_file_to_dataframe()
# create_df_from_dict()
# access_data_from_df()
# data_access_notations()
# access_data_using_loc()
# access_data_by_index()
filter_dataframe_data()
