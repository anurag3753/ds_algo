# DLL

Every node has reference to both prev and next.

###  <span style="color:red">Basic Node Structure</span>

```python
Class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
```

## <span style="color:red">SLL Vs DLL</span>

<b>DLL Advantages:</b>
    <ol>
        <li>
            Can be traversed in both directions.
            From any node be can traverse in both directions. <br>
            Ex. Managing edit history in an editor Or browser history in browser.
                Here, you need to do back-back-back and vice-versa
        </li>        
        <li> 
            A given node can be deleted in O(1) time with given reference/pointer to it.
        </li>
        <li>
            Insert/Delete before a given node in O(1) time. In SLL Insert/Delete after a given node is allowed in O(1) time but before one is not allowed. 
        </li>    
        <li>
            Insert/Delete from both ends in O(1) time by maintaing tail. (All 4 operations in O(1) time)
        </li>
        <li>
            Data Structure "Deque" allows you to add/delete at both ends.
        </li>
    </ol>


<b>DLL Disadvantages:</b>
    <ol>
        <li> Extra Space for prev </li>
        <li> Code becomes complex </li>
    </ol>

## <span style="color:red">Insert at Beginning of DLL</span>
```python
def insertBegin(head, x):
    temp = Node(x)
    if head is not None:
        head.prev = temp
    temp.next = head
    return temp
```
## <span style="color:red">Insert at End of DLL</span>
```python
def insertEnd(head, x):
    temp = Node(x)
    head_copy = head
    if head is None:
        return temp
    while head_copy.next is not None:
        head_copy = head_copy.next
    head_copy.next = temp
    temp.prev = head_copy
    return head
```
## <span style="color:red">Delete First Node of DLL</span>
```python
def deleteFirst(head):
    if head is None or head.next is None:
        return None
    head = head.next
    head.prev = None
    return head
```
## <span style="color:red">Delete Last Node of DLL (Can be done in O(1) time if we maintain tail ptr)</span>
```python
def deleteLast(head):
    if head is None or head.next is None:
        return None
    temp = head
    while (temp.next.next is not None):
        temp = temp.next
    temp.next = None
    return head
```
## <span style="color:red">Reverse a Doubly Linked List (The core idea is prev and next ptr gets interchanged)</span>
```python
def reverseDLL(head):
    if head is None or head.next is None:
        return head
    curr = head
    prev = None
    while curr is not None:
        curr.next, curr.prev = curr.prev, curr.next
        curr = curr.prev
    return prev
```