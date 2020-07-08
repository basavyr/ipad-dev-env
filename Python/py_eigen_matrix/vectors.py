import numpy as np
from numpy import random as rd
from numpy import linalg as LA

m0=[[1, 1, 1 ] ,[2, 2, 2 ]]

def Matrix(n):
    m=[]
    for id in range(n):
        line=[]
        for line_id in range(n):
            line.append(id+1)
        m.append(line)
    return m

def SymbMatrix(n):
    m=[]
    for id in range(n):
        line=[]
        for line_id in range(n):
            element='v'+str(id+1)+str(line_id+1)
            line.append(element)
        m.append(line)
    return m

m1=Matrix(3)
m1_symb=SymbMatrix(3)
# for id in range(len(m1_symb)):
    # print(m1_symb[id])

m1sT=np.transpose(m1_symb)
# print(m1sT)

values, vectors=LA.eig(m1)

lambdas=[]
for value in values:
    # print(round(value,2))
    lambdas.append(round(value,2))

# print(lambdas)
print('Eigenvectors')
# print(vectors)

def ComputeNorm(v):
    n=len(v)
    sumt=0
    for id in range(n):
        t0=v[id]
        t0_star=np.conj(t0)
        t=t0*t0_star
        sumt=sumt+t
    return np.sqrt(sumt)

# v=[1,1,1]
# vN=v/ComputeNorm(v)

for id in range(len(vectors)):
    p1_row=vectors[id]
    p1_col=vectors[:,id]
    print('row',p1_row,ComputeNorm(p1_row))
    print('col',p1_col,ComputeNorm(p1_col))

print(f'Eigenvectors')
print(vectors)