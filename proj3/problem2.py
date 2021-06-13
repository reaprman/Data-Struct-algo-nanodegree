def pivot_point(num_array, left=0):
    """ 
    Function to find index to split array for binary search ...i.e where smallest and biggest element meet
    """
    mid = len(num_array)//2
    if num_array[mid] < num_array[mid-1] or num_array[mid] > num_array[mid+1]:
        return mid + left
    
    if num_array[mid] < num_array[0]:
        return pivot_point(num_array[:mid])
    elif num_array[mid] > num_array[0]:
        return pivot_point(num_array[mid:], mid+left)

    return -1

def binary_search(num_array, target, left=0):
    mid = len(num_array)//2

    if num_array[mid] != target and len(num_array) <=1:
        return -1
    if num_array[mid] == target:
        return mid + left
    if num_array[mid] > target:
        return binary_search(num_array[:mid], target, left)
    elif num_array[mid] < target:
        return binary_search(num_array[mid:], target, mid+left)
    

def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    if len(input_list) < 1:
        return -1
    pivot = pivot_point(input_list)

    if input_list[pivot] == number:
        return pivot

    if pivot == -1:
        return binary_search(input_list, number)
    
    if input_list[pivot] > number and input_list[0] > number:
        return binary_search(input_list[pivot:], number, pivot)
    elif input_list[pivot] > number and input_list[0] <= number:
        return binary_search(input_list[:pivot], number)
    elif input_list[pivot] < number and input_list[len(input_list)-1] < number:
        return binary_search(input_list[:pivot], number)
    elif input_list[pivot] < number and input_list[len(input_list)-1] > number:
        return pivot + binary_search(input_list[pivot:], number,)


    pass


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6]) #Pass
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1]) #Pass
test_function([[6, 7, 8, 1, 2, 3, 4], 8]) #Pass
test_function([[6, 7, 8, 1, 2, 3, 4], 1]) #Pass
test_function([[6, 7, 8, 1, 2, 3, 4], 10]) #Pass
test_function([[7, 8, 1, 2, 3, 4, 5, 6], 8]) #Pass
test_function([[7, 8, 1, 2, 3, 4, 5, 6], 10]) #Pass
test_function([[7, 8, 1, 2, 3, 4, 5, 6], 8]) #Pass
test_function([[8, 1, 2, 3, 4, 5, 6, 7], 10]) #Pass
test_function([[7, 8, 1, 2, 3, 4, 5, 6], 5]) #Pass
test_function([[2, 3, 4, 5, 6, 7, 8, 1], 8]) #Pass
test_function([[3, 4, 5, 6, 7, 8, 1, 2], 1]) #Pass
test_function([[8,10,12,14,2,4,6], 10]) #Pass
test_function([[1,1,1,1,1,1,1], 10]) #Pass
test_function([[], -1]) #Pass
