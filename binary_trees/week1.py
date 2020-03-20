# Binary Trees 

# 1. Check if a binary tree is height balanced 
# Definition of height balance:
# if the left subtree and the right subtree does not differ 
# by more than one 

class Node:
    def __init__(self, x=None):
        self.val = x
        self.left = None
        self.right = None
    
    
def is_height_balance (node):
    if node.val == None:
        return True
    