# Sam records when they wake up every morning. Assuming Sam always wakes up in the same hour, use bubble sort to sort by earliest to latest.

def bubble_sort_1(l):
    # TODO: implement bubble sort solution
    for i in range(len(l)):
        for j in range(0, len(l)-i-1):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
    pass
wakeup_time = [16,49,3,12,56,49,55,22,13,46,19,55,46,13,25,56,9,48,45]
bubble_sort_1(wakeup_times)
print("Pass" if(wakeup_time[0] == 3) else "Fail")

# Sam doesn't always go to sleep in the same hour. Given the following times Sam has gone to sleep, sort the times from latest to earliest

def bubble_sort_2(l):
    for i in range(len(l)):
        for j in range(len(l)-i-1):
            if l[j][0] > l[j+1][0]:
                l[j], l[j+1] = l[j+1], l[j]
            if l[j][0] == l[j+1][0]:
                if l[j][1] >v   l[j+1][1]:
                    l[j], l[j+1] = l[j+1], l[j]
                
      
# Entries are (h,m) where h is the hour and m is the minute
sleep_times = [(24,13), (21,55), (23,20), (22, 5), (24, 23), (21, 58), (24, 3)]
bubble_sort_2(sleep_times)
print("Pass" if(sleep_times == ) else "Fail")