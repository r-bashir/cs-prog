#!/usr/bin/env python
# coding: utf-8


def factorial(n):         # Optional
    if n == 1:
      return 1
    elif n < 0:
        print("doent exist")
    elif n == 0:
        print("fac is 1")
    else:
      return (n*factorial(n-1))


num = int(input("Enter No.:"))
print("Factorial: ", factorial(num))
