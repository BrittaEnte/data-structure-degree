## Find the square root
for this problem I used a binary search. If the mid of this binary search is the square root we will return it. If not we got two
cases, the square root is less or more than the mid. This is the same procedure as in a binary search. the runtime of this search is
in average O(log n). 

## Dutch nationa flag problem
For this problem I used the list method called insert. The advantage is that this method got two parameters. the first parameter
is the index followed by item. We just need make sure that the index of the figure null is also null. so that all zero will
be inserted at the beginning of the list. The figure 2 will be appended at the end of the list with the right index. the runtime of
this easy function is O(n), since we iterate just one trough the list

## Max and min in an unsorted array
For this solution it is checked if the figure is more than the maximum or less than the minimum. If yes, the number is set as maximum
vice versa minimum. The function only loops one time trough the given list so the runtime is O(n)

## Rearrange array elements
For this problem is used mergesort, because i used already binary search. Furthermore the runtime for mergesort is only  O(nlog(n)),as requested. 
After the mergesort we loop through the list once and install 2 new list. For this the runtime is O(n).

## Search in a rotated sorted array
First we must find the pivot in the list, afterwards we can search for our target number. The function findPivot got a runtime of
O(log n) and also the function binarySearch. the last function use both function to find the target number. 

## Trie
For inserting a new word we got a runtim of O(n) and for the find function we got O(log n)). Tries were used for autocomplete features in e.g. Word file. 

## Http router using a trie
For inserting the new route we got 0(n) and for the search function we got O(log(n)). The class RouteTrie will 
create the structure and will traverse trough the Tree. The class RouteTrieNode will show the children dictionary and store each new data. The last class 


