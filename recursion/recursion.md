# Recursion Intro

## Make input smaller, but why ??
- actually we do not make input smaller, but it automatically becomes smaller based on the decisions we took in our recursion

## Recursion - Decision Space ??
- It acts as an identification method for recursion. If we have been provided a question, in which we are given `choices and decision`, then we can represent it in terms of decision space.

## Recursion Tree ??
- It is most important concept. If you managed to draw recursive tree for a problem, then writing code for that problem will be a cakewalk.
- I/P - O/P method to design the recursion tree.

## 2 steps to solve any recursive problem
- Design Recursion Tree
- Implement based on Recursion Tree

# Methods to approach recursion (4 approaches)
- Base Condition - Induction - Hypothesis (Making I/P smaller) [IBH]
- Recursive Tree - I/P O/P Method (Decision)
- Choice Diagram
- Will discuss later

## BC-Induction-Hypothesis (IBH)
- Write Hypothesis(Apply on smaller input)
    - solve(n) = 1 to n
    - solve(n-1) = 1 to n-1
- But in order to make hypothesis work, we need to write logic accordingly in `induction` step.
- Base Condition
    - smallest/largest valid input
    - smallest/largest invalid input
- Note : It is very much used in Trees, LL

```python
## Print 1 --> N
def print_n(n):
    if n == 0:                                     # Base Condition
        return 
    print_n(n-1)    # it will give me 1 ... n-1    # Hypothesis 
    print(n)                                       # Induction 
```
```python
## Print N --> 1
def print_n(n):
    if n == 0:                                     # Base Condition
        return 
    print(n)                                       # Induction 
    print_n(n-1)    # it will give me n-1 ... 1    # Hypothesis 
```
```python
## Return height of tree
def height(root):                                 # It will return me height of tree
    if root is None:                              # Base Condition
        return 0
    lh = height(root.left)                        # Hypothesis
    rh = height(root.right)                       # Hypothesis
    return 1 + max(lh, rh)                        # Induction  
```
```python
## Sort an array/stack using recursion
def insert(arr, item):
    if len(arr) == 0 or arr[-1] <= item:    # Base Condition
        arr.append(item)
        return
    temp = arr[-1]                          # Store last element in a variable
    arr.pop()                               # Remove it from array
    insert(arr, item)                       # Hypothesis
    arr.append(temp)                        # Induction

def mysort(arr):
    if len(arr) == 1:      # Base Condition
        return
    item = arr[-1]         # Store last element in a variable
    arr.pop()              # Remove it from array/stack          
    mysort(arr)            # Hypothesis
    insert(arr, item)      # Induction
```
## Delete middle element from stack
[youtube](https://www.youtube.com/watch?v=oCcUNRMl7dA&list=PL_z_8CaSLPWeT1ffjiImo0sYTcnLzo-wY&index=8)
```python
def del_middle_helper(st, k):                
    if k == 1:                                 # Base Condition 
        st.pop()
        return
    temp = st.pop()                            # Remove it from stack 
    del_middle_helper(st, k-1)                 # Hypothesis
    st.append(temp)                            # Induction

def del_middle(stack):
    if len(stack) == 0:
        return
    middle_element = len(stack) // 2 + 1       # as per definition from question
    del_middle_helper(stack, middle_element)
    return
```

## Reverse stack
```python
def insert(st, element):
    if len(st) == 0:
        st.append(element)
        return
    temp = st.pop()
    insert(st, element)
    insert.append(temp)

def reverse(st):
    if len(st) == 1:
        return
    temp = st.pop()
    reverse(st)
    insert(st, temp)
```

## Kth symbol in grammar (IBH Method)
[leetcode](https://leetcode.com/problems/k-th-symbol-in-grammar/)
[youtube](https://www.youtube.com/watch?v=5P84A0YCo_Y&list=PL_z_8CaSLPWeT1ffjiImo0sYTcnLzo-wY&index=10)
```python
def kthGrammar(self, n: int, k: int) -> int:
    if n == 1 and k == 1:
        return 0
    else:
        length = 2 ** (n-1)
        mid = length // 2
        if k <= mid:
            return self.kthGrammar(n-1, k)
        else:
            # We need to invert 1 -> 0 and 0 -> 1 if ans lies in 2nd half
            return (self.kthGrammar(n-1, k-mid)) ^ 1
```

## TOH (IBH Method)
```python
def toh(n, s, d, h):    # source to destination using helper
    if n == 1:
        print(f"Move disk {n} from {s} -> {d}")
    else:
        toh(n-1, s, h, d)
        print(f"Move disk {n} from {s} -> {d}")
        toh(n-1, h, d, s)

# Client code
toh(3, "a", "b", "c")
```

# IP-OP Method
![IP-OP Method](https://github.com/anurag3753/ds_algo/blob/main/images/ip_op.JPG)

## Print all subsets
[youtube](https://www.youtube.com/watch?v=Yg5a2FxU4Fo&list=PL_z_8CaSLPWeT1ffjiImo0sYTcnLzo-wY&index=12)
```python
# Using IP-OP Method, it was a cakewalk
def print_subsets(ip, op=""):
    if len(ip) == 0:
        print(op)
    else:
        op1 = op + ""
        op2 = op + ip[0]
        ip = ip[1:]
        print_subsets(ip, op1)
        print_subsets(ip, op2)
# Client Code
print_subsets("abc")
```
# Print all subsets = Print powerset = Print all subsequences (same code will work)
- powerset = all subsets of a set = print subsets
    - ab = {"", a, b, ab}
    - {a,b} = {"", a, b, ab}
- string variation:
    - substring
        - Continuous in nature
        - abc = a, b, c, ab, bc, abc [ac not allowed]
    - subsequences
        - abc = a, b, c, ab, bc, ac, abc [ac is allowed]
        - order matters here. Means `cb` can not be a subsequence
    - subset
        - Even the order does not matter here.
        - `ca` is also allowed here. order does not matter
        - {a,c} or {c,a} = All convey the same meaning
## Print unique subsets
- Put them in a set to get unique subsets
- sort them, to return output in lexicographic order

## Permutation with spaces
[gfg](https://practice.geeksforgeeks.org/problems/permutation-with-spaces3627/1)
[youtube](https://www.youtube.com/watch?v=1cspuQ6qHW0&list=PL_z_8CaSLPWeT1ffjiImo0sYTcnLzo-wY&index=14)

## Permutation with case change
[gfg](https://www.geeksforgeeks.org/permute-string-changing-case/)
[youtube](https://www.youtube.com/watch?v=J2Er5XceU_I&list=PL_z_8CaSLPWeT1ffjiImo0sYTcnLzo-wY&index=15)
```python
def case_change(ip, op=""):
    if ip == "":
        print(op)
    else:
        op1 = op + ip[0]
        op2 = op + ip[0].capitalize()
        ip = ip[1:]
        case_change(ip, op1)
        case_change(ip, op2)
```

## Letter case permutation
[youtube](https://www.youtube.com/watch?v=4eOPYDOiwFo&list=PL_z_8CaSLPWeT1ffjiImo0sYTcnLzo-wY&index=16)
[leetcode](https://leetcode.com/problems/letter-case-permutation/submissions/)

## Generate all balanced parenthesis
[youtube](https://www.youtube.com/watch?v=eyCj_u3PoJE&list=PL_z_8CaSLPWeT1ffjiImo0sYTcnLzo-wY&index=17)
[interviewbit](https://www.interviewbit.com/problems/generate-all-parentheses-ii/)
```python
def bal_parenthesis(open, close, op):
    if open == 0 and close == 0:
        print(op)
        return
    if open != 0:    # We are always using open bracket in Recursion Tree
        bal_parenthesis(open-1, close, op + "(")
    if open < close: # We are only allowed to do it, when we are having more open than close
        bal_parenthesis(open, close-1, op + ")")
# client code
bal_parenthesis(3,3,"")
```
## Print N-bit binary numbers having more 1s than 0s
[gfg](https://practice.geeksforgeeks.org/problems/print-n-bit-binary-numbers-having-more-1s-than-0s0252/1)
[youtube](https://www.youtube.com/watch?v=U81n0UYtk98&list=PL_z_8CaSLPWeT1ffjiImo0sYTcnLzo-wY&index=18)

## Josephus Problem
[youtube](https://www.youtube.com/watch?v=ULUNeD0N9yI&list=PL_z_8CaSLPWeT1ffjiImo0sYTcnLzo-wY&index=19)
[gfg](https://practice.geeksforgeeks.org/problems/josephus-problem/1)
```python
class Solution:
    def josephus_helper(self, k, li, index=0):
        if len(li) == 1:
            return li[0]
        else:
            index = (index + k) % len(li)
            li.pop(index)
            return self.josephus_helper(k, li, index)

    def josephus(self,n,k):
        li = list(range(1,n+1))
        index = 0   # starting index for game
        return self.josephus_helper(k-1, li, index)
```
