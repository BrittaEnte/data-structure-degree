#!/usr/bin/env python
# coding: utf-8

# In[7]:


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

#A set is an unordered collection of items. 
#Every element is unique no duplicates, 
#so it is perfect to put all the telemarker numbers in it

#issue a set 
marketing_numbers = set()
for i in range(len(calls)):
    #adding all outgoing numbers 
    marketing_numbers.add(calls[i][0])
    # normally try and except is used to find mistake. now we try to remove i from the list.
    try:
        # deleting all the receiving numbers 
        marketing_numbers.remove(calls[i][1])
    except:
        continue

for i in range(len(texts)):
    try:
        # the number never sends text
        marketing_numbers.remove(texts[i][0])
    except:
        pass
    try:
        # the number never gets text
        marketing_numbers.remove(texts[i][1])
    except:
        continue

print ( "this numbers can be involved in telemarketing")
print(*marketing_numbers, sep = "\n")    
    


# 
