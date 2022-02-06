## Arrays

### 1. 思路ToolBox

Array的一些常用思路



**a).  Sorting ** 

Sorting 可以带来的Benefit很多，尤其是对于return index不相关的问题，可以给Two Pointer带来理想的作用

实用于: Two Sum, Three Sum, K Sum 等等

**b). Index as hashmap**

当题目里有1,2...n的时候，index作为hashmap就可以实用了，(想想index sort)，这是一种特殊的骚操作提醒，可以用Finding Duplicate (仅限于1....n)，或者Finding Missing Range (利用整除的性质去recover missing 的数字)

```python
array[array[i]%n] += n  # 强大的整除性质来recover missing range
```

适用于Finding Duplicate, Finding Missing Range

**c)**. **Using a stack** 

适用于 Calculator等问题 (Parsing)

**d) Floyd Tortoise and Hare Algorithm** 

同样适用于finding duplicate的问题。虽然Tortoise and hare最初是用于linkedlist找cycle的，但是这个题目也可以被reduce成finding duplicate的题型

```python
# Given an array of integers nums containing n + 1 integers
# where each integer is in the range [1, n] inclusive.

# Input: nums = [1,3,4,2,2]
#  Output: 2

There is only one duplicate number in nums, return this duplicate number.


class Solution:
    def findDuplicate(self, nums):
        # Find the intersection point of the two runners.
        tortoise = hare = nums[0]
        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                break
        
        # Find the "entrance" to the cycle.
        # In phase 2, we give the tortoise a second chance
        # by slowing down the hare, so that it now moves
        # with the speed of tortoise: tortoise = nums[tortoise],
        # hare = nums[hare]. The tortoise is back at the starting 
        # position, and the hare starts from the intersection point.
        tortoise = nums[0]
        while tortoise != hare:
            tortoise = nums[tortoise]
            hare = nums[hare]
        
        return hare
```



**e) Running Sum/ Running Product**

适用于Product of Array

