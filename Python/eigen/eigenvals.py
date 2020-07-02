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


ComputeMatrix(3)
ComputeMatrix(4)

matrix_vec = [[1, 1, 1, 1], [-4, 0, 0, 1], [-3, 0, 1, 0], [-2, 1, 0, 0]]

print(matrix_vec)
