## Find the square root
for this problem I used a binary search. If the mid of this binary search is the square root we will return it. If not we got two cases, the square root is less or more than the mid. This is the same procedure as in a binary search. the runtime of this search is in average O(log n),because we can separate the list into smaller pieces.n is the length of the list.the space complexity is O(1) as we have a list, that is stored one time. 


## Dutch nationa flag problem
For this problem I used the list method called insert. The advantage is that this method got two parameters. the first parameter is the index followed by item. We just need make sure that the index of the figure null is also null. so that all zero will be inserted at the beginning of the list. The figure 2 will be appended at the end of the list with the right index. the runtime of this easy function is O(n), since we iterate just one trough the list one time.the for loop runs one time, so big o notation is O(n).  n is the length of the list. the space complexity is 0(1), because we store the list just once and then we will work in this list. 

## Max and min in an unsorted array
For this solution it is checked if the figure is more than the maximum or less than the minimum. If yes, the number is set as maximum vice versa minimum. The function only loops one time trough the given list so the runtime is O(n). n is the length of the array. the space complexity is O(1), as we store the list one time and then work with this list. 

## Rearrange array elements
For this problem is used mergesort, because i used already binary search. Furthermore the runtime for mergesort is only  O(nlog(n)),as requested. n is the length the array.
After the mergesort we loop through the list once and install 2 new list. For this the runtime is O(n).
the space complexity for mergesort is O(1), as we store one list. the space complexity for merge is 
0(2n), as we got two list to store. and the space complexity for the last function is also O(2n), as we got two list store and then we put them together so we got O(1).


## Search in a rotated sorted array
First we must find the pivot in the list, afterwards we can search for our target number. The function findPivot got a runtime of O(log n) and also the function binarySearch. n is the length of the array. the last function use both function to find the target number. the space complexity of all three functions is O(1), as we store the list one time. 


## Trie
the big o notation for a tree is for creating a tree: this depends on how long the word is. so we got m (this is the longest word) and n(which is the total number of words) so the big o notatiion is O(m * n). For searching, deleting and insert we got O(a * n). A is the length of one word and n is the total number of words. for the suffix method the big o notation is O(2 * * n). N is the depth of the trie. The space complexity will be O(1) for every word. or O(n) for the whole trie. N is the number of words. 


## Http router using a trie
The class RouteTrie will create the structure and will traverse trough the Tree. The class RouteTrieNode will show the children dictionary and store each new data. For this class we got the same big o notation as for the last task called trie. N is the length of the route. The class Router got a time complexity of O(n). N is the number of nodes. The space complexity for all is O(n). 


