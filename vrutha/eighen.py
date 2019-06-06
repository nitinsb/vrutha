
"""documentaion 
numpy.linalg.eig(a)[source]
Compute the eigenvalues and right eigenvectors of a square array.

Parameters:	
a : (…, M, M) array
Matrices for which the eigenvalues and right eigenvectors will be computed

Returns:	
w : (…, M) array
The eigenvalues, each repeated according to its multiplicity. The eigenvalues are not necessarily ordered. The resulting array will be of complex type, unless the imaginary part is zero in which case it will be cast to a real type. When a is real the resulting eigenvalues will be real (0 imaginary part) or occur in conjugate pairs

v : (…, M, M) array
The normalized (unit “length”) eigenvectors, such that the column v[:,i] is the eigenvector corresponding to the eigenvalue w[i].

Raises:	
LinAlgError
If the eigenvalue computation does not converge.

"""
import numpy as np
# read the size
print("Enter the size of matrix")
n = int(input()) 
print("Enter the elements of matrix")
# read the elements using genrators
a = [[int(j) for j in input().split()] for i in range(n)]\


m = np.matrix(a)
eigenvalues, eigenvectors = np.linalg.eig(m)
print("The Eigen values are...")
print(eigenvalues)
print("The Eigen vectors are...")
print(eigenvectors)


