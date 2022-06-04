# Exhaustive Search and Backtracking

## Exhaustive Search : Exploring every possible combination from a set of choices or values.
- Often implemented recursively
- Applications:
  - producing all permutations of a set
  - enumerating all possible names, passwords, etc.
  - combinatorics and logic programming
- Tip:
  - To debug the recursive code, often it is a good idea to put a print statement in the top.
### A general pseudo-code algorithm for exhaustive search
```shell
Search(decisions):
- if there are no more decisions to make: Stop.
- else, let's handle one decision ourselves, and the rest by recursion.
  for each available choice C for this decision:
    - Choose C.
    - Serach the remaining decisions that could follow C.
```
- Often the search space consists of many decisions, each of which has several available choices.
- Example: When enumerating all 5-letter strings, each of the 5 letters is a decision, <br>
           and each of those decision has 26 possible choices

## Generate all the binary strings of N bits
- Here n, denotes the number of digits that are left to be processed
- When all digits are processed, op contains the answer
```python
"""
    i/p : print_binary(2)
    o/p : 00 01 10 11  

    i/p : print_binary(3)
    o/p : 000 001 ... 111
"""

def print_binary_helper(n, op):
    print(f"print_binary_helper({n},{op})")
    if n == 0:
        print(op)
    else:
        op1 = op + "0"
        op2 = op + "1"
        print_binary_helper(n-1, op1)
        print_binary_helper(n-1, op2)

def print_binary(n):
    print_binary_helper(n, "")

# client code
print_binary(3)
```
## Generate all the digit strings of length N
```python
def print_decimal_helper(n, op):
    print(f"print_decimal_helper({n},{op})")
    if n == 0:
        print(op)
    else:
        for i in range(10):
            op1 = op + str(i)
            print_decimal_helper(n-1, op1)

def print_decimal(n):
    print_decimal_helper(n, "")
# client code
print_decimal(2)
```
## Backtracking: Finding solution(s) by trying partial solutions and then abondoning them if they are not suitable.
- a "brute force"  algorithm technique (tries all paths)
- often implemented recursively
- Applications
  - producing all permutations of a set of values
  - parsing languages
  - games : anagrams, crosswords, 8 queens
  - escaping from maze

