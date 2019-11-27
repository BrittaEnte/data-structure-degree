## Windows Active Directory
I wrote an active directory that can add user, groups and subgroups. then I wrote a function that can search for a user.
This function works with a recursion, which is a simply method of solving problems. the functions can be visualised as tree, where the user check all the leaves. when the match is found the function stops.
The worst-case scenario is that each group must be searched. This would be the runtime of O(n), whereas n is the number of users, groups and subgroups. Our memory complexity is determined by the number of return statements because each function call will be stored on the program stack. To generalize, a recursive function's memory complexity is O(recursion depth). As our tree depth suggests, we will have n total return statements and thus the memory complexity is O(n).


## Blockchain Problem
The task was to build a blockchain with date, datetime and previous hash. as data structure I used a linked list because Linked List is Dynamic data Structure that can grow and shrink during run time. Insertion and Deletion Operations are easier.  Furthermore, this data shall be coded with a SHA-256 hash. I built a class block and blockchain. In the blockchain I issued a new method called add blockchain, to add new data. 
time complexity: the runtime of a linked list is O(n).for the append function n represents the node of the blockchain. the function must go trough all nodes and then append the new node. 
space complexity: O(n) as Linked lists hold two main pieces of information (the value and pointer) per node. This means that the amount of data stored increases linearly with the number of nodes in the list. Therefore, the space complexity of the linked list is linear. 



## Finding Files
design:
for this problem i used again a recursive function,as we have to check every directory for the file.  For my function, I simply print the path if the suffix is a match, otherwise I check if it's a directory. If it is a directory, for each file in the directory, we recursively call the function again.

time complexity:
O(n) where n is the sum all directories, all subdirectories and all files. in worst case we don´t have the file, but the programm needs to search in all files and directories. 

space complexity:
O(n), as we have to store all files, directories and subdirectories in our memory. Our memory complexity is determined by the number of return statements because each function call will be stored on the program stack. To generalize, a recursive function's memory complexity is O(recursion depth). As our tree depth suggests, we will have n total return statements and thus the memory complexity is O(n).


## Huffman Code
This problem was extreme. I already gave up and continued with the next course topic called basic algorithm. There the topic was heap, heapify and heapsort. My first thought was, that this new knowledge maybe would help me with Huffman code. I think it is still not working. 
First, you must install a dict with the frequencies of each character. Then you must issue the tree with dict. Afterward, we issue a map, 
to connect all the frequencies with the code. For the encoding, we traverse through the map and decode all characters. For decoding, we traverse through each bit in the string and append the value. At the beginning we loop through all characters, then we loop through
heap, and then we create the tree. Therefore I would think the Big O Notation is O(n**3). the space complexity is O(3n log n), as we got heap, recursion, and a dict. but the short form is O(n log n).

## LRU Cache
The task was to install an LRU Cache. If the cache got more than 5 items, we will delete the first added item. the used data structure is a linked list, as this dynamic data structure can be used for items that will be stored and deleted. 
I wrote a get method and a set function for this class. An ordered Dictionary was used for this, as you can add and delete it conveniently. 
For the get and set function you only iterate once trough the list so the big O Notation is O(1). the space complexity is O(n). 


## Union and Intersection
the data structures of a linked list was implemented by udacity. I coded the union and intersection function. 
My union function got 2 while loops so the runtime is O(2n), but as the 2 does not count we got only O(n). the space complexity is O(3n), as we store list one, list two and then put these two lists into one last list. 
The intersection function got also 2 while loops so the runtime is the same O(n). the space complexity is again O(3n), as we got three lists to store. 
