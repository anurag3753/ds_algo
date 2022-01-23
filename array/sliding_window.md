# Identification:
    - I/P : array, size of subarray
    - I/P : string, substring (since substring is also continuous) / anagram wale question mai bhi lag jata hai
    - And, it must be asking (maximum/minimum) value for a certain parameter
    - K (which will be window size/subarray size)
    - windows formed (n-k+1)
    - jaha par bhi, (subarray, windows size, aur kuch largest de rakha hoga. to jaroor socho sliding window lag sakta hai kya)

# Types of Sliding Window:
- Fixed size window (Easy)
    - It is asked to compute largest sum/smallest sum
    - window size de rakha hai, sum nikalna hai
- Variable size window (Relatively Tough)
    - It is asked to find the largest window/smallest window subjected to a condition
    - sum de rakha hai, maximum window size nikalna hai
    - Ex . Find largest subarray with sum as 13.
        - Here, we need to find the window size

# Brute Force -> Optimization
- Check for below three steps, if you only come up with brute force so far:
    - Repetitive work ??

# Problems:

```python
# Generic Code
while j < n:
    # Do calculations
    if j - i + 1 < k:    # we have not reached our window size
        j += 1           # just increase till we hit our window size
    else:
    # 2 steps in else part
        # step1 :- Compute answer from calculations (ans <-- calculations)
        # step2 :- Move the window
```

