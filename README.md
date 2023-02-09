# Compute
This program computes the values of 1+1.0/ (1!) + 1.0 / (2!) + 1.0 / (3!) + ...+ 1.0 / (n!) (eq-1) (where i! = i x (i-1) x (i-2) x (i-3) x ... x 2 x 1)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 21:36:39 2023

@author: jacobeimont
"""

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def sum_of_terms(n):
    result = 0
    for i in range(1, n+1):
        result += 1.0 / factorial(i)
    return result

n = int(input("Enter the number of terms to include in the summation: "))
result = sum_of_terms(n)
print("The sum of the first", n, "terms is:", result)
