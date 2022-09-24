#!/usr/bin/env python
# coding: utf-8


def multiply(m, n):      # Compulsory
    if n == 0 or m == 0:
        return 0
    else:
        return m + multiply(m, n-1)


print("\nMultiplication...")
m1 = int(input("m: "))
n1 = int(input("n: "))
print("Multiplication: ", multiply(m1, n1))
