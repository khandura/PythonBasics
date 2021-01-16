import pandas as pd
import numpy as np

pd.set_option('max_columns', 100)
pd.set_option('max_rows', 100)


def split_message(msg, data):
    print(f'{"*" * 10} {msg} {"*" * 10}')
    print(str(data))


def fetch_dataset_as_dict():
    # create dictionary
    employees = {
        'name': ['Akhilesh', 'Priyanka', 'Navil', 'Ashok', 'Alex', 'Rainish'],
        'profile': ['Dev', 'Dev', 'Manager', 'Manager', 'Lead', 'Support'],
        'skill': ['Python', 'Java', 'Python', 'Java', 'Python', 'Java'],
        'salary': [50000, 80000, 120000, 180000, 130000, 75000],
    }
    return pd.DataFrame(employees)


def update_salary_of_devs():
    emp_df = fetch_dataset_as_dict()
    emp_df['points'] = 50
    split_message('employee dataframe', emp_df)
    # sum_sal_by_profile = emp_df.groupby('profile').sum().reset_index()
    # split_message('sum_sal_by_profile', sum_sal_by_profile)
    # emp_df['sal_sum'] = sum_sal_by_profile[ sum_sal_by_profile['profile'].isin(emp_df['profile']) ]

    emp_df['sal_sum'] = emp_df.groupby('profile').get_group('Dev').sum()['points']

    # print(emp_df.loc[:, 'profile'])

    # print('*******sum of slaries by profile******** \n',sum_sal_by_profile.loc[emp_df[:,'profile']])
    # emp_df.loc[emp_df['profile'] == 'Dev', ['points']] = emp_df['points'] + sum_sal_by_profile.get_group(emp_df['profile'])

    split_message('developers dataframe', emp_df)

    emp_df.loc[emp_df['profile'] == 'Dev', ['points']] = emp_df['sal_sum'] + emp_df['points']

    split_message('developers dataframe', emp_df)


def frp_prod():
    emp_df = fetch_dataset_as_dict()
    emp_df['points'] = 50
    split_message('employee dataframe', emp_df)

    points_ = emp_df.groupby('profile').sum().reset_index()[['profile', 'points']]
    print(points_)

    for name, group in emp_df.groupby('profile'):
        emp_df['points'] = np.where(emp_df['profile'] == name, group.sum()['points'], emp_df['points'])

    split_message('developers dataframe', emp_df)


def access_rows():
    emp_df = fetch_dataset_as_dict()
    split_message('employee dataframe', emp_df)
    split_message('first row', emp_df.iloc[0])
    emp_df['incentives'] = 1000
    emp_df['incentives1'] = 1000
    emp_df['incentives2'] = 1000
    print(emp_df)
    emp_df['Total'] = emp_df.iloc[:, 3:6].sum(axis=1)
    print(emp_df)


def group_by_demo():
    emp_df = fetch_dataset_as_dict()
    split_message('employee dataframe', emp_df)
    # gp_df = emp_df.groupby('profile').sum()
    # split_message('employee group by profile', gp_df)
    # print(gp_df.info())
    # print(f'sum of salary for dev', emp_df.groupby('profile').groups)

    gp_df = emp_df.groupby('profile')
    split_message('employee group by profile', gp_df)
    print(gp_df.groups)
    print(gp_df.get_group('Dev').sum())

    emp_df.groupby('profile').get_group('Dev').sum()


def gp_merge():
    emp_df = fetch_dataset_as_dict()
    emp_df['points'] = 50
    split_message('employee dataframe', emp_df)
    emp_df['sal_sum'] = emp_df.groupby('profile')['salary'].transform('sum')
    split_message('employee dataframe', emp_df)
    emp_df['points'] = np.where(emp_df['profile'].isin(['Dev', 'Manager']), emp_df['sal_sum'] / emp_df['salary'], emp_df['points'])
    # split_message('employee dataframe', emp_df)
    print(emp_df.loc[:-2, :])


# access_rows()
# update_salary_of_devs()
# group_by_demo()
# frp_prod()
gp_merge()