### A general pseudo-code algorithm for backtracking problems
```shell
Search(decisions):
- if there are no more decisions to make: Stop.
- else, let's handle one decision ourselves, and the rest by recursion.
  for each available choice C for this decision:
    - Choose C.
    - Explore the remaining choices that could follow C.
    - Unchoose C.(backtrack!)
```
```python
# Roll n dices and produce all possible outcomes
def dice_roll_helper(n, op):
    if n == 0:
        print(op)
    else:
        for i in range(1, 7):
            # choose
            op.append(i)
            # explore
            dice_roll_helper(n-1, op)
            # unchoose
            op.pop()

def dice_roll(n):
    dice_roll(3, [])
```
### Roll n dices and produce all possible outcomes that sum upto a desired sum
```python
def dice_desired_sum_helper(dice, desired_sum, sum_so_far, choices):
    if dice == 0 and sum_so_far == desired_sum:
        print(choices)
    else:
        # min_limit = sum_so_far + 1*(dice-1)
        # max_limit = sum_so_far + 6*(dice-1)
        for i in range(1, 7):
            if (sum_so_far + i + 1*(dice-1) <= desired_sum <= 
                sum_so_far + i + 6*(dice-1)):    
                # choose
                choices.append(i)
                # explore
                dice_desired_sum_helper(dice-1, desired_sum, sum_so_far+i, choices)
                # unchoose
                choices.pop()

def dice_desired_sum(n, desired_sum):
    dice_desired_sum_helper(3, 15, 0, [])

dice_desired_sum(3, 15)
```
### Generate all permutations of a string
[article](https://www.geeksforgeeks.org/write-a-c-program-to-print-all-permutations-of-a-given-string/)
```python
def permute_helper(string, chosen):
    if string == "":
        logger.debug("\n" + str(chosen) + "\n")
    else:
        for i in range(len(string)):
            # choose
            char = string[i]
            left_substr = string[0:i]
            right_substr = string[i+1:]
            rest = left_substr + right_substr
            # explore
            permute_helper(rest, chosen+char)
            # unchoose
            # N/A as string in python are immutable
            # so every time we make a call, we create a new string
            # and that is the reason, we need not remember choices
def permute(string):
    permute_helper(string, "")

permute("abc")
```
### Generate all permutations of a list of numbers
```python
# Permutations of a list of numbers
def permute_numbers_helper(li, chosen):
    if len(li) == 0:
        logger.debug("\n" + str(chosen) + "\n")
    else:
        for i in range(len(li)):
            # choose
            choice = li.pop(i)      # remove value at index i and return it
            chosen.append(choice)               
            # explore
            permute_numbers_helper(li, chosen)
            # unchoose
            li.insert(i, choice)
            chosen.pop()            # remove last value of chosen

def permute_numbers(li):
    permute_numbers_helper(li, [])

permute_numbers([1,2,3])
```
## Other Approaches [For generating permutations]
[tutorial](https://www.geeksforgeeks.org/write-a-c-program-to-print-all-permutations-of-a-given-string/)
[video](https://www.youtube.com/watch?v=jRyQVVvYBAM&list=PLjkkQ3iH4jy82KRn9jXeFyWzvX7sqYrjE&index=9)

### Generate all subsets of a list of names
```python
# approach 1
def sublists(list_of_people, chosen):
    if len(list_of_people) == 0:
        print(chosen)
    else:
        op1 = chosen.copy()
        op2 = chosen.copy()
        op2.append(list_of_people[0])
        list_of_people = list_of_people[1:]

        sublists(list_of_people, op1)
        sublists(list_of_people, op2)

li = ["anurag", "sumit", "amit"]
sublists(li, [])
```
```python
# approach 2
def sublists_helper(list_of_people, chosen):
    if len(list_of_people) == 0:
        print(chosen)
    else:
        # choose
        choice = list_of_people.pop(0)              # pull first person out of vector
        # explore
        chosen.append(choice)                       # add him in choice list
        sublists_helper(list_of_people, chosen)     # explore

        chosen.pop()                                # do not include in choice list
        sublists_helper(list_of_people, chosen)     # explore
        # # unchoose
        list_of_people.insert(0, choice)            # insert back at index 0

def sublists2(list_of_people):
    sublists_helper(list_of_people, [])

li = ["anurag", "sumit", "amit"]
sublists2(li)
```
## Other Approaches [For generating subsets]
[tutorial](https://github.com/LeadCoding/FrazArmy/blob/main/Recursion/lecture%207/Fraz_recursion_7_2.py)
[video](https://www.youtube.com/watch?v=0N3RCWa8jFM&list=PLjkkQ3iH4jy82KRn9jXeFyWzvX7sqYrjE&index=9)

### Generate all subsets with duplicate elements present [Learning]
[video](https://www.youtube.com/watch?v=u40eYbmT9zg&list=PLjkkQ3iH4jy82KRn9jXeFyWzvX7sqYrjE&index=11)
```python
def subset_helper(ip, op, i):
    if i == len(ip):
        print(op)
    else:
        op.append(ip[i])
        subset_helper(ip, op, i+1)
        op.pop()
        ## condition to handle duplicate elements
        while i+1 < len(ip) and ip[i] == ip[i+1]:
            i += 1
        # skip the element
        subset_helper(ip, op, i+1)

def subset(ip):
    op = []
    start_index = 0
    # to bring all duplicates at same place
    ip.sort()
    subset_helper(ip, op, start_index)

ip = [1,2,2]
ip = [1,2,3,2]
subset(ip)
```
### Choose k elements from a set of elements
[video](https://www.youtube.com/watch?v=DTFy9spEQGo&list=PLjkkQ3iH4jy82KRn9jXeFyWzvX7sqYrjE&index=13)
```python
# ip = [1,2,3,4], k = 2 op = [(1,2), (1,3) ... (2,3) ... (3,4)]
def combination_helper(ip, op, i, k):
    if k == 0:
        print(op)
        return
    # remaining elements (n - i + 1)
    # k = required elements
    if k > len(ip) - i + 1: return 
    if i == len(ip): return
    else:
        op.append(ip[i])
        combination_helper(ip, op, i+1, k-1)        # element selected, hence k-1
        op.pop()
        ## condition to handle duplicate elements
        while i+1 < len(ip) and ip[i] == ip[i+1]:
            i += 1
        # skip the element
        combination_helper(ip, op, i+1, k)          # element not selected, hence k 

def combination(ip, k):
    op = []
    start_index = 0
    # to bring all duplicates at same place
    ip.sort()
    combination_helper(ip, op, start_index, k)

# ip = [1,2,2]
ip = [1,2,3,2]
combination(ip, 2)
```
### Choose with a desired sum (numbers can be repeated infinite times)
[video](https://www.youtube.com/watch?v=Hca7284gCpI&list=PLjkkQ3iH4jy82KRn9jXeFyWzvX7sqYrjE&index=13)
```python
def infsum(ip, op, i, ds):
    if ds == 0: print(op)
    elif ds < 0: return
    elif i == len(ip) : return
    else:
        # do not pick
        infsum(ip, op, i+1, ds)     # we are not chossing it now, so in future also we will not choose it 
        # pick it
        op.append(ip[i])
        infsum(ip, op, i, ds-ip[i]) # in future also, we can choose it
        op.pop()

ip = [1,2,3]
desired_sum = 5
infsum(ip, [], 0, desired_sum)
```
### Choose with a desired sum (numbers to be chosen from array and numbers can be repeated in array)
[video](https://www.youtube.com/watch?v=6fARitpO0p8&list=PLjkkQ3iH4jy82KRn9jXeFyWzvX7sqYrjE&index=14)
```python
def target_helper(ip, op, i, ds):
    if ds == 0: print(op)
    elif ds < 0: return
    elif i == len(ip) : return
    else:
        # pick it
        op.append(ip[i])
        target_helper(ip, op, i+1, ds-ip[i])
        op.pop()
        ## condition to handle duplicate elements
        while i+1 < len(ip) and ip[i] == ip[i+1]:
            i += 1
        # skip the element
        target_helper(ip, op, i+1, ds) 

def target_sum(ip, desired_sum):
    ip.sort()   # to bring the same element together
    target_helper(ip, [], 0, desired_sum)

ip = [1,2,3,1]
desired_sum = 5
target_sum(ip, desired_sum)
```
