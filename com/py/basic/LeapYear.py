# this program will test the if-else functionality

def if_else_basic(yr):
    if yr % 4 == 0:
        print("LEAP year born")
    else:
        print("not leap year born")


def if_else_nested(yr):
    if yr == 0:
        print("year should be greater than zero")
    elif yr > 0:
        if yr % 4 == 0:
            print("LEAP year born")
        else:
            print("not leap year born")
    else:
        print("invalid year")


year = int(input("Enter your birth year : "))

print("check through basic if-else check")
if_else_basic(year)

print("check through basic if-else nested check")
if_else_nested(year)
