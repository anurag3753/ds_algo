## Maximum Subarray Sum (Kadane's Algorithm)
    - TC = O(n)
    - SC = O(1)
    - Logic : For every element, find out max subarray that must end with this element AND overall result is max of these values.
        - Two vars is sufficient to keep track (maxEnding, res)
        - maxEnding[i] = max(maxEnding[i-1] + arr[i], arr[i])

## Moore Voting Algorithm (> n/2 occurrence of an element in an array)
TC = O(n) SC = O(1)
```python
def find_majority(arr):
    " Return index of majority element "
    n = len(arr)
    count = 1
    res = 0   # 0th index element is majority
    for i in range(1, len(arr)):
        if arr[i] == arr[res]:
            count += 1        # GOT VOTE
        else:
            count -= 1        # LOST VOTE
        
        if count == 0:
            count = 1          # RESET COUNT
            res = i            # UPDATE INDEX FOR MAJORITY ELEMENT
        
    count = 0
    for i in range(len(arr)):
        if arr[res] == arr[i]:
            count += 1
    if count > n//2:
        return res
    return -1
```

## Left Rotate an array by d steps
Interesting Approach
TC = O(n) SC = O(d)
```python
def left_rotate(arr,d):
    temp = [None] * d
    for i in range(d):            # COPY first d elements in temp array
        temp[i] = arr[i]
    for i in range(d, len(arr)):  # Move n-d elements to front
        arr[i-d] = arr[i]
    for i in range(d):
        arr[n-d+i] = temp[i]
```

TC = O(n) SC= O(1)
```python
def left_rotate(arr, d):
    reverse(arr, 0, d-1)
    reverse(arr, d, n-1)
    reverse(arr, 0, n-1)

def reverse(arr, low, high):
    while(low < high):
        arr[low], arr[high] = arr[high], arr[low]
        low += 1
        high -= 1
```

## Right Rotate an array by d steps
TC = O(n) SC= O(1)
```python
def right_rotate(arr, d):
    reverse(arr, 0, n-1)
    reverse(arr, 0, d-1)
    reverse(arr, d, n-1)

def reverse(arr, low, high):
    while(low < high):
        arr[low], arr[high] = arr[high], arr[low]
        low += 1
        high -= 1
```

## Find missing and duplicate number
[gfg](https://www.geeksforgeeks.org/find-a-repeating-and-a-missing-number/)
```python
eq1 : missing - duplicate => sum(1..n) - sum(arr)
eq2 : 
```

## Find Missing and Duplicate Number in an Array of 1 to N | Swap Sort Need
[youtube](https://www.youtube.com/watch?v=uo4kuV3pWfE&list=PL_z_8CaSLPWdJfdZHiNYYM46tYQUjbBJx&index=3)
### Swap Sort O(n)
    - It contains 2 parts
    - Preprocessing
    - Calculation

```python
# Ideal Case :- arr[i] == i+1

arr = [2,3,1,5,1]
n = len(arr)

i = 0
while (i < n):
    if arr[i] != arr[arr[i]-1]:
        # swap arr[i], arr[arr[i]-1]
        temp = arr[arr[i]-1]
        arr[arr[i]-1] = arr[i]
        arr[i] = temp
    else:
        i += 1

for i in range(n):
    if arr[i] != i+1:
        missing, duplicate = i+1, arr[i]

print(missing, duplicate)
```