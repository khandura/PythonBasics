"""find leap year
In the Gregorian calendar, three conditions are used to identify leap years:
The year can be evenly divided by 4, is a leap year, unless:
The year can be evenly divided by 100, it is NOT a leap year, unless:
The year is also evenly divisible by 400. Then it is a leap year."""


def is_leap_year(year):
    if (year % 4 == 0 and not year % 100 == 0) or year % 400 ==0:
        return True
    return False


if __name__ == '__main__':
    year = int(input())
    if 1900 <= year <= pow(10, 5):
        print(is_leap_year(year))
