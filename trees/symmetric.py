from collections import deque

import logging
logging.basicConfig(filename='out.log', filemode='w')
logger=logging.getLogger()
logger.setLevel(logging.DEBUG)

def indent(func):
    def wrapper(*args, **kwargs):
        func_name = func.__name__
        args_list = func.__code__.co_varnames
        var = dict(zip(args_list, args))
        logger.debug('\n' + func_name + '( ' + str(var) + ' )\n')
        result = func(*args, **kwargs)
        return result
    return wrapper

#User function Template for python3
from collections import deque


def isSymmetric(root):
    # Your Code Here
    if root is None:
        return True
    queue = deque()
    queue.append(root.left)
    queue.append(root.right)
    while queue:
        left = queue.popleft()
        right = queue.popleft()
        
        if left is None and right is None:
            continue
        if (left is None and right is not None) or \
            (left is not None and right is None):
                return False
        
        if left.data != right.data:
            return False
            
        queue.append(left.left)
        queue.append(right.right)
        queue.append(left.right)
        queue.append(right.left)
        
    return True

@indent
def isSymmetricRec(root1, root2):
    print(f"root1 : {root1} , root2 : {root2}")
    if root1 is None and root2 is None:
        return True
    if root1 is None or root2 is None:
        return False
    
    if root1.data == root2.data:
        return  isSymmetricRec(root1.left, root2.right) and isSymmetricRec(root1.right, root2.left)

    return False





# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

    def __str__(self):
        return str(self.data)
    def __repr__(self):
        return str(self.data)   
    
if __name__=="__main__":
    # t=int(input())
    # for _ in range(0,t):
    #     s=input()
    #     root=buildTree(s)
    #     ob = Solution()
    #     if ob.isSymmetric(root):
    #         print("True")
    #     else:
    #         print("False")
        
    root = Node(1)
    root.left = Node(2)
    root.right = Node(2)
    root.left.left = Node(3)
    root.left.right = Node(4)
    root.right.left = Node(4)
    root.right.right = Node(3)
    print(isSymmetricRec(root, root))
        

# } Driver Code Ends