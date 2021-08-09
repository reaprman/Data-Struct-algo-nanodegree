def bubble_sort(l):
    # TODO: implement bubble sort solution
    for i in range(len(l)):
        for j in range(0, len(l)-i-1):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
    pass
wakeup_time = [16,49,3,12,56,49,55,22,13,46,19,55,46,13,25,56,9,48,45]
bubble_sort(wakeup_times)
print("Pass" if(wakeup_time[0] == 3) else "Fail")
