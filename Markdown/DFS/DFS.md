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


1.3 Decode String 
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

Examples:
```
s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".
```

Solution
```
class Solution:
	def decodeString(self, s):
		if not s or len(s) == 0:
			return s
		result, position = self.dfs(0,s,0,'')
		return result

	def dfs(self, position, s, prev_num, prev_str):
		while position < len(s):
			while s[position].isdigit():
				prev_num  = prev_num*10 + int(s[position])
				position += 1

			if s[position] == "[":
				#reset the prev_str
				returned_str, ending_pos = self.dfs(position+1, s, prev_num=0, prev_str="")
				#backtrack
				prev_str = prev_str + returned_str*prev_num
				position = ending_pos
				prev_num = 0
			#return the result
			elif s[position] == ']':
				return prev_str, position
			else:
				prev_str += s[position]
			position += 1
		return prev_str, position
```