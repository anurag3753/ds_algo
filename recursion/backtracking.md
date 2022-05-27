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
