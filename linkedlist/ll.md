# Linked List

Each node contains reference to next node. It is a linear data structure. <br>

#### Advantages
    - Ease of insertion/deletion

#### Disadvantages
    - No random access
    - No cache friendliness

## Linked List Node Structure

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
```

## Applications of Linked List
- Worst case insertion at end and begin are O(1)
- Worst case deletion from beginning is O(1)
- Insertion and Deletions in the middle are O(1) if we have reference to the previous node
- Round Robin Implementation (Infact circular linked list is precisely used for this purpose)
- Merging two sorted linked lists is faster than arrays
- Implementation of simple memory manager where we need to link free blocks
- Easier implemantation of Queue and Deque data structure

## Recursively Reverse Linked List
```python
def reverseList(curr, prev=None):
    if curr is None:
        return prev
    nextnode = curr.next
    curr.next = prev
    return reverseList(nextnode, curr)
```

## Detect Loop in LL (Floyd’s Cycle-Finding Algorithm)
```python
def detectLoop(head):
    slow_p = head
    fast_p = head
    while(slow_p and fast_p and fast_p.next):
        slow_p = slow_p.next
        fast_p = fast_p.next.next
        if slow_p == fast_p:
            return True
    return False
```
## Merge Two Sorted Lists (Recursive)
```python
def merge_two_sll(head1, head2):
    if head1 is None:
        return head2
    if head2 is None:
        return head1

    if head1.val < head2.val:
        head1.next = merge_two_sll(head1.next, head2)
        return head1
    else:
        head2.next = merge_two_sll(head1, head2.next)
        return head2
```
## Tips
- Python does not have tail call elimination

## Must Do Programming Questions
- [merge-two-sorted-linked-lists](https://www.geeksforgeeks.org/merge-two-sorted-linked-lists/)
    - Create a dummy node
    - Recursive Solution

- [reverse-a-linked-list](https://www.geeksforgeeks.org/reverse-a-linked-list/)
    - Iterative way
    - Recursive way

- [add-two-numbers-represented-by-linked-lists](https://www.geeksforgeeks.org/add-two-numbers-represented-by-linked-lists/)
    - Using Stack as Data Structure
    - Reverse Both Lists, Add nodes iteratively, reverse the resultant list. T.C = O(n) , S.C. = O(1) [url](https://www.geeksforgeeks.org/add-two-numbers-represented-by-linked-lists-set-3/?ref=lbp)

- [finding-middle-element-in-a-linked list](https://www.geeksforgeeks.org/write-a-c-function-to-print-the-middle-of-the-linked-list/)
    - Count nodes. Compute nodes/2. Return node->data at count/2 location
    - use slow_ptr and fast_ptr

- [check-if-linked-list-is-palindrome](https://www.geeksforgeeks.org/function-to-check-if-a-singly-linked-list-is-palindrome/)
    - 3 ways
    - 1 :- use stack, 2:- use recursion, 3:- reverse_list from middle and then compare 2 lists. Recreate original list in end
- 
