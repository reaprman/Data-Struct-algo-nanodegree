def count_inversions(arr):
    merged, cnt = inversion_count(arr)
    return cnt

def inversion_count(items):
    if len(items) < 2:
        return items, 0
    
    mid = len(items)//2
    left = items[:mid]
    right = items[mid:]

    left, left_cnt = inversion_count(left)
    right, right_cnt = inversion_count(right)

    cnt = left_cnt + right_cnt

    merged, inv_cnt = merge(left, right)
    cnt += inv_cnt

    return merged, cnt

def merge(left, right):
    merged = []
    left_idx, right_idx = 0,0
    cnt = 0

    while left_idx < len(left):
        lvalue = left[left_idx]
        rvalue = right[right_idx]

        if lvalue > rvalue:     #its an inversion
            cnt += 1
        right_idx += 1

        if right_idx >= len(right):
            left_idx += 1
            right_idx = 0
            merged.append(lvalue)
    
    #merged.extend(right
    merged += right

    return merged, cnt

def test_function(test_case):
    arr = test_case[0]
    solution = test_case[1]
    if count_inversions(arr) == solution:
        print("Pass")
    else:
        print("Fail")

arr = [2, 5, 1, 3, 4]
solution = 4
test_case = [arr, solution]
test_function(test_case)

arr = [54, 99, 49, 22, 37, 18, 22, 90, 86, 33]
solution = 26
test_case = [arr, solution]
test_function(test_case)

arr = [1, 2, 4, 2, 3, 11, 22, 99, 108, 389]
solution = 2
test_case = [arr, solution]
test_function(test_case)



