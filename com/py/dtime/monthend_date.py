import dateutil.parser as date_parser
from pandas.tseries.offsets import BMonthEnd


def fetch_monthend_date():
    given_date = '2020-05-30'
    parsed_date = date_parser.parse(given_date)
    print(f'given date : {given_date}')
    print(f'parsed date : {parsed_date}')

    monthend_date = parsed_date - BMonthEnd(1)
    print(f'existing month end date : {monthend_date}')

    monthend_date = parsed_date + BMonthEnd(1)
    print(f'plus month end date : {monthend_date}')

    # monthend_date = parsed_date + BMonthEnd() - BMonthEnd()
    # print(f'updated month end date : {monthend_date}')

    monthend_date = parsed_date + BMonthEnd(1)

    if monthend_date.month > parsed_date.month:
        monthend_date = monthend_date - BMonthEnd()
        print(f'updated month end date : {monthend_date}')
    else:
        print(f'updated month end date : {monthend_date}')


def fetch_business_monthend_date():
    given_dates = ['2020-05-30', '2020-02-01', '2020-10-31', '2020-12-31', '2020-01-01']

    for given_date in given_dates:
        parsed_date = date_parser.parse(given_date)
        print(f'given date : {given_date}')

        b_month_end_ = parsed_date + BMonthEnd(1)
        monthend_date = b_month_end_ - BMonthEnd(1) if (
                b_month_end_.month > parsed_date.month or b_month_end_.year > parsed_date.year) else b_month_end_

        print(f'business month end date : {monthend_date}')


fetch_business_monthend_date()
# fetch_monthend_date()
