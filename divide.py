#!/usr/bin/env python
# coding: utf-8

def division(a, b):
    if a < b:
        return 0
    else:
        return 1 + division(a-b, b)


t= 24
n= 2
print(division(t, n))
