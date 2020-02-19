## 1. DFS 

1.1 Minimum Depth of Binary Tree
Level: Easy
Given a binary tree, find its minimum depth.

**The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.**

Note: A leaf is a node with no children.

#### Solution 
```
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root == None: # Empty Node
            return 0 
        if root.left == None or root.right == None: # No Child.
            return 1 + self.minDepth(root.left) + self.minDepth(root.right)
        return 1 + min (self.minDepth(root.left), self.minDepth(root.right))
```
        
#### Explanation:
This is not a classical DFS problem. The basic logic is use recursion to calculate  
``` 
1 + min (self.minDepth(root.left), self.minDepth(root.right)) [1]
```
However, since the definition of minimum depth is different, we have to add a new case:
Looking at three cases: 
1. Empty Node
2. Either right or left child is empty, thus the minimum depth of the subtree
will **not** take the minimum depth of the left and right. Instead, it will always take 
the "maximum" (non-empty path)
3. If both children aren't empty, then apply the logic [1]. 