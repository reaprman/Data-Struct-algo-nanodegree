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

numList = set()

for row in texts:
    chk1 = row[0]
    chk2 = row[1]
    if chk1 not in numList:
        numList.add(chk1)
    if chk2 not in numList:
        numList.add(chk2)

for row in calls:
    chk1 = row[0]
    chk2 = row[1]
    if chk1 not in numList:
        numList.add(chk1)
    if chk2 not in numList:
        numList.add(chk2)

print("There are", len(numList), "different telephone numbers in the records.")


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
