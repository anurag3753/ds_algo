# HEAP DS

```python
import heapq               # It implements min-heap

pq = [5, 20, 1, 30, 4]
heapq.heapify(pq)
print(pq)                  # [1,4,5,30,20]
heapq.heappush(pq, 3)
print(pq)                  # [1,4,3,30,20,5]   
print(heapq.heappop(pq))   # [3,4,5,30,20]

heapq.nlargest(2, pq)      # provides 2 largest elements from heap
heapq.nsmallest(2, pq)     # provides 2 smallest elements from heap

# Creating empty heap
heap = []
heapq.heapify(heap)

# To access the smallest item without popping it, use 
print(heap[0])
```

