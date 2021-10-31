#!/usr/bin/env python3

def f(x):
    if x == 0:
        return 1
    s = 0
    for i in range(x):
        s += f(i)
    return s


for i in range(11):
    print(f(i))
