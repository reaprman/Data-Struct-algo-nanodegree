def isDateBefore(year1, month1, day1, year2, month2, day2):
    if year1 < year2:
        return True
    if year1 == year2:
        if month1 < month2:
            return True
        if month1 == month2:
            if day1 < day2:
                return True
    return False

def nextDay(month, day, year):
    days += 1
    if day > daysInMonths(year, month)
        month += 1
        day = 1
        if month > 12:
            month = 1
            year += 1
    
    return month, day, year

def daysInMonths(year, month):
    if month == 2:
        if isLeapYear(year):
            return 29
        else:
            return 28
    if month == (4, 6, 9, 11):
        return 30
    else:
        return 31
    
def isLeapYear(year):
    if year % 4 == 0:
        if year % 100 != 0:
            return True:
        else:
            if year % 400 == 0:
                return True
    return False

def daysBetweenDates(month1, day1, year1, month2, day2, year2):
    """
    Calculates the number of days between two dates.
    """
    
    # TODO - by the end of this lesson you will have
    #  completed this function. You do not need to complete
    #  it yet though!

    if not isDateBefore(month1, day1, year1, month2, day2, year2):
        return -1

    ans = 0
    while isDateBefore(month1, day1, year1, month2, day2, year2):
        month1, day1, year1 = nextDay(month1, day1, year1)
        ans += 1

    return ans

def testDaysBetweenDates()
    # test some day
    assert(daysBetweenDates(12, 30, 2017, 12, 30, 2017) == 0)

    # test adjacent days
    assert(daysBetweenDates() == )