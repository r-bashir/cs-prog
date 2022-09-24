#!/usr/bin/env python
# coding: utf-8

def harmonic(n):         # Compulsory

    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return 1/n + harmonic(n-1)


print("\nHamonic...")
n = int(input("n: "))
print("Hamonic: ", harmonic(n))
