def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers. can use counting sort to complete in single pass.
    I will use QuickSort to complete this problem and redo with count sort later.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if ints == None or ints == []:
        return -1

    min, max = ints[0], ints[0]
    
    for num in ints:
        if num < min:
            min = num
        if num > max:
            max = num
    
    return (min, max)

## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)
j = [i for i in range(0, 100000)]  # a list containing 0 - 9
random.shuffle(j)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail") #Pass
print ("Pass" if ((0, 99999) == get_min_max(j)) else "Fail") #Pass
print ("Pass" if (-1 == get_min_max([])) else "Fail") #Pass
print ("Pass" if ((1, 66) == get_min_max([2,4,6,8,10,44,66,32,1])) else "Fail") #Pass
print ("Pass" if ((0, 99) == get_min_max(j)) else "Fail") #Fail