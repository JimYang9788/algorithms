# Strings 

# Understand the implication of a string type which is immutable, 
# e.g. the need to allocate a new string when concatenating 
# immutable 

# e.g. "+123", "-321" -> 123, -321

import functools

def str_to_int(s):
    return (-1 if s[0] == '-' else 1) * functools.reduce(
        lambda running_sum, c: running_sum * 10 + string.digits.index(c),
        s[s[0] in '-+': ],0) # 骚得一批...s[s[0] in '-+':] 就是s作为list来用，但是slice了开始位置..

# e.g. 123, 321 -> "123", "321"

def int_to_str(n):
    is_negative = False
    if n < 0:
        n, is_negative = -n, True
    
    s = []
    while n!=0:
        s.append(chr(ord('0')+ n%10))
        n /= 10
    return ('-' if is_negative else '') + ''.join(reversed(s))