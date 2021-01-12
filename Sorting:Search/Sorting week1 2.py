# 1. Write a program which takes an input two sorted arrays,
# And returns a new array containing elements that are presented 
# in both of the input arrays
# SHOULD BE FREE OF DUPLICATE 
import bisect

def intersect_two_sorted_array(A,B):
    def is_present (k):
        # bisect_left returns the first index of element that is 
        # less than k in list B 
        # O(log(m))
        i = bisect.bisect_left(B,k)
        return i < len(B) and B[i] == k 

    return [
        a for i , a in enumerate (A)
        if (i == 0 or a != A[i-1]) and is_present(a)
    ]
    # total in O(n log (m) )

# when advances, use i and j 
def better_intersect_two_sorted_array(A,B):
    i, j, intersection_A_B = 0,0,[]
    while i < len(A) and j < len(B):
        if A[i] == B[j]:
            if i == 0 or A[i] != A[i-1]:
                intersection_A_B.append(A[i])
            i,j = i + 1, j + 1 
        elif A[i] < B[j]:
            i += 1 
        else:
            j += 1 
    return intersection_A_B