## Maximum sum subarray of size k (fixed size)
[youtube](https://www.youtube.com/watch?v=KtpqeN0Goro&list=PL_z_8CaSLPWeM8BDJmIYDaoQ5zuwyxnfj&index=3)
    - Identification
    - PS - I/P and O/P
    - Abstract --> code
    - code
```python
size : 7
arr [] : [2, 5, 1, 8, 2, 9, 1]
k : 3 (window size)

Return the max sum of all subarrays of size = k

- We need to have start and end of the window (i -> start, j -> end)
- Current window size = j - i + 1
- We will start i = 0, j = 0. We will hit the condition first time when (j - i + 1 == k)
- Initially, we need to do only j += 1
- Once we hit the window of size k, then we need to maintain that window (i += 1 and j += 1)
- We need to do the task till j < size_of_array

# Code
arr = [2, 5, 1, 8, 2, 9, 1]
n = len(arr)
i = j = 0        # start, end
max_sum = INT_MIN
sum_ = 0
while j < n:
    sum_ += arr[j]
    if j - i + 1 < k:
        j += 1
    elif j - i + 1 == k:
        # 2 steps
        # 1. Calculate my answer 
        # 2. Slide the windows
        max_sum = max(sum_, max_sum)
        sum_ = sum_ - arr[i]
        i += 1
        j += 1
return max_sum
```
## First -ve integer in every window of size k
[youtube](https://www.youtube.com/watch?v=uUXXEgK2Jh8&list=PL_z_8CaSLPWeM8BDJmIYDaoQ5zuwyxnfj&index=4)
```python
i = j = 0        # start, end
res = []         # compute the final result list
queue = deque()  # queue to store the -ve elements
while j < n:
    if arr[j] < 0:
        queue.append(arr[j])    # store all the -ve numbers in queue
    if j - i + 1 < k:
        j += 1
    elif j - i + 1 == k:
        # if current window contains no -ve numbers, then append 0 to res
        if len(queue) == 0:
            res.append(0)
        else:
            # queue front will always contains the 1st -ve number
            res.append(queue[0])
            # Slide the window
            if arr[i] == queue[0]:
                # Remove the element from queue, if matches with the removing element from window
                queue.popleft()
        i += 1
        j += 1
return res
```
## Count occurences of anagram
- [youtube](https://www.youtube.com/watch?v=MW4lJ8Y0xXk&list=PL_z_8CaSLPWeM8BDJmIYDaoQ5zuwyxnfj&index=5)
- [gfg](https://practice.geeksforgeeks.org/problems/count-occurences-of-anagrams5839/1)
- A neat concept, I learned in this process is that, suppose we need to check for the emptiness of a dictionary
- Then we can maintain a count variable which shows total number of unique elements. We create the elements dict. While doing the computations, we check if at any point the value of a key becomes zero, at that time we need to decrement the count also.

## Maximum of all subarrays of size k
- [youtube](https://www.youtube.com/watch?v=xFJXtB5vSmM&list=PL_z_8CaSLPWeM8BDJmIYDaoQ5zuwyxnfj&index=6)
- [gfg](https://practice.geeksforgeeks.org/problems/maximum-of-all-subarrays-of-size-k3101/1)
- It is a tricky approach. Based on observation made while solving question. A similar variation was asked to me in one of the interviews question, which I could not solve. We have used deque also for solving this question.

# Variable size window
| Fixed Size           | Variable Size       |
|----------------------|---------------------|
| WS --> Given         | WS --> Min/Maximize |
| Sum --> Min/Maximize | Sum --> Given       |

## Identification:
    - arr/string ka question
    - subarray/substring mention hoga
    - isme ek sum/condition de rakhi hogi, jo ws indentify karne mai help karegi
    - We need to maximize/minimize the window size

# General code for variable size window problems
```python
# Generic Code
while j < n:
    # Do calculations
    if condition < k:    # we have not met the given condition yet
        j += 1             # just increase till we hit our window size
    elif condtion == k:    
        # compute result   # res <-- calculations
        j += 1
    elif contition > k:
        while condition > k:
            # remove calculations for `i`
            i += 1
        j += 1
return res
```

## Largest subarry of +ve numbers with sum = k
```python
# Here sum = k
i = j = 0
_sum = 0
res = 0
while j < n:
    _sum += arr[j]
    if _sum < k:
        j += 1
    elif _sum == k:
        res = max(res, j - i + 1)    # Update res window size
        j += 1
    else:
        # sum became greater than k, so slide window
        while _sum > k:
            _sum -= arr[i]
            i += 1
        j += 1
return res
```

## Longest substring with k unique characters
[gfg](https://practice.geeksforgeeks.org/problems/longest-k-unique-characters-substring0853/1/#)
```python
"""
s : aabacbebebe
k : 3
Explaination : aabac, abacb, bacbe , cbebebe    [each contains k=3 unique characters]
o/p : 7 (cbebebe)
"""
i = j = 0
res = -1
uniq_char = dict()
while j < n:
    if arr[j] in uniq_char:
        uniq_char[arr[j]] += 1
    else:
        uniq_char[arr[j]] = 1

    if len(uniq_char) < k:
        j += 1
    elif len(uniq_char) == k:
        res = max(res, j - i + 1)    # compute answer
    elif len(uniq_char) > k:
        while len(uniq_char) > k:
            uniq_char[arr[i]] -= 1
            if uniq_char[arr[i]] == 0:
                uniq_char.pop(arr[i])
            i += 1
        j += 1
return res
```
## Longest substring without any repeating characters
[youtube](https://www.youtube.com/watch?v=L6cffskouPQ&list=PL_z_8CaSLPWeM8BDJmIYDaoQ5zuwyxnfj&index=12) <br>
[gfg](https://www.geeksforgeeks.org/length-of-the-longest-substring-without-repeating-characters/)
```python
# similar to above except, instead of k we need to check it against window size at any given point in time
len(uniq_char) == j - i + 1
```

## Pick toys | An interesting problem
[youtube](https://www.youtube.com/watch?v=seOKHXB_w74&list=PL_z_8CaSLPWeM8BDJmIYDaoQ5zuwyxnfj&index=12)

## Minimum window substring
[youtube](https://www.youtube.com/watch?v=iwv1llyN6mo&list=PL_z_8CaSLPWeM8BDJmIYDaoQ5zuwyxnfj&index=13) <br>
[gfg](https://practice.geeksforgeeks.org/problems/smallest-window-in-a-string-containing-all-the-characters-of-another-string-1587115621/1/)