def recursive_binary_search(target, source, left=0):
    if len(source) == 0:
        return None
    center = (len(source)-1) // 2
    if source[center] == target:
        return center + left
    elif source[center] > target:
        # left passes original index when source array split, what happens if target 6 and source 1-10
        return recursive_binary_search(target, source[:center], left)
    else: #source[center] < target:
        #if just center for second value passed, then also just center+left for third value, what happens if target 9 and source 1-10
        return recursive_binary_search(target, source[center+1:], center+left+1)
    
    return None
 
 def find_first(target, source):
    first_idx = recursive_binary_search(target, source)
    if first_idx == None:
        return None

    while source[first_idx-1] == target:
        first_idx -= 1
    return first_idx

def contains(target, source):
    idx = recursive_binary_search(target, source)
    if idx != None and source[idx] == target: #srouce[idx] == target check may be unneccassary
        return True
    return False

multiple = [1,3,5,7,7,8,11,12]
print(recursive_binary_search(7,multiple)) #answer should be 4

multiple = [1,3,5,7,7,8,11,12,13,14,15]
print(find_first(7, multiple)) #should return 3
print(find_first(9, multiple)) #should return None

letters = ['a', 'c', 'd', 'f', 'g']
print(contains('a', letters)) #True
print(contains('b', letters)) #false
