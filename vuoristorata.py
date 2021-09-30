# -*- coding: utf-8 -*-
"""
Putkaposti Vuoristorata, https://www.ohjelmointiputka.net/postit/tehtava.php?tunnus=vrata

Pisin näkee aina junasta. Toiseksi pisin näkee junasta puolissa tapauksissa.
On yhtä todennäköistä, että hän on pisimmän edessä tai takana. Kolmanneksi
pisin näkee junasta joka kolmannessa tapauksessa jne.
"""

from fractions import Fraction
a = Fraction(0, 1)
for case in range(5, 32):
    a = Fraction(0, 1)
    for i in range(1, case):
        a += Fraction(1, i)
    print(str(case-1) + " " + str(a))
