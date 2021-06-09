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
   