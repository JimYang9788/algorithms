# Week 1 Array 
# 5.1 The Dutch National Flag Problem 


# One solution to the quicksort run time problem 
# is to reorder the array so that all elements less
# than the pivot apppear first, followed by elements 
# equal to the pivot, followed by the elements greater 
# than the pivot. This is called Dutch national flag 
# because the dutch national flag consists of three
# horizontal bands  

# Write a program that takes an array A and an index i into A,
# and rearrages the elements such that all elements less than A[i]
# appears first

# Solution 1, very trivial 
def dutch_flag1(A, i):
    pivot = A[i]
    less, equal, greater = [], [], []
    for val in A:
        if val < pivot:
            less.append(val)
        elif val == pivot:
            equal.append(val)
        else:
            greater.append(val)
    A = less + equal + greater  # O(n) in time and space 
    return A 

# Solution 2: Swap O(n) with O(1) Space Complexity 
def dutch_flag2(A, i):
    pivot = A[i]
    smaller = 0 
    for i in range (len (A)):
        if A[i] < pivot:
            A[i], A[smaller] = A[smaller], A[i] # Through Swapping, Group all the smaller elements to the left hand side 
            smaller += 1 

    larger = len(A) - 1 
    for i in  reversed(range(len (A))):
        if A[i] > pivot:
            A[larger], A[i] = A[i], A[larger]
            larger -= 1 
    
    return A 
    





if __name__ =='__main__':
    A = [1,4,3,2,2]
    print (dutch_flag1(A, 3))