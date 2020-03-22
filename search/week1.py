# Basics 

def bsearch (A, n):
    U = len (A) - 1 
    L = 0 
    res = -1 
    while (L <= U):
        M = (U - L) // 2 
        if A [M] > n: 
            L = M + 1 
        elif L[M] < n:
            U = M - 1 
        else:
            res = M 
            L = U + 1 # Break the loop

    return res 


# 11.1 Search a sorted array for the first occurrence of k

# Asks for the index of any element of a sorted array that is 
# equal to a specified element. Returns the index of the 
# first occurrence of that key in the array.
def search_occurrence_k (A, n):
    L = 0 
    U = len(A) - 1 
    res = -1 

    while (L <= U):
        M = (L+U) // 2
        if (A[M] < n):
            U = M - 1 
        elif A[M] > n:
            L = M + 1 
        else:
            res = M 
            U = M - 1  # Only difference, keep searching until runs out. 
    return res 