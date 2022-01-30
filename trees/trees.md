# Trees

## DP on Trees 

[Identification](https://www.youtube.com/watch?v=qZ5zayHSH2g&list=PL_z_8CaSLPWfxJPz2-YKqL9gXWdgrhvdn&index=2):
- Normal tree traversal complexity is O(n)
- If you find that in a particular tree question you, need to do certain work for every tree node. It is an indication that you should apply DP, otherwise your TC ~ O(n^2)


[General Syntax for DP on Trees](https://www.youtube.com/watch?v=d1u2t018Kjg&list=PL_z_8CaSLPWfxJPz2-YKqL9gXWdgrhvdn&index=2):
```python
global res
res = -math.inf                  # Equivalent to INT_MIN
def solve(root):
    # Base Condition
    if root is None:
        return 0
    
    # Hypothesis
    l = solve(root.left)
    r = solve(root.right)

    # Induction
    ##temp = calculate_temp_answer
    temp = 1 + max(l, r)         # For diameter question
    ans = max(temp, relation)    # relation will tell if this guy could be answer or not
    res = max(res, ans)          

    return temp                  # You may not be answer, so just pass your value upwards


## Driver Code
solve()
print(f"Final answer is {res}")  # `res` stores the final answer
```
### Tips
- We need to solve it without using the global var in python
- [leetcode](https://leetcode.com/problems/diameter-of-binary-tree/)

## LEETCODE SOLUTION FOR Diameter of a Binary Tree
- Way 1
```python
class Solution:
    
    def diameterHelper(self,root, res):
        # Code here
        if root is None:
            return 0, res
        l, res1 = self.diameterHelper(root.left, res)
        r, res2 = self.diameterHelper(root.right, res)
        
        res = max(res1, res2)
        temp = max(l, r) + 1
        ans = max(temp, 1+l+r)
        res = max(res, ans)
        
        return temp, res
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        temp, res = self.diameterHelper(root, res)
        return res-1
```
- Way 2
```python
## GFG : https://practice.geeksforgeeks.org/problems/diameter-of-binary-tree/1
## LEETCODE : https://leetcode.com/problems/diameter-of-binary-tree/submissions/
class Solution:
    
    def diameterHelper(self,root, res):
        # Code here
        if root is None:
            return 0
        l = self.diameterHelper(root.left, res)
        r = self.diameterHelper(root.right, res)
        
        temp = max(l, r) + 1
        ans = 1+l+r
        if ans > res[0]:
            res[0] = ans
        return temp
    
    def diameter(self, root):
        result = [-99999999999]
        tempans = self.diameterHelper(root, result)
        # if the tree is skewed
        if result[0] == -99999999999:
            return tempans
        else:
            return result[0]
```

## GFG SOLUTION FOR Maximum Path Sum between 2 Leaf Nodes
```python
class Solution:
    
    def maxPathSumHelper(self, root, res):
        # code here
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return root.data
        
        left = self.maxPathSumHelper(root.left, res)
        right = self.maxPathSumHelper(root.right, res)
        
        if root.right is None:
            return root.data + left
            
        if root.left is None:
            return root.data + right
        
        temp = max(left, right) + root.data
        ans = left + right + root.data
        if ans > res[0]:
            res[0] = ans
        return temp
        
    def maxPathSum(self, root):
        res = [-999999999]
        tempans = self.maxPathSumHelper(root, res)
        if res[0] == -999999999:
            return tempans
        else:
            return res[0]
```
## Maximum path sum from any node
```python

## https://leetcode.com/problems/binary-tree-maximum-path-sum/submissions/
    def maxPathSumHelper(self, root, res):
        if root is None:
            return -999999999
        
        left = self.maxPathSumHelper(root.left, res)
        right = self.maxPathSumHelper(root.right, res)
        
        temp = max(max(left, right) + root.val, root.val)
        ans = max(left + right + root.val, root.val, left+root.val, right + root.val)
        if ans > res[0]:
            res[0] = ans
        return temp

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [-999999999]
        tempans = self.maxPathSumHelper(root, res)
        if res[0] == -999999999:
            return tempans
        else:
            return res[0]
```



Problems Based on DP on Trees: <br>
- Diameter of Binary tree
    - [gfg](https://www.geeksforgeeks.org/diameter-of-a-binary-tree/)
    - [youtube](https://www.youtube.com/watch?v=zmPj_Ee3B8c&list=PL_z_8CaSLPWfxJPz2-YKqL9gXWdgrhvdn&index=3)
- Maximum Path Sum in a Binary Tree
    - [gfg](https://www.geeksforgeeks.org/find-maximum-path-sum-in-a-binary-tree/)
    - [youtube](https://www.youtube.com/watch?v=Osz-Vwer6rw&list=PL_z_8CaSLPWfxJPz2-YKqL9gXWdgrhvdn&index=4)
- Maximum path sum between two leaves of a binary tree
    - [gfg](https://www.geeksforgeeks.org/find-maximum-path-sum-two-leaves-binary-tree/)
    - [youtube](https://www.youtube.com/watch?v=ArNyupe-XH0&list=PL_z_8CaSLPWfxJPz2-YKqL9gXWdgrhvdn&index=5)