# STACK (LIFO)
    - Main operations (Only push and pop modify the stack rest functions does not modify)
        - isEmpty()
        - push(x)
        - pop()
        - peek() : Returns top item
        - size() : Returns size of stack
    - In Python we have list.
        - push = append
        - pop = pop
        - peek = use -1 index
        - size = len
        - isEmpty = if not li

## <span style="color:red">Application of STACK:</span>
<ol>
    <li>  function calls (functions are executed in LIFO order). This stack is also called Function Call Stack.
    </li>
    <li> checking for Balanced paranthesis </li>
    <li> Reversing Items </li>
    <li> Infix to prefix/postfix </li>
    <li> Evaluation of prefix/postfix </li>
    <li> Stock span problem and its variants (Most IMP interview questions) </li>
    <li> Undo/Redo OR Forward/Backward </li>
</ol>

## <span style="color:red">STACK in Python</span>
<ol>
    <li> Using List (implemented using Dynamic Size Arrays) </li>
    <li> Using collections.deque (implemented using Doubly LL) </li>
    <li> Using queue.LIFOQueue (Only used in multithreaded environment) </li>
    <li> Using our own implementation </li>
</ol>

### <span style="color:red">Using Deque</span>
```python
from collections import deque
stack = deque()
stack.append(10)
stack.append(20)
stack.append(30)
print(stack.pop())
top = stack[-1]
print(top)
size = len(stack)
print(size)

Advantages/Disadvantages:
- deque worst case for any operation is O(1)
- Not cache friendly (as it is a linked list implementation)
```

### <span style="color:red">Using List</span>
    - Which end to insert the element is good ?
        - At the end of the list (append method)
        - Reason : List is an array implementation, if we insert in beginning we need to move 
                    things. And same if we remove we need to shift everything again, that 
                    increases the time complexity.
    - pop() recommended

    Advantages/Disadvantages
        - list it is amortized O(1) . Worst case is O(n)
        - But list is cache friendly

## <span style="color:red">SLL implementation of STACK:</span>
    - It is good idea to choose head for insert/delete while implementing stack.
        - Reason : O(1) for both insert/delete
    - If we chosse LL end for insert/delete (even if we maintain tail pointer)
        - Then also Insert - O(1) But Deletion - O(n)

## [Identification of Stack Question](https://www.youtube.com/watch?v=P1bAPZg5uaE&list=PL_z_8CaSLPWdeOezg68SKkeLN4-T_jNHd):
- If you are working on array question, try to think if it can be optimized using stack
- If you get strong feeling of sorting array, then it could belong to Heap also.
- If you had to write an O(n^2) loop such that j = Fn(i), then it is 100% candidate of stack
```cpp
for (int i = 0; i < n; i++) {
    for (int j = 0; j < i; j++){
    }
}

j : 0 to i, j++
j : i to 0, j--
j : i to n, j++
j : n to i, j--

All above 4 scenarios, you can apply stack
```
```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class MyStack(self):
    def __init__(self):
        self.head = None
        self.sz = 0

    def push(self, x):
        node = Node(x)
        # Made it point to whatever head is pointing to
        node.next = self.head
        self.head = node
        self.sz += 1

    def pop(self):
        # Delete Node and return the data which is deleted
        if self.isEmpty():
            return math.inf
        else:
            res = self.head.data
            self.head = self.head.next
            self.sz -= 1
            return res

    def peek(self):
        if not self.isEmpty():
            return self.head.data
        return math.inf

    def size(self):
        return self.sz

    def isEmpty(self):
        if self.head == math.inf:
            return True
        return False

    ## Driver Code
    s = MyStack()  # top = None
    s.push(10)
    s.push(20)
    s.push(30)
    print(s.pop())
    print(s.peek())
    print(s.pop())
    print(s.size())
```

## <span style="color:red">Check for Balanced Paranthesis</span>
Time Complexity = O(n), Space Complexity = O(n)
```python
def is_matching(a, b):
    if (a == "(" and b == ")") or \
        (a == "{" and b == "}") or \
        (a == "[" and b == "]"):
        return True
    else:
        return False

def is_balanced(string):
    my_stack = []
    for char in string:
        if char in ("[","(","{"):
            my_stack.append(char)
        else:
            if not my_stack:
                return False
            stack_char = my_stack.pop()
            if not is_matching(char, stack_char):
                return False
    if stack:
        return False
    return True
```
## Infix, Postfix and Prefix Introduction
Advantages of Prefix and Postfix
- Do not require parenthesis, precedence rules and associativity rules
- Can be evaluated by writing a program that traverses the given expr exactly once

P.S: When we are converting Infix to Prefix, we need precedence and associativity rules

## Infix to Postfix using Stack
- Create empty stack, `st`
- Do following for every character x from left -> right:
- If x is:
    - operand : output it
    - left parenthesis : Push to `st`
    - right parenthesis : Pop from `st` until left parenthesis is found. Output popped operators
    - operator:
        - if `st` is Empty, push x to `st`, Else compare with `st` top
        - Higher precedence (than `st` top), push to `st`
        - Lower precedence, pop `st` top and output until a higher precedence operator is found. Then push x to `st`
        - Equal precedence, use associativity 
            - If associativity is l->r , we consider lower precedence
            - If associativity is r->l , we consider higher precedence
- Pop and output everything from `st`

- P.S : Precedence Order  ^  **>**  *, / **>** +, - **>** ( 

## Evaluation of Postfix
- Create empty stack, `st`
- Traverse through every symbol x of given postfix
    - If x is an operand, push to `st`
    - Else (x is an operator)
        - op1 = `st.pop()`
        - op2 = `st.pop()`
        - compute `op2 x op1` and push the result to `st`
    - Return `st.pop()`

## Infix to Prefix
- Create an empty stack `st`
- Create an empty string, `prefix`
- Do following for every character `C` from **right to left**
- If `C` is:
    - **Operand** : Push it to prefix
    - **Right Parenthesis** : Push to `st`
    - **Left Parenthesis** : Pop from `st` until right parenthesis is found. Append the popped character to prefix
    - **Operator** : If `st` is empty, push `C` to `st` Else compare with `st` top
        - Higher Precedence(than `st` top): Push `C` to `st`
        - Lower Precedence: Pop `st` top and append the popped item to `prefix` until a higher precedence operator is found (or `st` becomes empty). Push `C` to `st`.
        - Equal Precedence : Use Associativity
    - Pop everything from `st` and append to prefix
    - Return **`reverse of prefix`**

## Evaluation of prefix
- Create empty stack, `st`
- Traverse through every symbol x from **right to left**
    - If x is an operand, push to `st`
    - Else (x is an operator)
        - op1 = `st.pop()`
        - op2 = `st.pop()`
        - compute `op1 x op2` and push the result to `st` (**Note** op1 x op2)
    - Return `st.pop()`
