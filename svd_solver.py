import numpy as np

def svd_solver(A: np.array):
    """
    Perform Singular Value Decomposition (SVD) on the input matrix A.

    Parameters:
        A (numpy.ndarray): The input matrix for which SVD is performed.

    Returns:
        U (numpy.ndarray): Eigenvectors matrix of A*A^T.
        sigma (numpy.ndarray): Diagonal matrix of singular values.
        V (numpy.ndarray): Eigenvectors matrix of A^T*A.
        cond_number (float): Condition number of the matrix.
        inv_A (numpy.ndarray): Inverse of the input matrix A.

    Raises:
        ValueError: If at least one of the singular values is 0,
                    indicating that the inverse of the matrix does not exist.
    """


    tolerance = 1e-5

    cov_matrix_U = np.dot(A, A.T)
    cov_matrix_V = np.dot(A.T, A)
    
    
    eigen_values_U, eigen_vectors_U = np.linalg.eig(cov_matrix_U)
    eigen_values_V, eigen_vectors_V = np.linalg.eig(cov_matrix_V)
    
    
    sorted_indices_U = np.argsort(eigen_values_U)[::-1]
    sorted_indices_V = np.argsort(eigen_values_V)[::-1]
    
    eigen_values_U = eigen_values_U[sorted_indices_U]
    eigen_vectors_U = eigen_vectors_U[:, sorted_indices_U]
    
    eigen_values_V = eigen_values_V[sorted_indices_V]
    eigen_vectors_V = eigen_vectors_V[:, sorted_indices_V]

    U = eigen_vectors_U
    V = eigen_vectors_V

    sigma = np.zeros_like(A, dtype=float)
    for i in range(len(eigen_values_U)):
        sigma[i, i] = np.sqrt(eigen_values_U[i])

    sign = np.sign((A@V)[0] * (U@sigma)[0])
    V = V*sign
    

    for val in np.diag(sigma):
        if np.abs(val) < tolerance:
            raise ValueError("At least one of the single values is 0. This means the inverse of the matrix does not exist.")
        
    
    min =np.min(np.diag(sigma))
    max = np.max(np.diag(sigma))

    cond_number = max/min

    inv_sigma = np.linalg.inv(sigma)
    inv_A = V @ inv_sigma @ U.T


    V = V.T

    return U, sigma, V, cond_number, inv_A

