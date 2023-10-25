
def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


year = int(input("Year to check if is leap year : "))
is_leap_year = is_leap_year(year)


if is_leap_year:
    print("leap year")
else:
    print("not a leap year")


