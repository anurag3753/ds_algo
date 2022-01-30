from logging import log
from zigzag import zigzag

import logging
logging.basicConfig(filename='out.log', filemode='w')
logger=logging.getLogger()
logger.setLevel(logging.DEBUG)

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
    def __str__(self):
        return str(self.data)
    def __repr__(self):
        return str(self.data)

def indent(func):
    def wrapper(*args, **kwargs):
        func_name = func.__name__
        args_list = func.__code__.co_varnames
        var = dict(zip(args_list, args))
        logger.debug('\n' + func_name + '( ' + str(var) + ' )\n')
        result = func(*args, **kwargs)
        return result
    return wrapper


@indent
def preorder(root):
    if root is None:
        return 
    else:
        print(root.data, end = " ")
        preorder(root.left)
        preorder(root.right)

def inorder(root):
    if root is None:
        return 
    else:
        inorder(root.left)
        print(root.data, end = " ")
        inorder(root.right)

def postorder(root):
    if root is None:
        return 
    else:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end = " ")


if __name__ == "__main__":
    root = Node(10)
    root.left = Node(3)
    root.right = Node(4)
    root.left.right = Node(9)
    root.right.left = Node(5)
    root.right.right = Node(6)

    preorder(root)
    # print()
    # inorder(root)
    # print()
    # postorder(root)
    # print(zigzag(root))

# res is a global variable. Is there any way I can avoid it. When running on multiple-tcs it is producing incorrect result.
# I took the C++ code and trying to covert it to relevant Python Code. But in C++, we can receive args via reference. Hence no problem in C++.
# HOW TO RESOLVE SAME PROBLEM in Python ??
res = 0

def diameterHelper(self,root):
    global res
    # Code here
    if root is None:
        return 0
    leftdiameter = self.diameterHelper(root.left)
    rightdiameter = self.diameterHelper(root.right)
    
    temp = max(leftdiameter, rightdiameter) + 1
    ans = max(temp, 1+leftdiameter+rightdiameter)
    res = max(res, ans)
    
    return temp
    
def diameter(self,root):
    global res
    self.diameterHelper(root)
    temp = res
    res = 0
    return temp


struct Node
{
    int data;
    struct Node* left;
    struct Node* right;

    Node(int x){
        data = x;
        left = right = NULL;
    }
};

int diameterHelper(Node* root, int &res) {
    if (root == Null) {
        return 0;
    }
    
    int leftdiameter = diameterHelper(root->left);
    int rightdiameter = diameterHelper(root->right);

    int temp = max(leftdiameter, rightdiameter) + 1;
    int ans = max(temp, 1 + leftdiameter + rightdiameter);
    res = max(res, ans);

    return temp;
}

int diameter(Node* root){
    int res = 0;
    diameterHelper(root, res);
    return res;     # It contains the actual answer
}
