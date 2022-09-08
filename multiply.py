#!/usr/bin/env python
# coding: utf-8

def multiply(m, n):
    if n == 1:
        return m
    else:
        return m + multiply(m, n-1)


m1 = 5
n1 = 6
result = multiply(m1, n1)
print("Result: ", result)
