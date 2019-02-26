'''
Created on 26 lut 2019

@author: szymonOleksiewicz
'''
import numpy as np
A = np.matrix [1,2,3,4,5,6]

A = [[12,7,3],
     [4,5,6],
     [7,8,9]]

B = [[5,8,1,2],
     [6,7,3,0],
     [4,5,9,1]]
    
# result is 3x4
res = [[0,0,0,0],
       [0,0,0,0],
       [0,0,0,0]]
       
for l in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(B)):
            res[l][j] += A[l][k] * B[k][j]
print(res)    
A = [[12,7],
     [4,5],
     [3,8]]
T = [[0,0,0],
     [0,0,0]]
         
for k in range(len(A)):
    for j in range(len(A[0])):
        T[j][k] = A[k][j]
for r in T:
    print(r)
