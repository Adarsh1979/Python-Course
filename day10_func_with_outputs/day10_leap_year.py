def is_leap(year_p):
    if (year % 4 == 0):
        if (year % 100 == 0):
            if (year % 400 == 0):
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def days_in_month(year_p,month_p):
    month_days = [31,28,31,30,31,30,31,31,30,31,30,31]
    if is_leap(year_p) and month == 2:
        return 29
    return month_days[month_p-1]

year = int(input("Enter a year: "))
month = int(input("Enter month number: "))
print(days_in_month(year_p=year, month_p=month), "days")