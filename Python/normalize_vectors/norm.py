from numpy import linalg as LA
import numpy as np


def InnerProduct(v1):
    if(len(v1) == 0):
        print('invalid vector!')
    v1T = np.transpose(v1)
    sum = 0
    for id in range(len(v1)):
        t = v1[id]*v1T[id]
        sum = sum+t
    print(f'<v|v>={np.sqrt(sum)}')


def ComputeNorm(v1):
    if(len(v1) == 0):
        print(f'invalid vector')
        return
    sum_t = 0
    for x in v1:
        t = np.power(x, 2)
        sum_t = sum_t+t
    return(np.sqrt(sum_t))


v1 = [6, 8, 9]

v1T = np.transpose(v1)

norm = ComputeNorm(v1)
v1Normed = v1/norm
print(v1, v1Normed)
InnerProduct(v1)
