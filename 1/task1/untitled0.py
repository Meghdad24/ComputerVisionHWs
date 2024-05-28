# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 10:10:36 2024

@author: Pouria
"""
import numpy as np

A = np.random.rand(200,10)
print(np.sum(A, axis=0))


mu = np.zeros(A.shape[1])
for i in range(A.shape[0]):
    mu += A[i]
mu /= A.shape[0]

C = np.zeros_like(A)
for i in range(A.shape[0]):
    C[i] = A[i] - mu
    


B = A - (np.sum(A, axis=0) / A.shape[0])

D = C == B