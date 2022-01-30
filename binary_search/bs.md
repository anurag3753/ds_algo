# Binary Search

```python
# To avoid overflow in Binary search
mid = ( low + high ) // 2 
mid = low + (high - low)//2    # Will prevent integer overflow error, useful in languages like c++
```

## Binary Search
```python
def binary_search(arr, n, item):
    low = 0
    high = n-1
    while low <= high:
        mid = (low + high)//2
        if arr[mid] == item:
            return mid
        elif arr[mid] < item:
            low = mid + 1
        else:
            high = mid - 1
    return -1
```

## BS on Reverse Sorted array:
```python
elif arr[mid] < item:
    high = mid - 1
else:
    low = mid + 1
```

## Order not known search
- Suppose you do not know, if the array is sorted in asc/desc order. In such scenarios, a safe thing would be to compare arr[0] with arr[n-1] to identify asc/desc order

## First and last occurrence
[youtube](https://www.youtube.com/watch?v=zr_AoTxzn0Y&list=PL_z_8CaSLPWeYfhtuKHj-9MpYb6XQJ_f2&index=5)
- Create a variable res and use it to store the last valid occurrence in search. Once we are done with bs, we will have our ans stored in res
```python
def first_occurence(arr, n, item):
    low = 0
    high = n - 1
    res = -1
    while low <= high:
        mid = (low + high)//2
        if arr[mid] == item:
            res = mid                # Store the last valid occurrence in res
            high = mid - 1           # Continue the search on the LHS 
        elif arr[mid] < item:
            low = mid + 1
        else:
            high = mid - 1
    return res

def last_occurence(arr, n , item):
    res = mid                        # Store the last valid occurrence
    low = mid + 1                    # Continue Search on RHS to get last occurrence
```

## Find Minimum in Rotated Sorted Array
[leetcode](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/submissions/) <br>
[youtube](https://www.youtube.com/watch?v=4WmTRFZilj8&list=PL_z_8CaSLPWeYfhtuKHj-9MpYb6XQJ_f2&index=7) ```Related Concept but applicable in next question``` <br>
[pepcoding](https://www.youtube.com/watch?v=Kcj2NGnuSNg&list=PL-Jc9J83PIiHhXKonZxk7gbEWsmSYP5kq&index=15)
- Please check both videos and leetcode submission for details

## Number of times an array is rotated
[youtube](https://www.youtube.com/watch?v=4WmTRFZilj8&list=PL_z_8CaSLPWeYfhtuKHj-9MpYb6XQJ_f2&index=7) <br>
- Valid for unique and clockwise rotated array.
[pepcoding](https://www.youtube.com/watch?v=JUYjIZjz6js)
```python
# Only valid if array is rotated in clockwise fashion
# Just return the index of smallest element, assuming no duplicates

def findMin(self, arr: List[int]) -> int:
    low = 0
    high = len(arr) - 1
    n = len(arr)
    
    # Handle the case if array is already sorted
    if arr[low] <= arr[high]:
        return 0
    
    while low <= high:
        mid = (low + high) // 2
        prev_ele = (mid - 1 + n) % n
        next_ele = ( mid + 1 ) % n
        
        # two observations: 
        # if arr[mid] > next_element -> then it means next element is min value
        # else arr[mid] < prev_element --> means you are only the smallest element
        if arr[mid] > arr[next_ele]:
            return (mid+1)%n
        elif arr[mid] < arr[prev_ele]:
            return mid
        elif arr[low] < arr[mid]:   # move in unsorted region
            low = mid + 1
        elif arr[mid] < arr[high]:  # move in unsorted region
            high = mid - 1
```

## Find an element in a rotated sorted array
[youtube](https://www.youtube.com/watch?v=Id-DdcWb5AU&list=PL_z_8CaSLPWeYfhtuKHj-9MpYb6XQJ_f2&index=8) <br>
[leetcode](https://leetcode.com/problems/search-in-rotated-sorted-array/submissions/) <br>
- Idea is based on finding the index of minimum element
- Once we got that we can call 2 binary search to both the sorted halves

## Search in almost sorted array
[gfg](https://www.geeksforgeeks.org/search-almost-sorted-array/) <br>
[youtube](https://www.youtube.com/watch?v=W3-KgsCVH1U&list=PL_z_8CaSLPWeYfhtuKHj-9MpYb6XQJ_f2&index=10) <br>
```python
def search_almost(arr, n, item):
    low = 0
    high = n-1
    while low <= high:
        mid = (low+high)//2
        if arr[mid] == item:
            return mid
        elif mid != 0 and arr[mid-1] == item:
            return mid - 1
        elif mid != n-1 and arr[mid+1] == item:
            return mid + 1
        elif arr[mid] < ele:
            high = mid - 2
        else:
            low = mid + 2
    return -1
```

## Ceil and Floor in Sorted Array (Easy)
[youtube_floor](https://www.youtube.com/watch?v=5cx0xerA8XY&list=PL_z_8CaSLPWeYfhtuKHj-9MpYb6XQJ_f2&index=10) <br>
[youtube_ceil](https://www.youtube.com/watch?v=uiz0IxPCUeU&list=PL_z_8CaSLPWeYfhtuKHj-9MpYb6XQJ_f2&index=11) <br>

## Next Alphabetical Element
[youtube](https://www.youtube.com/watch?v=X45c37QMdX0&list=PL_z_8CaSLPWeYfhtuKHj-9MpYb6XQJ_f2&index=12)
```python
def next_alphabet(arr, n, char):
    low = 0
    high = n - 1
    res = ""
    while low <= high:
        mid = (low+high)//2
        if arr[mid] <= char:
            low = mid + 1
        else:
            res = arr[mid]
            high = mid - 1
    return res
# client code
arr = ["a", "b", "g", "i", "j", "k"]
n = len(arr)
print(next_alphabet(arr, n, "b"))
```

## Find position of an element in an Infinite Sorted Array
```python
def find_element(arr, n, key):
    low = 0
    high = 1
    # Increase high till the key lies b/w low and high
    while key > arr[high]:
        low = high
        high = high * 2
    # Apply regular binary search provided low and high keys
    binary_search(arr, low, high, key)
```

## Minimum Difference Element in a sorted array
[youtube](https://www.youtube.com/watch?v=3RhGdmoF_ac&list=PL_z_8CaSLPWeYfhtuKHj-9MpYb6XQJ_f2&index=16)
```python
def min_diff_element(arr, n, key):
    low = 0
    high = n - 1
    while low <= high:
        mid = (low+high)//2
        if arr[mid] == key:
            return arr[mid]
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    if low >=0 and high <= n-1:
        # Answer lies in range
        if abs(arr[low]-key) < abs(arr[high]-key):
            return arr[low]
        else:
            return arr[high]
    elif low >= 0:
        # It will happen, when high goes out of bound
        return arr[low]
    else:
        # It will happen when low goes out of bound
        return arr[high]
```

# Binary Search on answer
[youtube](https://www.youtube.com/watch?v=IZP_8-JZqhM&list=PL_z_8CaSLPWeYfhtuKHj-9MpYb6XQJ_f2&index=16) <br>
- Can apply binary search on unsorted array
- We develop a criteria to decide
    - Whether mid is answer or not,
    - If mid is not answer, then another criteria to identify which side to move

## Index of Peak Element
[youtube](https://www.youtube.com/watch?v=OINnBJTRrMU&list=PL_z_8CaSLPWeYfhtuKHj-9MpYb6XQJ_f2&index=17)
- Better code in GFG lectures. Used GFG lecture code below
```python
def peak(arr, n):
    low = 0
    high = n - 1
    while low <= high:
        mid = (low + high)//2
        # Neatly written condition
        if (mid == 0 or arr[mid-1] <= arr[mid]) and \
            (mid == n-1 or arr[mid+1] <= arr[mid]):
            return mid
        elif mid > 0 and arr[mid-1] >= arr[mid]:
            high = mid - 1
        else:
            low = mid + 1
```

## Bitonic Point = Same as finding a peak element in array
[youtube](https://www.youtube.com/watch?v=BrrZL1RDMwc&list=PL_z_8CaSLPWeYfhtuKHj-9MpYb6XQJ_f2&index=19) <br>
[gfg](https://practice.geeksforgeeks.org/problems/maximum-value-in-a-bitonic-array3001/1)

## Search in Bitonic Array
[youtube](https://www.youtube.com/watch?v=IjaP8qt1IYI&list=PL_z_8CaSLPWeYfhtuKHj-9MpYb6XQJ_f2&index=19) <br>
- Find Bitonic Element index = `index`
- BinarySearchAscOrder(arr, 0, `index-1`)
- BinarySearchDescOrder(arr, `index`, n-1)

## Search in Row-wise and Column-wise sorted array
[youtube](https://www.youtube.com/watch?v=VS0BcOiKaGI&list=PL_z_8CaSLPWeYfhtuKHj-9MpYb6XQJ_f2&index=20)
- O(n+m) [using Binary Search]
```python
def search(arr, n, m, key):
    print(f"rows = {n} cols = {m}")
    i = 0
    j = m-1
    while (i >= 0 and i <= n-1) and (j >= 0 and j <= m-1):
        print(f"i = {i} \t j = {j} \t arr[i][j] : {arr[i][j]}")
        if arr[i][j] == key:
            return i,j
        elif arr[i][j] > key:
            j -= 1
        else:
            i += 1
    return -1

arr = [
    [10,20,30,40],
    [15,25,35,45],
    [29,30,37,45],
    [32,33,39,50]
]

n = len(arr)
m = len(arr[0])
key = 29
print(search(arr, n, m, key))
```

## Allocate Minimum Number Of Pages
[gfg](https://www.geeksforgeeks.org/allocate-minimum-number-pages/) <br>
[youtube](https://www.youtube.com/watch?v=2JSQIhPcHQg&list=PL_z_8CaSLPWeYfhtuKHj-9MpYb6XQJ_f2&index=21)
```python
def isvalid(arr, n, k, mid):
    students = 1
    sum  = arr[0]
    for i in range(1,n):
        sum += arr[i]
        if sum > mid:
            students += 1
            sum = arr[i]
        if students > k:
            return False
    return True

def allocate_pages(arr, n, k):
    # books are less than number of students
    if n < k:
        return -1

    low = max(arr)
    high = sum(arr)
    res = -1
    while low <= high:
        mid = (low+high)//2
        if isvalid(arr, n, k, mid):
            res = mid
            high = mid - 1
        else:
            low = mid + 1
```
Related Problems:
[Painter Partition Problem](https://www.geeksforgeeks.org/painters-partition-problem/) <br>
[1482-leetcode](https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/) <br>
[1283 Find the Smallest Divisor Given a Threshold](https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/) <br>
[1231 Divide Chocolate](https://leetcode.ca/all/1231.html) <br>
[1011. Capacity To Ship Packages Within D Days](https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/) <br>
[875. Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/) <br>
[410. Split Array Largest Sum](https://leetcode.com/problems/split-array-largest-sum/) <br>
[774 Max Distance to Gas Station](https://leetcode.ca/all/774.html) <br>