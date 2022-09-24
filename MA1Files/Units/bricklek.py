#!/usr/bin/env python
# coding: utf-8


def bricklek(f, t, h, n): # Compulsory
    """f: source, t: target, h: auxiliary, n: tiles"""
    lst = []
    if n==1:
        # print ("Base: Move disk 1 from source", f, "to target", t)
        lst.append(f'{f}->{t}')
    else:
        lst = lst + bricklek(f, h, t, n-1)
        # print ("Move disk",n,"from source", f, "to target", t)
        lst.append(f'{f}->{t}')
        lst = lst + bricklek(h, t, f, n-1)
    return lst


print("\nBricklek...")
n = int(input("Enter No. of Tiles: "))

import time
tstart = time . perf_counter ()
bricklek('f','h','t', n)
tstop = time . perf_counter ()
print(f"Measured time : { tstop - tstart } seconds")
