from datetime import datetime


def create_date_from_string():
    str_date = '20200228'
    date_formatter = '%Y%m%d'

    date_string = "01-31-2020 14:45:37"
    format_string = "%m-%d-%Y %H:%M:%S"

    dt = datetime.strptime(str_date, date_formatter)
    print(dt)
    # dt = datetime.strptime(date_string, format_string)
    # print(dt)


create_date_from_string()
