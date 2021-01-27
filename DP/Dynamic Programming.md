#### Dynamic Programming 



做DP时注意一些小细节:

1. **Variable 取名不要太没意义** D就是个很没意义的题目，试着用"longestSeq"等等

2. **建立2D的DP时注意顺序**: 一定是要从竖排到横排，不然i和j的loop时可以烦上天

3. **Base Case的建立一定要小心，注意不要用 *来Initiate Array**  

4. **先把空集 或者和长度唯一的 Case处理好，免得后期翻车** 

   

1. **Longest Common Subsequence**

**Prompt**: 寻找两个String最长的Common Subsequence

**Solution**: 设计$$D[i][j]$$ 为目前最长的Common Subseqeuence

$$D[i][j]=D[i-1][j-1] + 1$$ if $s[i]==s[j]$ else $\max \  D[i][j-1], D[i-1][j]$  

 

2. **Minimum Steps**

**Prompt**: 从index跳另外一个Index

普通的DP解法 $minSteps[i] = min D[j] + 1 $ ($0\le j<i$) , and j reachable to i

一个更好的BFS解法

```python
def jump(self, nums):
    if len(nums) <= 1: return 0
    l, r = 0, nums[0]
    times = 1
    while r < len(nums) - 1:
        times += 1
        nxt = max(i + nums[i] for i in range(l, r + 1))
        l, r = r, nxt
    return times
```

