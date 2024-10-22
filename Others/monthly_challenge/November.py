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


class Solution:
    def set_row(self, target, matrix):
        print ('begin: target',target, matrix)
        for idx,row in enumerate(matrix):
            if idx == target:
                for j, val in enumerate(matrix[idx]):
                    print (matrix[idx][j])
                    matrix[idx][j] = 0
        print ("end",target, matrix)
    
    def set_col(self, j, matrix):
        for row in matrix:
            for idx, val in enumerate (matrix):
                if idx == j:
                    row[idx] = 0
        
        
class Solution:

        
        
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row_set = set()
        col_set = set()
        for i,row in enumerate (matrix):
            for j,cell in enumerate (row):
                if cell == 0:
                    row_set.add(i)
                    col_set.add(j)
        
        # Iterate again 
        for i,row in enumerate (matrix):
            for j,cell in enumerate (row):
                if i in row_set or j in col_set:
                    matrix[i][j] = 0
                

class Solution:
    def is_palindrome (self, s):
        while s:
            if len (s) == 1:
                return True
            elif s[0] == s[-1]:
                s = s[1:-1]
            else:
                return False     
        return True
        
    def longestPalindrome(self, s: str) -> str:
        cur_max = ""
        for i in range (0, len(s)+1):
            for j in range (i, len(s)+1):
                if len(s[i:j]) > len(cur_max) and self.is_palindrome(s[i:j]):
                    cur_max = s[i:j]
                    
        return cur_max 
                

## Wrong Solution

class Solution:
    def find_max(self,target,nums, D):
        max_so_far = -1 
        for i,n in enumerate (nums):
            if target > n:
                print (target, n)
                max_so_far = D[i] + 1 
        return max_so_far 
    
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) <= 2: return False 
        
        D = [0] * len(nums)
        D[0] = 1 
        max_so_far = 1 
        for i, val in enumerate(nums):
            if i == 0: 
                continue 
            D[i] = max (max_so_far, self.find_max(val,nums[:i],D))
            max_so_far = max(max_so_far, D[i])
        print (D)
        return D[-1] >= 3 
    
    def increasingTriplet(nums):
        first = second = float('inf')
        for n in nums:
            if n <= first:
                first = n
            elif n <= second:
                second = n
            else:
                return True
        return False


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        dummy1 = odd = ListNode(0)
        dummy2 = even = ListNode(0)
        while head:
            odd.next = head
            even.next = head.next
            odd = odd.next
            even = even.next
            head = head.next.next if even else None
        odd.next = dummy2.next
        return dummy1.next
        
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        hash_set = {}
        dummy1 = headA 
        dummy2 = headB
        while (dummy1):
            hash_set [dummy1] = 1
            dummy1 = dummy1.next 
            
        while (dummy2):
            if dummy2 in hash_set:
                return dummy2 
            dummy2 = dummy2.next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """ 
        if not headA or not headB: return None

        p = headA
        while p.next:
            p = p.next
        mark = p
        #make a cycled list
        mark.next = headA

        rst = None
        p1 = headB
        p2 = headB
        while p1 and p2:
            p1 = p1.next
            p2 = p2.next
            if p2: p2 = p2.next
            if p1 == p2: break

        if p1 and p2 and p1 == p2:
            p1 = headB
            while p1 != p2:
                p1 = p1.next
                p2 = p2.next
            rst = p1

        #unmake the cycle
        mark.next = None

        return rst


if __name__ == '__main__':
    zeros = Solution.setZeroes([[1,1,1],[1,0,1],[1,1,1]])
