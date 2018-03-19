# -*- coding: utf-8 -*-
"""
Created on Sun Mar 18 03:08:00 2018

@author: Vinh Huynh
"""

import numpy as np 
import math as m
size = int(input("Please input the number of nodes (must larger than 3): "))
if (m.sqrt(size) - int(m.sqrt(size))) != 0 or size <= 3: #check for possible matrix
    print("\nThis is an invalid number of nodes since it has to be a square matrix")

dimension = int(m.sqrt(size))


"""
#Redefine A--install a row system 
row = 0
A = np.zeros(shape=(size,size))

#Define 1/4 in this nested for loop
for row in range(size):
    for column in range(size):
        

for i in range(size):
    A[i][i] = -1   #This is correct
"""    


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

'''
#THIS IS NOT COMPLETE 
for i in range(1,size):
    if i == (dimension - 1):
        continue
    if i == dimension*(dimension-1):
        continue
    if i == size - 1: 
        continue
    if i < (dimension - 1): 
        B[i][0] = -T00*0.25
    if (dimension - 1) < i and i < dimension*(dimension -1):
   #     if   #internal zero
   #     if   #outside
            
        if i % (dimension) == 1:
            B[i][0] = -T10*0.25
    if i > dimension*(dimension - 1):
        B[i][0] = -T11*0.25
'''

X = np.linalg.solve(A,B)
print(X)