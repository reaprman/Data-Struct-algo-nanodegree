def mergesort(items):
    if len(items) < 2: # <= 1
        return items

    mid = len(items)//2

    left = items[:mid]
    right = items[mid:]

    left = mergesort(left)
    right = mergesort(right)

    return merge(left, right)

def merge(left, right):

    merge = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merge.append(left[left_index])
            left_index += 1
        else:
            merge.append(right[right_index])
            right_index += 1
    
    # merged += left[left_index:]
    # merged += right[right_index:]

    if left_index < len(left):
        merged.extend(left[left_index]:)
    elif right_index < len(right):
        merged.extend(right[right_index:])
    
    return merged
    

merged = merge([1,4,6], [2,3,8]) # 1,2,3,4,6,8
print(merged)

test_list_1 = [8, 3, 1, 7, 0, 10, 2]
test_list_2 = [1,0]
test_list_3 = [97, 98, 99]

print('{} to {}'.format(test_list_1, mergesort(test_list_1)))
print(test_list_2, "to", mergesort(test_list_2))
print(f'{test_list_3} to {mergesort(test_list_3)}')
