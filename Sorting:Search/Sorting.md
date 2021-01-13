#### Sorting/Search 

1. **Median of Two Sorted Array**

$O(log(m+n)) | O(1)$

解题思路: 解题思路就是median的对比，然后进行筛选

1. 将小于小Median的去掉，
2. 将大于大Median的去掉

```python
class Solution:
    def findMedianSortedArrays(self, A, B):
        l = len(A) + len(B)
        if l % 2 == 1:
            return self.kth(A, B, l // 2)
        else:
            return (self.kth(A, B, l // 2) + self.kth(A, B, l // 2 - 1)) / 2.   

    def kth(self, a, b, k):
        if not a:
            return b[k]
        if not b:
            return a[k]
        ia, ib = len(a) // 2 , len(b) // 2
        ma, mb = a[ia], b[ib]

        # when k is bigger than the sum of a and b's median indices 
        if ia + ib < k:
            # if a's median is bigger than b's, b's first half doesn't include k
            if ma > mb:
                return self.kth(a, b[ib + 1:], k - ib - 1)
            else:
                return self.kth(a[ia + 1:], b, k - ia - 1)
        # when k is smaller than the sum of a and b's median indices
        else:
            # if a's median is bigger than b's, a's second half doesn't include k
            if ma > mb:
                return self.kth(a[:ia], b, k)
            else:
                return self.kth(a, b[:ib], k)
```

```

```





2. Binary Search with Range 

```python
def searchForRange(array, target):
	
	def binarySearch (array, target, curRange, goLeft):
		l,r = 0, len(array) -1 
		while (l <= r):
			m = (l + r) // 2
			if target > array[m]:
				l = m + 1 
			elif target < array[m]:
				r = m - 1
			else:
				if goLeft:
					if m == 0 or array[m-1] != target:
						curRange[0] = m 
						return 
					else:
						r = m - 1 
				else:
					if m == len(array)-1 or array[m+1] != target:
						curRange[1] = m
						return 
					else:
						l = m + 1 

	curRange = [-1,-1]
	binarySearch (array, target, curRange,0)
	
	binarySearch (array, target, curRange, True)
	binarySearch (array, target, curRange,False)
	return curRange
```



3. First Index = Value 

```python
def indexEqualsValue(array):
    # Write your code here.
    l,u = 0, len(array)-1
	res = -1 
	while (l <= u):

		m = (l + u) // 2 
		
		if array[m] > m:
			u = m - 1 
		elif array[m] < m:
			l = m + 1 
		else:
			if m - 1 < 0 or array[m-1] != m - 1:
				return m
			else:
				res = m 
				u = m - 1	
	return res 

```

