#!/usr/bin/env python
# coding: utf-8

def power(x, n):
    if n == 0:
        return 1
    else:
        return (x * power(x, n - 1))


num = int(input("Enter Base: "))
exp = int(input("Enter Expo: "))
print("Result: ", power(num, exp))
