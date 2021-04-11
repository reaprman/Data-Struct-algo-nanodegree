"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

telSet = set()
non_tel = set()

for row in calls:
    telSet.add(row[0])
    non_tel.add(row[1])

for row in texts:
    non_tel.add(row[0])
    non_tel.add(row[1])

copy_telSet = telSet.copy()
for num in copy_telSet:
    if num in non_tel:
        telSet.discard(num)

sort_tel = sorted(telSet)
print("These numbers could be telemarketers:")
for num in sort_tel:
    print(num) 

"""
TASK 4: 
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

