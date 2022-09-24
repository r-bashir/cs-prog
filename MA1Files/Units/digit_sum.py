#!/usr/bin/env python
# coding: utf-8

def digit_sum(x):        # Optional
    if n == 0:
        return 0
    return n%10 + digit_sum(int(n/10))
    
    
num = int(input("Enter No.: "))
print("Result: ", digit_sum(num))
