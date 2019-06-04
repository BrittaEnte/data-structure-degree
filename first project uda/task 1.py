#!/usr/bin/env python
# coding: utf-8

# task 1 first project 

# In[6]:


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
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
# the input will be the all numbers. the output will be the number of unique numbers 
#of all list
# we will use a set, because a set got no duplicates. and we want each number only once.
numbers =set()

for c in calls:
    numbers.add(c[0]) # first line
    numbers.add(c[1]) # second line   

    
for t in texts:
    numbers.add(t[0]) # first line
    numbers.add(t[1]) # second line
    
print("there are {} different numbers in the records".format(len(numbers)))


# 

# #### What is a set in Python?
# A set is an unordered collection of items. Every element is unique (no duplicates) and must be immutable (which cannot be changed).
# However, the set itself is mutable. We can add or remove items from it.
# Sets can be used to perform mathematical set operations like union, intersection, symmetric difference etc.
# 
# 
