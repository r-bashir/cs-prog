#!/usr/bin/env python
# coding: utf-8

def power(x, n):
    if n == 0:
        return 1
    else:
        result = (x * power(x, n - 1))
        return result


num = int(input("Enter Base: "))
exp = int(input("Enter Expo: "))
print("Result: ", power(num, exp))
