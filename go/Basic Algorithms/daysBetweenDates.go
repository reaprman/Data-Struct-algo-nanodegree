package main
import "fmt"

func isDateBefore(month1, day1, year1, month2, day2, year2 int) bool {
	if year1 < year2 {
		return true
	}
	if year1 == year2 {
		if month1 < month2 {
			return true
		} else if month1 == month2 {
			if day1 < day2 {
				return true
			}
		}
	}
	return false
}

func nextDay(month, day, year int) (int,int,int){
	day += 1
	if day > daysInMonth(month){
		day = 1
		month += 1
		if month > 12{
			month = 1
			year += 1
		}
	}
	return month, day, year
}

func isLeapYear(year){
	if year % 4 == 0{
		if year % 100 == 0{
			if year % 400 == 0{
				return true
			}else{
				return false
			}
		}
		return true
	}
	return false
}

func daysInMonth(month, year int) int{
	if month == 2{
		if isLeapYear(year){
			return 29
		}else{
			return 28
		}
	}
	if month ==  (4,6,9,11) {
		return 30
	}
	return 31
}

func daysBetweenDates(month1, day1, year1, month2, day2, year2){
	ans = 0
	if isDateBefore(month1, day1, year1, month2, day2, year2){
		return -1 //return false
	}
	for isDateBefore(month1, day1, year1, month2, day2, year2){
		month1, day1, year1 = nextDay(month1, day1, year1)
		ans += 1
	}
	return ans
}

func main(){
	# test some day
    assert(daysBetweenDates(12, 30, 2017, 12, 30, 2017) == 0)

    # test adjacent days
    assert(daysBetweenDates() == )
}
