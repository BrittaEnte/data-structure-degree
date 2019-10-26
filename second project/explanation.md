## Windows Active Directory
I wrote an active directory that can add user, groups and subgroups. then i wrote a function that can search for a user.
This function works with a recursion. If the user was not found in one group the function tries the next group or subgroup.
The worst case scenario is that in each group must be searched. This would be runtime of O(n).


## Blockchain Problem
The task was to build a blockchain with date, datetime and previous hash. so this is like a linked list. Furthermore this data shall be 
coded with a SHA-256 hash. I built a class block and blockchain. In the blockchain i issued a new method called add blockchain, to add 
new data. As in a linked list you traverse a list with runtime O(1). We just go one time trough the entire list. 


## Finding Files
We need to search a file in a path. So in this case we again can use a recursion. we run trough every directory until we find the 
right file. So the runtime is O(n).

## Huffmann Code
This problem was extrem. I already gave up and continued with the next course topic called basic algorithm. There the topic was heap, heapify 
and heapsort. My first thought was, that this new knowlegde maybe would help me with huffmann code. I think it is still not working. 
First you must install a dict with the frequencies of each character. Then you must issue the tree with dict. Afterwards we issue a map, 
to connect all the frequencies with the code. For the encoding we traverse trough the map and decode all characters. For decoding we 
traverse through each bit in the string and append the value. At the beginning we loop through all characters, then we loop through
heap, and then we create the tree. Therefore I would think the Big O Notation is O(n**3).

## LRU Cache
The task was to install a LRU Cache. If the cache got more than 5 items, we will delete the first added item. I wrote a get method
and a set function for this class. An ordered Dictorary was used for this, as you can add and delete in a convenient way. 
For the get and set function you only iterate once trough the list so the big O Notation is O(1)

## Union and Intersection
My union function got 2 while loops so the runtime is O(2n), but as the 2 does not count we got only O(n). The intersection 
function got also 2 while loops so the runtime is the same. 
