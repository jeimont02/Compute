#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 21:46:39 2023

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
