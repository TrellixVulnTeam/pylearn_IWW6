# !/usr/bin/env python3
# -*- coding: utf-8 -*-


def power(x, n=2):
    s = 1
    while n > 0:
        s = s * x
        n = n - 1
    return s


print(power(5, 3))
