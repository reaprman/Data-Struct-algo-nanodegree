"""
Read file into texts and calls.
It's ok if you don't understand how to read files

"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

callTimes = {}
key = ""
for row in calls:
    chk1 = row[0]
    chk2 = row[1]
    if chk1 not in callTimes:
        callTimes[chk1] = int(row[3])
        if key == "":
            key = chk1
        if int(row[3]) > callTimes[key]:
            key = chk1
    else:
        callTimes[chk1] = callTimes[chk1] + int(row[3])
        if callTimes[chk1] > callTimes[key]:
            key = chk1
    if chk2 not in callTimes:
        callTimes[chk2] = int(row[3])
        if int(row[3]) > callTimes[key]:
            key = chk2
    else:
        callTimes[chk2] = callTimes[chk2] + int(row[3])
        if callTimes[chk2] > callTimes[key]:
            key = chk2

print(key, "spent the longest time,", callTimes[key], "seconds, on the phone during September 2016")


"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""