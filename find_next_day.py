# not a leetcode problem
# D = 5, M = 7, Y = 2023
jan = 31
feb = 28
mar = 31
apr = 30
may = 31
jun = 30
july = 31
aug = 31
sep = 30
october = 31
nov = 30
dec = 31
months = {
    1: jan, 2: feb, 3: mar, 4: apr, 5: may, 6: jun,
    7: july, 8: aug, 9: sep, 10: october, 11: nov, 12: dec
}


def is_leap_year(year):
    if (year % 400 == 0) and (year % 100 == 0):
        return True
    elif (year % 4 == 0) and (year % 100 != 0):
        return True
    return False


def find_next_day(d=1, m=1, y=1):
    leap = is_leap_year(y)
    if leap:
        months[2] = 29
    if d > months[m]:
        raise KeyError()
    month_range = months[m]
    d = d + 1
    if d > month_range:
        d = 1
        m = m + 1
        if m > 12:
            m = 1
            y = y + 1
    return d, m, y


print(find_next_day())                # result:  (2, 1, 1)
print(find_next_day(5, 7, 2023))      # result: (6, 7, 2023)
print(find_next_day(31, 12, 2023))    # result: (1, 1, 2024)
print(find_next_day(30, 2, 2023))     # result: KeyError
print(find_next_day(28, 2, 1900))     # result: (1, 3, 1900)
print(find_next_day(28, 2, 2000))     # result: (29, 2, 2000)