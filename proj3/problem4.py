def sort_012(input_list=[]):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.
    brute force: create three arrays and loop through original placing values were they need to go. add the arrays together

    Args:
       input_list(list): List to be sorted
    """
    zero_idx, start = 0, 0
    two_idx = len(input_list)-1
    while start <= two_idx:
        temp = input_list[start]
        if input_list[start] > 2:
            return -1
        if input_list[start] == 0:
            input_list[start] = input_list[zero_idx]
            input_list[zero_idx] = temp
            zero_idx += 1
            start += 1

        elif input_list[start] == 2:
            input_list[start] = input_list[two_idx]
            input_list[two_idx] = temp
            two_idx -= 1
        elif input_list[start] == 1:
            start += 1
    return input_list
    
def test_function(test_case):
    sorted_array = sort_012(test_case)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2]) #Pass
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1]) #Pass
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]) #Pass
test_function([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) #Pass
test_function([]) #Pass
test_function([4,4,4,4,5,5,5,6,4,4,6]) #Fail