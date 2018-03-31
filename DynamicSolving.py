# -*- coding: utf-8 -*-
"""
This program is to solve steady state heat transfer boundary condition using finite difference method and Linear Algebra to find
the temperature at each node.
        
                T00
           -----------------
           |---|---|---|---|
      T01  |---|---|---|---|  T10
           |---|---|---|---|
           |---|---|---|---|
           |---|---|---|---|
           -----------------
                T11
"""

import numpy as np 
import math as m
size = int(input("Please input the number of nodes (must larger than 3): "))
if (m.sqrt(size) - int(m.sqrt(size))) != 0 or size <= 3: #check if a square matrix
    print("\nThis is an invalid number of nodes since it has to be a square matrix")

dimension = int(m.sqrt(size))



#A is complete
row = 0
A = np.zeros(shape=(size,size))

#Define 1/4 in this nested for loop
for i in range(size):
    row = i // dimension
    column = i % dimension
    if row == 0:
        if column == 0:
            A[i][i+1] = 0.25
            A[i][i+dimension] = 0.25
        if 0 < column and column < (dimension - 1):
            A[i][i-1] = 0.25
            A[i][i+1] = 0.25
            A[i][i+dimension] = 0.25
        if column == (dimension-1):
            A[i][i-1] = 0.25
            A[i][i+dimension] = 0.25
    if 0 < row and row < (dimension - 1):
        if column == 0:
            A[i][i+1] = 0.25
            A[i][i+dimension] = 0.25
            A[i][i-dimension] = 0.25
        if 0 < column and column < (dimension - 1):
            A[i][i-1] = 0.25
            A[i][i+1] = 0.25
            A[i][i+dimension] = 0.25
            A[i][i-dimension] = 0.25
        if column == (dimension-1):
            A[i][i-1] = 0.25
            A[i][i+dimension] = 0.25
            A[i][i-dimension] = 0.25
    if row == (dimension - 1):
        if column == 0:
            A[i][i+1] = 0.25
            A[i][i-dimension] = 0.25
        if 0 < column and column < (dimension - 1):
            A[i][i-1] = 0.25
            A[i][i+1] = 0.25
            A[i][i-dimension] = 0.25
        if column == (dimension - 1):
            A[i][i-1] = 0.25
            A[i][i-dimension] = 0.25    
for i in range(size):
    A[i][i] = -1


B = np.zeros(shape = (size,1))
# [X] = [A]^-1[B]

T00 = int(input("Please input the temperature of T00: "))
T01 = int(input("Please input the temperature of T01: "))
T10 = int(input("Please input the temperature of T10: "))
T11 = int(input("Please input the temperature of T11: "))


#Special case
B[0][0] = (-T00-T01)*0.25
B[dimension-1][0] = (-T00-T10)*0.25
B[(dimension)*(dimension-1)][0] = (-T01-T11)*0.25
B[size-1][0] = (-T10-T11)*0.25



for i in range(size):
    row = i // dimension
    col = i % dimension
    if row == 0:
        if 0 < col and col < (dimension - 1):
            B[i][0] = -T00*0.25
    if 0 < row and row < (dimension - 1):
        if col == 0:
            B[i][0] = -T01*0.25
        if col == (dimension - 1):
            B[i][0] = -T10*0.25
    if row == (dimension - 1):
        if 0 < col and col < (dimension - 1):
            B[i][0] = -T11*0.25

X = np.linalg.solve(A,B)
print(X)
