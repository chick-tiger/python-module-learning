#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def triangles():
    L = []
    L.append([1])
    yield L[0]
    L.append([1,1])
    yield L[1]
    L.append([1,2,1])
    yield L[2]
    n = 3
    while n >= 3:
        L.append([1])
        i = 0
        while i < n-1:
            L[n].append(L[n-1][i]+L[n-1][i+1])
            i += 1
        L[n].append(1)
        yield L[n]
        n += 1



n = 0
for t in triangles():
    print(t)
    n = n + 1
    if n == 10:
        break

