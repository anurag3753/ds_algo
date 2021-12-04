# Circular Linked List

## Advantages
    - We can traverse whole list from any node
    - Implementation of algorithms like round-robin
    - We can insert at the beginning and end by just maintaining one tail reference/pointer
        - This property can be used to implement queue data structure (insert at end, remove from beginning)
        Delete from Beginning       - O(1)
        Insert at the End           - O(1)
        Insert at the Beginning     - O(1)

## Disadvantages
    - Implementation of operations become complex
        - Code for cll traversal is also little complex, same true with rest operations also.

## Traversal OF CLL (VVIMP)
```python
def printCircular(head):
    if head is None:
        return
    print(head.data, end = " ")
    curr = head.next
    while curr != head:
        print(curr.data)
        curr = curr.next
```

## Insert at Beginning of CLL
Time Complexity : O(n)
```python
def insert_at_begin(head, data):
    node = Node(data)
    if head is None:
        node.next = node
        return node
    head_copy = head
    while head_copy.next != head:
        head_copy = head_copy.next
    head_copy.next = node
    node.next = head
    return node
```
Time Complexity : O(1)
```python
Tricky Solution

def insert_at_begin(head, data):
    node = Node(data)
    if head is None:
        node.next = node
        return node
    # insert after head
    node.next = head.next
    head.next = node
    # swap head and head.next data
    head.data, node.data = node.data, head.data
    return head
```

## Insert at END of CLL
Time Complexity : O(n)
```python
def insert_at_end(head, data):
    node = Node(data)
    if head is None:
        node.next = node
        return node
    # insert at end
    head_copy = head
    while head_copy.next != head:
        head_copy = head_copy.next
    node.next = head
    head_copy.next = node
    return head
```
Time Complexity : O(1)
```python
Tricky Solution

def insert_at_end(head, data):
    node = Node(data)
    if head is None:
        node.next = node
        return node
    # insert after head
    node.next = head.next
    head.next = node
    # swap head and head.next data
    head.data, node.data = node.data, head.data
    return head.next    # THIS IS THE TRICK    
    # OR
    return node # node is new HEAD
```

## Delete HEAD of CLL
Time Complexity : O(n)
```python
def delete_head(head):
    if head is None or head.next == head:
        return None
    curr = head
    while curr.next != head:
        curr = curr.next
    curr.next = head.next
    return head.next
```
Time Complexity : O(1)
```python
def delete_head(head):
    if head is None or head.next == head:
        return None
    # copy data from head.next to head
    # Then delete head.next, works only for >=2 nodes in LL
    head.data = head.next.data
    head.next = head.next.next
    return head
```

## Delete K<sup>th</sup> Node of CLL (Numbering starts with 1)
Time Complexity : O(k)
```python
def delete_kth_node(head, k):
    if head == None:
        return head
    elif k == 1:
        return delete_head(head)
    else:
        curr = head
        for i in range(k-2):
            curr = curr.next
        curr.next = curr.next.next
        return head
```