#!/usr/bin/env python
# coding: utf-8

def harmonic(n):
    if n == 0:
        return 1
    else:
        return 1/n + harmonic(n-1)


num = int(input("Enter the value:"))
result = harmonic(num)
print("harmonic is :", result)
