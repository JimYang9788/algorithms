# Write a program to test if a given word can be permutated to 
# a palindrome
import collections 

def test_palindrome(word):
    hash_table, res, odd_count = {}, False, 0
    for c in word:
        if c in hash_table:
            hash_table += 1 
        else:
            hash_table[c] = 1 
        
    for key, val in hash_table.items():
        if val % 2 == 1:
            odd_count += 1 

    res = odd_count <= 1 

    return res  

# Or concisely...

def concise_test_palindrome(s):
    return sum (v % 2 for v in collections.Counter(s).values()) <= 1

