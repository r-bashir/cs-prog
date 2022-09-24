#!/usr/bin/env python
# coding: utf-8


def largest(a):          # Compulsory
    if len(a) == 1:
        return a[0]
    else:
        if (a[0] > largest(a[1:])):
            return a[0]
        else:
            return largest(a[1:])

            
print("\nLargest...")
l1 = [3, 5, 9, 0, 15]
print(l1)
print("Larget: ", largest(l1))
