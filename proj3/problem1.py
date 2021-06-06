def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if number <= 1:
        return number

    num_check = number//2
    return binary_search_sqroot(number, num_check)

def binary_search_sqroot(number, num_check):
    if num_check * num_check == number or (num_check*num_check < number and (num_check+1)*(num_check+1) > number):
        return num_check
    if num_check*num_check > number:
        return binary_search_sqroot(number, num_check//2)
    elif num_check*num_check < number:
        return binary_search_sqroot(number, num_check+1)

    pass

print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")
print("Pass" if (10 == sqrt(101)) else "Fail")