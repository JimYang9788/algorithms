#### Backtracking 


Backtracking is an algorithmic-technique for solving problems recursively by trying to build a solution incrementally, one piece at a time, removing those solutions that fail to satisfy the constraints of the problem at any point of time (by time, here, is referred to the time elapsed till reaching any level of the search tree).

**Generic Template:**

```python
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(tmplist,first):
          	# 到头了撤退
            if len(tmplist) == k:
                output.append(tmplist[:])
            # 找所有解题思路
            for i in range(first,n):
              	# 给出新解答
                tmplist.append(nums[i])
                # 继续backtrack
                backtrack(tmplist,i+1)
                # 不用这个解答继续
                tmplist.pop()
        
        n = len(nums)
        output = []
        tmplist = []
        for k in range(0,n+1):
            # Loop through all subset length 
            backtrack(tmplist, 0)
            
        
        return output 

```

