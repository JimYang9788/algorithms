### Binary Tree

1. **Validate Binary Tree**

**Test Point:** Understand the logic of Binary Search Tree 

**易错点** 不能单单检查每个Node的Validility，需要知道上下限

**Source:** Leetcode Q98

O(n) | O(1)

```python
class Solution(object):
    def isValidBST(self, root, lessThan = float('inf'), largerThan = float('-inf')):
        if not root:
            return True
        if root.val <= largerThan or root.val >= lessThan:
            return False
        return self.isValidBST(root.left, min(lessThan, root.val), largerThan) and \
               self.isValidBST(root.right, lessThan, max(root.val, largerThan))
```





2. 