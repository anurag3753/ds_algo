from collections import deque
# import logging
# logging.basicConfig(filename="out.txt")

def print_queue(queue):
    # res = []
    for ele in queue:
        print(ele.data, end = " ")
    print()

def zigzag(root):
    if root is None:
        return []
    else:
        queue = deque()
        queue.append(root)
        i = 0
        res = []
        while (queue):
            node_count = len(queue)
            print("**************************************************************")
            print(" i : ", i)
            print_queue(queue)
            # print("**************************************************************")
            for code in range(node_count):
                if i%2 == 0:
                    # even traversal
                    node = queue.pop()
                    res.append(node.data)
                    if node.right:
                        queue.appendleft(node.right)
                    if node.left:
                        queue.appendleft(node.left)
                else:
                    # odd traversal
                    node = queue.pop()
                    res.append(node.data)
                    if node.left:
                        queue.appendleft(node.left)
                    if node.right:
                        queue.appendleft(node.right)
            i += 1
        return res