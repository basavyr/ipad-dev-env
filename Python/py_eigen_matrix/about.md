# Study the eigenvectors given by `Linalg` implementation of `numpy`

This script studies the behavior of the results returned by the `eig` implementation found in `linalg` submodule from `numpy`.

The actual type of data structure is relevant to the present study, due to the necessity of having consistency between results given by Python and Mathematica with regards to solving the eigenvalue and eigenvector equation for a Hermitian squared matrix $M$.

## Comparison between the data structure of the eigenvectors provided by Mathematica and Python

Mathematica provides the eigenvectors for a matrix $M$ (in the present case, a Hermitian, squared matrix) with the implementation called `Eigensystem`.

On the other hand, Python uses `linalg`, which is a sub-module of `numpy`.

___

### Mathematica's `Eigensystem`

The eigenvectors are returned as a matrix, where each **line** contains the components of a vector $v_i$, vector that checks the equation:
$$Mv_i=\lambda_iv_i$$

**Observation**: Although above equation is correct from a mathematical standpoint, when referring to the actual implementation of `Eigensystem`, the equation that the vectors must verify is:
$$M\mathbf{v}^T=\Lambda\mathbf{v}^T$$

This is because the eigenvectors $v_i$ are returned as row vectors, and the first equation requires each $v_i$ to be a column vector.

So, in conclusion, in order to get each of the $n$ - eigenvectors of a matrix $M$, one must first select the vector with $v_i=\mathbf{v}[[i]]$ and then apply `Transpose[`$v_i$`]` in order to check the first equation.

### Python's `linalg`

Python returns the eigenvectors (which are also normalized to unity by default) as a list of column vectors, where each column `v[:,i]` is in fact $v_i$. 

In other words, Python's `eig` implementation doesn't require a transposition of the eigenvector matrix in order to check the consistency of the eigenvector/eigenvalue equation.
