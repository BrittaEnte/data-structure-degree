#!/usr/bin/env python
# coding: utf-8

# task 2 first project 

# In[4]:


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

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

# input is the number called and the time spent
# output is the number and the longest time spent

#A dictionary is a collection which is unordered, changeable and indexed. 
#In Python dictionaries are written with curly brackets, and they have keys and values.

nummern = dict()
for i in range(len(calls)):
    #This method return a value for the given key. If key is not available, then returns default value None.
   
    nummern[calls[i][1]] = nummern.get(calls[i][1], 0) + int(calls[i][-1])
    nummern[calls[i][0]] = nummern.get(calls[i][0], 0) + int(calls[i][-1])    
    
    # use a sorted list. reverse true must be otherwise it would start with the smallest number.
    maxlist = sorted(nummern, reverse=True, key=lambda x: nummern[x])[0]
    
#print statement     
print(str(maxlist) + " used the longest time, " + str(nummern[maxlist]) + " seconds on the phone during September 2016.")


# 
# 
# 

# In[ ]:




