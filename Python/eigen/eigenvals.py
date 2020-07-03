import numpy as np
import matplotlib.pyplot as plt
from numpy import random as rd
from numpy import linalg as LA

# The number w is an eigenvalue of a if there exists a vector v such that a @ v = w * v. Thus, the arrays a, w, and v satisfy the equations a @ v[:,i] = w[i] * v[:,i] for i \in \{0,...,M-1\}.

# The array v of eigenvectors may not be of maximum rank, that is, some of the columns may be linearly dependent, although round-off error may obscure that fact. If the eigenvalues are all different, then theoretically the eigenvectors are linearly independent and a can be diagonalized by a similarity transformation using v, i.e, inv(v) @ a @ v is diagonal.


def CreateMatrix(n):
    test_line = np.linspace(1, n, n, dtype=int)
    m = []
    pow = 1
    for _ in range(n):
        line = []
        for x in test_line:
            m_ij = x
            m_ij = np.power(x, 1)
            line.append(m_ij)
        m.append(line)
        pow = pow+1
    return m


M1 = CreateMatrix(3)
M2 = CreateMatrix(4)


def GetEigenvalues(m):
    eigs, vecs = LA.eig(m)
    return eigs


def GetEigenvectors(m):
    eigs, vecs = LA.eig(m)
    return vecs


def ComputeMatrix(n):
    M = CreateMatrix(n)
    M_eigs = GetEigenvalues(M)
    M_vecs = GetEigenvectors(M)
    print(f'The matrix M is: {M}')
    print('The eigenvalues are')
    for omega in M_eigs:
        print(int(np.round(omega)))
    print('The eigenvectors are')
    for v in M_vecs:
        print(np.round(v))


def IdentityMatrix(n):
    m = []
    for column in range(n):
        line = []
        for row in range(n):
            if(row == column):
                x = 1
                line.append(1)
            else:
                line.append(0)
        m.append(line)
    return m


id3 = IdentityMatrix(3)

matrix_vec = [[1, 2, 3], [0, 1, 1], [2, 2, 2]]

values, vectors = LA.eig(matrix_vec)

count = 1
for value in values:
    # print(f'l[{count}]={value}')
    # print(f'Its corresponding vector is: v[{count}]={vectors[:,count-1]}')
    count = count+1


def CreateLambdaMatrix(n, lambdas):
    if(n != len(lambdas)):
        return 'Error: the matrix is invalid'
    count = 0
    m = []
    for column in range(n):
        line = []
        for row in range(n):
            if(row == column):
                line.append(lambdas[count])
                count = count+1
            else:
                line.append(0)
        m.append(line)
    return m

# check if the eigenvalues are comouted correctly
# l is the list of eigenvalues
# v is the list with the eigenvectors of m


def CheckEigenEquation(m, l, v):
    if(len(m) != len(l)):
        return 'Invalid matrix: can\'t solve the system'
    
    lhs = 0
    rhs = 0
    for id in range(len(m)):
        x_id = v[:, id]
        lhs = np.matmul(m, x_id)
        rhs = l[id]*x_id
    for elem in range(len(lhs)):
        a1=round(lhs[elem],4)
        a2=round(rhs[elem],4)
        if(a1==a2):
            print(f'The equation no.{elem+1} is VALID')
        else:
            print(f'Not valid')


CheckEigenEquation(matrix_vec, values, vectors)


lambdas = CreateLambdaMatrix(3, values)
lhs = np.matmul(lambdas, np.transpose(vectors))
# print(lhs)
rhs = np.matmul(matrix_vec, np.transpose(vectors))
# print(rhs)

x0 = vectors[:, 0]

lhs = np.matmul(matrix_vec, x0)
# print(lhs)

rhs = values[0]*vectors[:, 0]
# print(rhs)
# This is implemented using the _geev LAPACK routines which compute the eigenvalues and eigenvectors of general square arrays.

# The number w is an eigenvalue of a if there exists a vector v such that a @ v = w \* v. Thus, the arrays a, w, and v satisfy the equations a @ v[:,i] = w[i] \* v[:,i] for :math:i \in \{0,...,M-1\}.

# v  : (..., M, M) array
# The normalized (unit "length") eigenvectors, such that the  column `v[:,i]` is the eigenvector corresponding to the  eigenvalue `w[i]`

# print(values)

count = 1
for id in range(len(vectors)):
    # print(f'The vector x_{count}: {vectors[id,0]}')
    count = count+1


# print(vectors)
