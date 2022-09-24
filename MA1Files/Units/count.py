#!/usr/bin/env python
# coding: utf-8

def count(x, s):         # Compulsory
    if s == []:
        return 0
        
    if s[0] == x:
        return 1 + count(x, s[1:])
    elif type(s[0]) == list:
        return count(x, s[0]) + count(x, s[1:])
    else:
        return 0 + count(x, s[1:])
        

print("\nCount...")
l1 = [1, 4, 2, ['a', [ [ 4 ] , 3, 4] ] ]
print("l1 = ", l1)
x = int(input("x: "))
print("Count: ", count(x, l1))
