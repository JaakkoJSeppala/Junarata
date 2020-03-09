# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from fractions import Fraction
a = Fraction(0,1)
for case in range(5,32):
    a = Fraction(0,1)
    for i in range(1,case):
        a += Fraction(1,i)
    print(str(case-1) + " " +str(a))