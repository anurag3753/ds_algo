# ds_algo
This repository contains notes related to data structures and algorithms using python
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
    <li> using our own implementation </li>
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

Advantages/Disadvantages <br>
    - list it is amortized O(1) . Worst case is O(n) <br>
    - But list is cache friendly