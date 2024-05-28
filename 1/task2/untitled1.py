# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 10:49:47 2024

@author: Pouria
"""

from matplotlib import pyplot as plt
import numpy as np

I = plt.imread('masoleh_gray.jpg')

Icopy = np.flip(I, axis=0)

concatenated_matrix = np.concatenate((I, Icopy), axis=0)

plt.imshow(concatenated_matrix,cmap='gray')
plt.show()