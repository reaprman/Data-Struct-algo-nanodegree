def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    merged = []
    rindex, lindex = 0, 0

    while lindex < len(left) and rindex < len(right):
        if left[lindex] > right[rindex]:
            merged.append(left[lindex])
            lindex += 1
        else:
            merged.append(right[rindex])
            rindex += 1
    
    merged += left[lindex:]
    merged += right[rindex:]

    return merged

def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    ans = [0,0]

    input_list = mergeSort(input_list)

    for index in range(len(input_list)):
        if index % 2 == 0:
            ans[0] = (ans[0]*10) + input_list[index]
        else:
            ans[1] = (ans[1]*10) + input_list[index]

    return ans

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_function([[1, 2, 3, 4, 5], [542, 31]]) #Pass
test_case = [[4, 6, 2, 5, 9, 8], [964, 852]]

# need additional test cases
test_function(test_case) #Pass
test_function([[], [0, 0]]) #Pass
test_function([[], []]) #Pass
test_function([[], [31, 2]]) #Fail



