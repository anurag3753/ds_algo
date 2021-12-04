# Use Case for static arrays:
    - Storing and accessing sequential data
    - Temporarily storing objects
    - Used by IO routines as buffers
        - You want to process a very large file, it does not fit into memory. Then you need to process the file in chunks using buffers (buffers are nth but static arrays)
    - Lookup tables and inverse lookup tables
        - Due to indexing property of array, arrays are used in lookup tables
    - Can be used to return multiple values from a function
        - In C, we can return only 1 value. But if want to return multiple values, we return the reference to an array which contains all the return values that we want
    - Used in dynamic programming to cache answers to subproblems
        - Ex. like knapsack problem, coin change problem

|           | Static Array | Dynamic Array |
|-----------|--------------|---------------|
| Access    | O(1)         | O(1)          |
| Search    | O(n)         | O(n)          |
| Insertion | N/A          | N/A           |
| Appending | N/A          | O(1)          |
| Deletion  | N/A          | O(n)          |

# List Introduction
    - It internally uses array for implementation.
    - It grows dynamically. 
    - It allows items of different types.

## Popular list functions
    - li.insert(ind, ele) : It inserts element `ele` at index `ind`
    - li.count(ele) : It returns the count of element `ele` present in list
    - li.index(ele) : Returns the index of first ocurence of element `ele`
    - li.index(ele, start, end) : start :- inclusive, end :- exclusive
    - li.remove(ele) : It removes first occurence of element `ele`. Raises error if element not present
    - li.pop() : It removes last item from list and returns it. Raises error if pop from empty list.
    - li.pop(ele_index) : It removes the item at index `ele_index`
    - del li[1] : del is general purpose. It removes item from li at index 1
    - del li[0:2] : Item at index 0, 1 are removed
    - li.reverse() : Reverse list (It works inplace)
    - li.sort() # It sorts list inplace
    - sorted() # It returns a seperate copy with sorted elements
    - li.reverse() # It reverse the list inplace
    - reversed() # It returns a seperate copy with reversed elements

## Working of list in Python
    - It uses an array underline.
    - Every member of a list is actually a reference. So this array is actually an array of references.
    - And these references must be stored at contiguous locations, because the underline data structure is array.
    - It also does some `preallocated extra space for future additions`
    - Advantages:
        - Random Access
        - Cache friendly :
            - Locality of reference: When CPU fetches data, they also fetch the nearby data too. So, when we go the next data chances are that it is already
            - present in the main memory. Hence there are fewer cache misses.
    - Disadvantages:
        - Insertion, Deletion : Are SLOW O(n)
        - Search is also slow for unsorted data : O(n)
    
### How does Dynamic Size Work ?
    - Preallocates some extra space
    - If becomes full, do the following:
        - Allocate a new space of larger size(multiply by x)
        - Copy old space to new
        - Free old space
        - pop and append are both constant time on average

### Amortized Time Calculation:
    - Assumptions:
        - Initial Capacity : n
        - We double the size when list becomes full
    
    - Average Time to append (n+1) items : O(1) + O(1) + ...... + O(n)
    -                                      ----------------------------
    -                                                  n+1
    - Here, while inserting the (n+1)th item, we had to copy all elements to new location. That is why it took O(n)
    - i.e. O(n) + O(n) / O(n) = O(1)
    - So, it takes constant time on average to insert n+1 items. (Catch : We are always interested in inserting items in the end)

## Slicing (List, Tuple and String)
    - Slicing does not change things inplace
    - list slicing returns list, string slicing returns string and tuple slicing returns tuple
    - We can have -ve step also. When you have -ve step then make sure your start > end
        - Ex. l = [10, 20, 30, 40, 50]  ===>   l[4:1:-1] = [50, 40, 30]
        - Ex l[-1:-6:-1] == l[::-1] ==> l[-1:-(len)+1:-1] (It resolves to this)

### Use of `is` operator
    - `is` operator is used to see, if two objects are referencing to same location
    - If values are same, then python tries to map as many vars as possible which points to same value.
```python
    >>> a = 3
    >>> b = 3
    >>> a is b
    >>> True

    From this we see, that python first tries to map as many vals as possible to same location.    
```
```python
l = [10, 20, 30]
l2 = l1[:]
t1 = (10, 20, 30)
t2 = t1[:]
s1 = "geeks"
s2 = s1[:]
print(li is l2)     # o/p   False (list creates a copy despite vals are same)
print(t1 is t2)     # o/p   True  (tuple pointitng to same memory location if val is same)
print(s1 is s2)     # o/p   True  (string pointitng to same memory location if val is same)
```

### Comprehensions in Python
    - Dictionary Comprehensions
        - l1 = [101, 102, 103] , l2 = ["gfg", "ide", "courses"]
        - d3 = {l1[i]: l2[i] for i in range(len(l2))}
        - Better Way : d3 = dict(zip(l1, l2))
    - Inverting a Dictionary
        - d1 = {101: "gfg", 103: "practice", 102: "ide"}
        - d2 = {v:k for (k,v) in d1.items()}


## TIPS:
    - Multiple values can be returned from python function as tuple
    - On the receiving end, you need to unpack the returned tuple
    - Comprehensions (List, Set, Dictionary) are available python comprehensions
 