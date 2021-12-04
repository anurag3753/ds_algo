## Check if array pairs are divisible by K
```python
Naive: O(n2) [Not perfect code, but an intuition]
1. create visited array b[n] of size n, initialized as False
2. For each element in arr; compute x = (arr[i]% k + k)%k
3. For each j starting from i+1; if b[j] == False(not visited); then compute y =  (arr[j]% k + k)%k
4. if x == 0 and y == 0; mark both index as True in visited array
5. elif x+y == k, then mark both as True in visited array
6. else, if no such j; Return False

 
Efficient: O(n) [Use HashMap or Dictionary]
1. Loop over arr, and create dict of remainders as
    - rem = arr[i]%k +k)%k
    - my_dict[rem] += 1
2. Check if 0 remainders count are not even
    - if my_dict[0] % 2 != 0:
        - return False
3. For i = 1 to k:
    if my_dict[i] != my_dict[k-i]:
        # k = 3 (we are looking for 1+2 == 3)
        # my_dict[1] = 2
        # my_dict[2] = 2
        return False
4. return True
```
## Length of the longest substring without repeating characters
- [gfg](https://www.geeksforgeeks.org/length-of-the-longest-substring-without-repeating-characters/)
- [video](https://www.youtube.com/watch?v=3IETreEybaA)
- [my_implementaion](https://practice.geeksforgeeks.org/problems/length-of-the-longest-substring3036/1)

## Is soduku Valid ??
- [gfg](https://www.geeksforgeeks.org/check-if-given-sudoku-board-configuration-is-valid-or-not/)
- [video](https://youtu.be/Pl7mMcBm2b8?t=627) :- Much Better than GFG
- [my_implementation]

