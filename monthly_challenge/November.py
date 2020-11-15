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

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        # two get pointers for nums1 and nums2
        p1 = m - 1
        p2 = n - 1
        # set pointer for nums1
        p = m + n - 1
        
        # while there are still elements to compare
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] < nums2[p2]:
                nums1[p] = nums2[p2]
                p2 -= 1
            else:
                nums1[p] =  nums1[p1]
                p1 -= 1
            p -= 1
        
        # add missing elements from nums2
        nums1[:p2 + 1] = nums2[:p2 + 1]


class Solution:
    def countPrimes(self, n):
        if n < 3:
            return 0
        primes = [True] * n
        primes[0] = primes[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if primes[i]:
                primes[i * i: n: i] = [False] * len(primes[i * i: n: i])
        return sum(primes)

class Solution:
    def hammingWeight(self, n: int) -> int:
        sum_total = 0
        while (n!=0):
            sum_total += 1 
            n &= n - 1 
        return sum_total


        def hammingWeight(int n):
            bits = 0;
            mask = 1;
            for (i = 0; i < 32; i++) {
                if ((n & mask) != 0) {
                bits++;
            }
            mask <<= 1;
    }
    return bits;
}


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total_length = len(nums) + 1 
        total_sum = (0 + total_length - 1) * total_length / 2 
        
        return int (total_sum - sum (nums))

class Solution:

    
    def hammingDistance(self, x: int, y: int) -> int:

        return bin(x ^ y).count('1')


class Solution:

    def generate(self, numRows: int) -> List[List[int]]:
        n = numRows
        if n == 0:
            return []
        elif n == 1:
            return [[1]]
        elif n == 2:
            return [[1],[1,1]]

        prev_res = self.generate (n-1)
        prev_row = prev_res[-1]
        cur_row = [1] * n
        for i in range (n):
            if i == 0 or i == n - 1:
                continue
            else:
                cur_row[i] = prev_row[i] + prev_row [i-1]
        
        prev_res.append (cur_row)
        return prev_res 