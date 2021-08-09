""" 
Binary search practice
Let's get some practice doing binary search on an array of integers. We'll solve the problem two different ways—both iteratively and resursively.

Here is a reminder of how the algorithm works:

Find the center of the list (try setting an upper and lower bound to find the center)
Check to see if the element at the center is your target.
If it is, return the index.
If not, is the target greater or less than that element?
If greater, move the lower bound to just above the current center
If less, move the upper bound to just below the current center
Repeat steps 1-6 until you find the target or until the bounds are the same or cross (the upper bound is less than the lower bound).
Problem statement:
Given a sorted array of integers, and a target value, find the index of the target value in the array. If the target value is not present in the array, return -1.
come up with both an iterative and recursive solution
 """

def binary_search(array, target):
    '''Write a function that implements the binary search algorithm using iteration
   
    args:
      array: a sorted array of items of the same type
      target: the element you're searching for
   
    returns:
      int: the index of the target, if found, in the source
      -1: if the target is not found
    '''

    start, end = 0, len(array)-1
    
    while start < end:
        mid = (start+end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            start = mid+1
        else: #elif array[mid] > target:
            end = mid-1
    
    return -1

def test_function(test_case):
    answer = binary_search(test_case[0], test_case[1])
    if answer == test_case[2]:
        print("Pass")
    else:
        print("Fail")

array = [0,1,2,3,4,5,6,7,8,9,10]
target = 6
index = 6
test_case = [array, target, index]
test_function(test_case)

def binary_search_recursive(array, target, start, end):
    '''Write a function that implements the binary search algorithm using recursion
    
    args:
      array: a sorted array of items of the same type
      target: the element you're searching for
         
    returns:
      int: the index of the target, if found, in the source
      -1: if the target is not found
    '''
    if start > end:
        return -1
    
    mid = (start+end) // 2

    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search_recursive(array,target, start, mid-1)
    elif array[mid] < target:
        return binary_search_recursive(array, target, mid+1, end)
    
    return binary_search_recursive_soln(array, target, 0, len(array)-1)
    

def binary_search_recursive_soln(array, target, start_idx, end_idx):
    if start_idx > end_idx:
        return -1
    
    mid_idx = (start_idx+end_idx)//2
    mid_element = array[mid]
    
    if mid_element == target:
        return mid_idx
    elif mid_element < target:
        return binary_search_recursive_soln(array, target, mid_idx+1, end)
    else: #elif mid_element > target
        return binary_search_recursive_soln(array, target, start, mid_idx-1)

def test_function(test_case):
    answer = binary_search_recursive(test_case[0], test_case[1], 0, len(test_case[0])-1)
    if answer == test_case[2]:
        print("Pass")
    else:
        print("Fail")

array = [0,1,2,3,4,5,6,7,8,9,10]
target = 4
index = 4
test_case = [array, target, index]
test_function(test_case)