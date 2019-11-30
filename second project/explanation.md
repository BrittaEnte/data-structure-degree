## Windows Active Directory
I wrote an active directory that can add user, groups, and subgroups. then I wrote a function that can search for a user.
This function works with a recursion, which is a simple method of solving problems. the functions can be visualized as a tree, where the user checks all the leaves. when the match is found the function stops.
The worst-case scenario is that each group must be searched. This would be the runtime of O(n), whereas n is the number of users, groups, and subgroups. Our memory complexity is determined by the number of return statements because each function call will be stored on the program stack. To generalize, a recursive function's memory complexity is O(recursion depth). As our tree depth suggests, we will have n total return statements and thus the memory complexity is O(n).


## Blockchain Problem
The task was to build a blockchain with date, datetime and previous hash. as data structure I used a linked list because Linked List is Dynamic data Structure that can grow and shrink during run time. Insertion and Deletion Operations are easier.  Furthermore, this data shall be coded with a SHA-256 hash. I built a class block and blockchain. In the blockchain I issued a new method called add blockchain, to add new data. 
time complexity: the runtime of a linked list is O(n).for the append function n represents the node of the blockchain. the function must go trough all nodes and then append the new node. 
space complexity: O(n) as Linked lists hold two main pieces of information (the value and pointer) per node. This means that the amount of data stored increases linearly with the number of nodes in the list. Therefore, the space complexity of the linked list is linear. 



## Finding Files
design:
for this problem, i used again a recursive function, as we have to check every directory for the file.  For my function, I simply print the path if the suffix is a match, otherwise, I check if it's a directory. If it is a directory, for each file in the directory, we recursively call the function again.

time complexity:
O(n) where n is the sum all directories, all subdirectories, and all files. in the worst case, we don´t have the file, but the program needs to search in all files and directories. 

space complexity:
O(n), as we have to store all files, directories and subdirectories in our memory. Our memory complexity is determined by the number of return statements because each function call will be stored on the program stack. To generalize, a recursive function's memory complexity is O(recursion depth). As our tree depth suggests, we will have n total return statements and thus the memory complexity is O(n).


## Huffman Code
This problem was extreme. I already gave up and continued with the next course topic called basic algorithm. There the topic was heap, heapify and heapsort. My first thought was, that this new knowledge maybe would help me with Huffman code. 

design:
I used a dictionary as datastructure to store the letters and how often they occur. the dictionary has the advantage that you can store the key and its value. means the letter and the figure of occurrence. to install the tree I used a heap because with a heap you can find the greatest and minimum number of occurrence of the code. furthermore, you can use it as a priority queue. and in our case, the letters that appear more often shall be mentioned early in the heap to keep the code short. then I issued a map of the heap to add a 0 or 1 to our tree. afterward, i encoded the tree, as the code went overall characters of my sentence. the program catch the binary value from the map. and afterward, we put all values together. the last function is to encode the message. so we do it the other way around. we check every bit and look at what letter is behind it. then we append this letter to the decoded message. 

time complexity for encoding:
resources: https://www.geeksforgeeks.org/complexity-different-operations-binary-tree-binary-search-tree-avl-tree/
the function has to loop over each character of our message. O(n)
then we loop over all different frequencies to install our heap. O(n) 
and then we loop over all the items of the map to get the binary code. O(n)
so the total must be O(n **3), but the short form is O(n). 

space complexity for encoding:
the dictionary got O(n log n)
the heap got O(n log n)
the map got also 0(n log n)
total of O(3n log n), but we write 0( n log n)

time complexity for decoding: 
we loop over each bit in the encoded message that gives us O(n)

space complexity for decoding: 
all the data must be stored in one list. each letter will be added to another so we got O(n log n)



## LRU Cache
The task was to install an LRU Cache. If the cache got more than 5 items, we will delete the first added item. the used data structure is a linked list, as this dynamic data structure can be used for items that will be stored and deleted. 
I wrote a get method and a set function for this class. An ordered Dictionary was used for this, as you can add and delete it conveniently. 

big o notation for the set function:
time complexity: set function you only iterate once trough the list so the  big O Notation is O(1)
space complexity: as the list capacity got only 5 items the space needed will never change. so we got O(1)


big o notation for the get function:
time complexity: with the if clause we loop through the entire dict. so we got O(n)
space complexity: as the list capacity got only 5 items the space needed will never change. so we got O(1)




## Union and Intersection
the data structures of a linked list was implemented by udacity. I coded the union and intersection function. 

big O Notation for the union function:
My union function got 2 while loops so the runtime is O(2n), but as the 2 does not count we got only O(n). 
According to Python wiki: Time complexity, set is implemented as a hash table. So you can expect to lookup/insert/delete in O(1) average. so we got O(n) and O(1), which gives us a total  O(n). 
the space complexity is O(n), as we store list one. 

big O Notation for the intersection function:
According to Python wiki: Time complexity, set is implemented as a hash table. So you can expect to lookup/insert/delete in O(1) average.
The intersection function got also 2 while loops so the runtime is the same O(n).
the space complexity is again O(n), as we got one list to store. 