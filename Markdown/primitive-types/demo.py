
# Preface:
# A single bitwise AND is O(1)

def count_bits (x):
    num_bits = 0
    while x:
        num_bits += x & 1 
        x >>= 1 
    return num_bits 
   
# The parity returns 1 if the number of 
# 1s in the binary representation of the 
# number is odd, else return 0  


# Brute Force 1:  
def parity (x):
    count = 0
    result = 0
    while x:
        if x & 1 == 1:
            count += 1 
        x >>= 1 
    
    if count % 2 == 1:
        result = 1 
    return result 

# O(k), k being the number of set bits
# Note: x&(x-1) equals x with its lowest set bit erased 
# (Here & is the bitwise-AND operator) 
def parity2 (x):
    result = 0 
    while x:
        result ^= 1  # ^ is the XOR operator. Only true when inputs differ
        x &= x - 1 # Drops the lowest set bit of x 
    return result 


# Idea, cache the result as you compute. 
def parity3 (x):
    PRECOMPUTED_PARITY = {}
    mask_size = 16 
    bit_mask = 0xFFFF 
    return (PRECOMPUTED_PARITY[x >> (3 * mask_size)] ^ 
            PRECOMPUTED_PARITY[(x >> (2 * mask_size)) & bit_mask] ^ 
            PRECOMPUTED_PARITY[(x >> mask_size)
            & bit_mask] ^ PRECOMPUTED_PARITY[x & bit_mask])



def parity4 (x):
    x ^= x >> 32
    x ^= x >> 16
    x ^= x >> 8
    x ^= x >> 4
    x ^= x >> 2
    x ^= x >> 1
    return x & 0x1 

