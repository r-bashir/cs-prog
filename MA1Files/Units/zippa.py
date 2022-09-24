#!/usr/bin/env python
# coding: utf-8


def zippa(l1, l2):       # Compulsory

    # Base Case:
    if len(l1) <= 1 and len(l2) <= 1:
        return [l1[0], l2[0]]
    
    # Recursive Call:
    if len(l1) > len(l2):
        return [l1[0], l2[0]] + zippa(l1[1:len(l2)], l2[1:]) + l1[len(l2):]
        
    elif len(l1) < len(l2):
        return [l1[0], l2[0]] + zippa(l1[1:], l2[1:len(l1)]) + l2[len(l1):]        
    else:
        return [l1[0], l2[0]] + zippa(l1[1:], l2[1:])


print("\nZippa...")
l1 = [1, 4, 2, 7]
l2 = [1, 4, 2]
print("l1 = ", l1)
print("l2 = ", l2)
print("Zippa: \n", zippa(l1, l2))
