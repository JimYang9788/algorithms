
# Friend Cycle 

There are N students in a class. Some of them are friends, while some are not. Their friendship is transitive in nature. For example, if A is a direct friend of B, and B is a direct friend of C, then A is an indirect friend of C. And we defined a friend circle is a group of students who are direct or indirect friends.

Given a N*N matrix M representing the friend relationship between students in the class. If M[i][j] = 1, then the ith and jth students are direct friends with each other, otherwise not. And you have to **output the total number of friend circles** among all the students.

Example 1:

```
[[1,1,0],
 [1,1,0],
 [0,0,1]]
```

Note:
N is in range [1,200].
M[i][i] = 1 for all students.
If M[i][j] = 1, then M[j][i] = 1.

Solution 

```
class Solution:
    count = 0
    def findCircleNum(self, M: List[List[int]]) -> int:
        for i,val in enumerate(M):
            if  M[i][i] != 2:
                self.DFS (M, i)
                self.count += 1 
        return self.count 
  
    def DFS (self, M, i):
        if M[i][i] == 2:     
            return
        M[i][i] = 2
        
        # For M[i]'s neighbour
        for j,val in enumerate(M[i]): 
            if M[i][j] == 1:
                self.DFS (M, j)

```

Explanation:
Classical DFS. It's kind of like the island finder problem. 
