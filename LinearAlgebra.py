# -*- coding: utf-8 -*-
"""
Created on Sun Mar 18 02:04:42 2018

@author: Vinh Huynh
"""

import numpy as np
A = np.array([[-1,0.25,0.25,0],[0.25,-1,0,0.25],[0.25,0,-1,0.25],[0,0.25,0.25,-1]])
B = 0.25*np.array([-350,-500,-300,-300])

X = np.linalg.solve(A,B)
print(X)
