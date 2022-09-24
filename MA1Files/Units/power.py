#!/usr/bin/env python
# coding: utf-8


def power(x, n):         # Optional
    if n == 0:
        return 1
    elif n > 0:
        return x*power(x, n-1)
    else:
        return 1./power(x, -n)  # OR, return 1./(x*power(x, n+1))


print("\nPower...")
num = int(input("Enter Base: "))
exp = int(input("Enter Expo: "))
print("Power: ", power(num, exp))
