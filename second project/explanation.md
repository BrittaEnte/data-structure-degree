## Windows Active Directory
I wrote an active directory that can add user, groups and subgroups. then I wrote a function that can search for a user.
This function works with a recursion. why did you use that data structure? If the user was not found in one group the function tries the next group or subgroup. this is why i used recursion to solve this problem. 
The worst-case scenario is that in each group must be searched. This would be the runtime of O(n). the space complexity is O(1), because we store the complete directory one time. 


## Blockchain Problem
The task was to build a blockchain with date, datetime and previous hash. as data structure I used a linked list because Linked List is Dynamic data Structure that can grow and shrink during run time. Insertion and Deletion Operations are easier.  Furthermore, this data shall be coded with a SHA-256 hash. I built a class block and blockchain. In the blockchain I issued a new method called add blockchain, to add new data. the runtime and space complexity of the linked list is for both cases O(n). we store the linked list just one time, so O(n) and in the worst case
we must search through all the data one time, so again we got O(n).


## Finding Files
We need to search a file in a path. So, in this case, we again can use recursion. we run through every directory until we find the right file. The advantage of recursion is that we got a simple and clean solution for our problem. furthermore, the recursion function is short, which means the code will probably have fewer bugs. 
So the runtime is O(n), as in worst case we run trough every file. and the space complexity is also 0(n), as we got one storage of all files, we don´t change this storage but just search in three files. 



## Huffman Code
This problem was extreme. I already gave up and continued with the next course topic called basic algorithm. There the topic was heap, heapify and heapsort. My first thought was, that this new knowledge maybe would help me with Huffman code. I think it is still not working. 
First, you must install a dict with the frequencies of each character. Then you must issue the tree with dict. Afterwards, we issue a map, 
to connect all the frequencies with the code. For the encoding, we traverse trough the map and decode all characters. For decoding, we traverse through each bit in the string and append the value. At the beginning we loop through all characters, then we loop through
heap, and then we create the tree. Therefore I would think the Big O Notation is O(n**3). the space complexity is O(3n log n), as we got heap, recursion and a dict. but the short form is O(n log n).

## LRU Cache
The task was to install an LRU Cache. If the cache got more than 5 items, we will delete the first added item. the used data structure is a linked list, as this dynamic data structure can be used for items that will be stored and deleted. 
I wrote a get method and a set function for this class. An ordered Dictionary was used for this, as you can add and delete it conveniently. 
For the get and set function you only iterate once trough the list so the big O Notation is O(1). the space complexity is O(n). 


## Union and Intersection
the data structures of a linked list was implemented by udacity. I coded the union and intersection function. 
My union function got 2 while loops so the runtime is O(2n), but as the 2 does not count we got only O(n). the space complexity is O(3n), as we store list one, list two and then put this two lists into one last list. 
The intersection function got also 2 while loops so the runtime is the same O(n). the space complexity is again O(3n), as we got three lists to store. 

