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

# get all calls from the file
for call in calls:
    marketing_numbers.add(call[0])
       
# get all calls that are outgoing and delete them from that list. we use discard
# discard will only delete it from the set, if it exists.
for call in calls:
    marketing_numbers.discard(call[1])
    
# now we must remove all numbers that get textmessage or send them
for text in texts:
    marketing_numbers.discard(text[0])
    marketing_numbers.discard(text[1]) 
    
 
new_marketing_numbers = sorted(marketing_numbers)
print ( "this numbers can be involved in telemarketing")
print(*new_marketing_numbers, sep = "\n")    
    

