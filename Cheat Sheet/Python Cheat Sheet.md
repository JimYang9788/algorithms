### Python Cheat Sheet

### 1.16 QUEUE/HEAPQ

| Name                | Comment                                                      |
| :------------------ | :----------------------------------------------------------- |
| Initialize min heap | `heapq.heapify(q)`                                           |
| heappush a tuple    | q=[]; heapq.heappush(q, (5, ‘ab’))                           |
| pop                 | `print (heapq.heappop(q))`                                   |
| first item          | `q[0]`                                                       |
| print heapq         | `print list(q)`                                              |
| create a queue      | `from collections import deque; queue = deque([1,5,8,9])`    |
| append queue        | `queue.append(7)`                                            |
| pop queue from head | `element = queue.popleft()`                                  |
| Reference           | [Link: Python Heapq](https://www.techbeamers.com/python-heapq/) |

### 1.3 LIST & TUPLES

| Name                                                         | Comment                                                      |
| :----------------------------------------------------------- | :----------------------------------------------------------- |
| [Create a fixed size array](https://stackoverflow.com/questions/10617045/how-to-create-a-fix-size-list-in-python/10617340) | `[None]*5`                                                   |
| Create a fixed size matrix/2D array                          | `[[sys.maxsize for j in range(2)] for i in range(3)]`        |
| Flatten 2D array into 1D array                               | `[a for r in matrix for a in r]`                             |
| [Iterate over a list](https://developers.google.com/edu/python/lists) | `for v in l:`                                                |
| [Iterate over a list with index+val](https://www.geeksforgeeks.org/python-accessing-index-and-value-in-list/) | `for i, v in enumerate(l):`                                  |
| zip two lists as one                                         | l = sorted(zip(nums, range(len(nums))))                      |
| Convert int array to a string                                | `' '.join([str(v) for v in [1, 2,3,4]])`                     |
| Extact columns from multi-dimensional array                  | `[row[1] for row in l]`                                      |
| Sort in descending                                           | l=sorted([8, 2, 5], reverse=True)                            |
| Sort list by a lambda key                                    | l=sorted([(‘ebb’,12),(‘abc’,14)], key=lambda x: x[1])        |
| Sort list by a function                                      | sorted(logs, key=getKey), [LeetCode: Reorder Data in Log Files](https://code.dennyzhang.com/reorder-data-in-log-files) |
| In-place sort                                                | `l.sort()`                                                   |
| Find the index of one item                                   | `[1,2,5,3].index(2)`                                         |
| Return all but last                                          | `list[:-1]`                                                  |
| The second last item                                         | `list[-2]` or `list[~1]`                                     |
| Generate a-z                                                 | `map(chr, range(ord('a'), ord('z')+1))`                      |
| Convert from ascii to character                              | `chr(ord('a'))`                                              |
| Reverse a list                                               | `["ab", "cd", "ef"][::-1]`                                   |
| map                                                          | `map(lambda x: str(x), [1, 2, 3])`                           |
| Copy a range to another range                                | nums1[:k+1] = nums2[:j+1]                                    |
| append an element                                            | `array.append(var)`                                          |
| insert elements to head                                      | `array.insert(0,var)`                                        |
| delete element by index                                      | `del a[1]`                                                   |
| list as stack                                                | `item = l.pop()`                                             |
| map/reduce                                                   | `functools.reduce((lambda x, y: "%s %s" % (x, y)), l)`       |
| replace ith to jth                                           | `list[i:j] = otherlist`                                      |
| combine two list                                             | `list1 + list2`                                              |
| get sum                                                      | `sum(list)`                                                  |
| unique list                                                  | `set(["Blah", "foo", "foo", 1, 1, 2, 3])`                    |
| Insert to sorted list                                        | `bisect.insort(l, 3)`                                        |
| Reverse a list                                               | `l[::-1]`                                                    |
| Print zip array                                              | `print(list(zip(l1, l2)))`                                   |
| Reference                                                    | [Link: Lists and Tuples in Python](https://realpython.com/python-lists-tuples/) |

### 1.5 STACK & QUEUE

| Name                                                         | Comment                                                      |
| :----------------------------------------------------------- | :----------------------------------------------------------- |
| [Python deque as a stack](https://www.geeksforgeeks.org/deque-in-python/) | s = collections.deque(), s.append(x), s.pop(), s[-1]         |
| [Python deque as a queue](https://www.geeksforgeeks.org/deque-in-python/) | s = collections.deque(), s.append(x), s.popleft(), s[0]      |
| Implement a stack in Python                                  | [Link: Stack in Python](https://www.geeksforgeeks.org/stack-in-python/). Leverage: list, collections.deque or queue.LifoQueue |

TBD 

1. Calculate interval 
2. MergeSort 
3. Binary Search 
4. Floyd Tortoise and hare 
5. 