#!/usr/bin/env python
# coding: utf-8


def divide(t, n):        # Optional
    if t < n:
        return 0
    else:
        return 1 + divide(t-n, n)


print("\nDivide...")
t1 = int(input("Enter 1st No.: "))
n1 = int(input("Enter 2nd No.: "))
print("Divide: ", divide(t1, n1))
