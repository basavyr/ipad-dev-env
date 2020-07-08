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
for id in range(len(m1_symb)):
    print(m1_symb[id])
