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


if __name__ =='__main__':
    A = [1,4,3,2,2]
    print (dutch_flag1(A, 3))