# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        level = []
        if root:
            level.append(root)
        while level:
            push_list = []
            for node in level:
                if node:
                    push_list.append (node.val)
            if push_list != []:
                res.append (push_list)
            next_level = []
            for node in level:
                if node:
                    next_level.append (node.left)
                    next_level.append (node.right)
            level = next_level 
        return res 