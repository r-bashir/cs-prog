#!/usr/bin/env python
# coding: utf-8


def get_binary(x):
    if x == 0:
        return "" 
    else:
        return get_binary(x//2) + str(x%2)
        

print("\nGet Binary...")
num = int(input("Enter No.: "))
print("Binary No.: ", get_binary(num))
