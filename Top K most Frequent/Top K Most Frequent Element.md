# Top K Elements

Top K Element 一般属于

- Find K Largest Element,
- Find Top K Smallest Elements
- Find K most Frequent Element

一般针对这种题型，Heap的使用至关重要

### 1. Top K Largest Element

从Array里找K最大。一般的算法会用Sorting，然后直接[:k]来找k最大的，这样的runtime是nlogn，内存也是n

另一个经典算法是建立一个size k的heap，然后每次新加入的Element要比heap最小的大时，

1. 将最小的取出
2. 将新的放入 

runtime大概是 建立heap的k，以及insert pop的logk，总共需要 n-k步

O(k) + O((n-k) log k) → O(n logk)

### 2. Kth Smallest Element

从一个Array里找k最小的。一般的算法依旧是NlogN

用heap的话，建立heap需要O(k), Insert & Pop O( (n-k) log k ) = O(nlogk ) 最后取出最小的就可以了。这里用max heap是会更合适，在max heap里都是比top要小的数

### 3. K closest point to the origin

Prompt: Given an array of 2D points, find the K closest points to the origin (0,0)

Brute Force: Find distance, create new data structure to store the distance and the points, then sort and produce the best results (n log n ) 

用heap依旧可以解决这个问题，储存一个maxheap，size为k，可以在N log K 的时间里解决问题

### 4. Connect Ropes

Given an array of ropes, return the minimum cost to connect them together. The cost is equivalent to the sum of the length of individual ropes. 

```json
[1,3, 11,5] => 33 
// 1 + 3 = 4, 4 + 5 = 9, 9 + 11 = 20 
// total cost = 4 + 9 + 20 = 33 
```

感觉有点像一个conenct string 的问题，240的string decode，应该每次都conenct最小的两个，因为更长的string在之后的cost会不断的被使用，所以一定要用最小的string，常规思路就是用一个heap来存最小的数字，然后每次拿走最小的两个，然后放回minheap

Constructing the heap will take O(n) amount of time. Insert/Pop N element will take O(log N) time, since each combination will reduce the elements exactly by 1, so the total runtime would be O(nlogn) 

### 5. Top K most frequent elements

我的思路是，先用collections，use collections to combine the items in O(n) time. Then construct a heap in O(k) size, does insert and pop algorithm that reduces the runtime to standard O(N log K) 

**6. Frequency Sort** 

Given a string, sort the string in decreasing frequency of its characters. 

这道题的方法就多了。用之前的collections Counter + heap的话，大概的runtime是

O(n) + O(DlogD) where D is the number of distinct characters . Worst case can be O(N LOG N). Where we have N distinct characters. 

Besides, using bucket sort may work too. So use a hashmap. of constant size (limited by the maxfrequency F ≤ n) so O (26) time to create the constant map, and then create this maxfrequency O(F) ≤ O(N) bucket list of frequency count. Then we can iterate through this bucket and output. O(N*N) since we can have all letters of the same length. Worst case is pretty bad. But realistically it's very rare.

 

### 7. Kth Largest Element in a data stream

Build minHeap, size k. It's going to take log(K) time to update each time we see a new number. 

### 8. *K Closest Number

Given a **sorted** number array and two integers K and X, find k closest number to X. Return the numbers in sorted order. 

1. Center the array around X 
2. Reduce the problems to K smallest. 
3. N log K 

1. 更好的解决方法是先使用binary search，先找到最接近x的数字，然后以y为中心，将左右k个的数字放入(distance, element) pair放入 min Heap进行update，然后取出最小的k个

这样的话，runtime就只需要 O(logK ) + ( k log K)

2. 另外一个是用two pointer，找到Y以后两个pointer左右开工，看一下谁能先找到下一个最小的，然后放入Queue。这样O(k) 就可以搞定了

### 9. Maximum Distinct Element

Given an array and K elements. Remove K elements such that we are left with maximum number of distinct elements. We want to delete **Non disctinct wth least frequency** 

1. Use collection convert into a frequency counter 
2. Convert into minheap 
3. Greedily delete 

O(n) + O(D) + k O( N log N)

### 10. Find Sum of all numbers between k1th and k2th smallest number of that array:

Trivial. Similar to k most frequent

### 11. Rearrange String

Given a string, find if its letters can be rearranged in such a way that no two same characters come next to each other.

```python
Input: "aappp"
Output: "papap"
Explanation: In "papap", none of the repeating characters come next to each other
```

- Like the task scheduler problem: with cool down set to 1

This problem follows the [Top ‘K’ Numbers](https://www.educative.io/collection/page/5668639101419520/5671464854355968/5728885882748928/) pattern. We can follow a greedy approach to find an arrangement of the given string where no two same characters come next to each other.

We can work in a stepwise fashion to create a string with all characters from the input string. Following a greedy approach, we should first append the most frequent characters to the output strings, for which we can use a **Max Heap**. By appending the most frequent character first, we have the best chance to find a string where no two same characters come next to each other.

O(N log N)

hao