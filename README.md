# SVD_solver

#### Files Included

`svd_solver.py` : Includes a Custom SVD decomposition function |
`equlibrium.py` : Includes all necessary functions to solve the two spring-mass systems prescribed |
`SVD_comparisons.ipynb` : Shows comparison of custom solver and numpy results from part 1 of the project


### Running the Spring_Mass system

In the terminal, in this repository's directory, run `python3 equlibrium.py`

The user will then be prompted with the following with sample input:
```
Enter the number of springs
3
Enter the number of masses
3
Enter either: Fixed-Free or Fixed-Fixed
Fixed-Free
Enter the spring constant for spring 1
1
Enter the spring constant for spring 2
1
Enter the spring constant for spring 3
1
Enter the mass for mass 1
1
Enter the mass for mass 2
1
Enter the mass for mass 3
1
```


If the user enters invalid input they will be prompted with an error message such as the one below and then be asked to input valid information again
```
Input not accepted. Please Follow the instructions.
Please enter positive integers for each of springs and mass. The number of masses must be equal or one less than the number of springs.
The boundary condition must be either Fixed-Free or Fixed-Fixed.
Enter the number of springs
```

When valid input is made the user will be given info similar to the following:
```
A matrix: 
[[ 1.  0.  0.]
 [-1.  1.  0.]
 [ 0. -1.  1.]]
Spring constant Matrix: 
[[1. 0. 0.]
 [0. 1. 0.]
 [0. 0. 1.]]
Force vector: 
[-9.81 -9.81 -9.81]
Stiffness Matrix: 
[[ 2. -1.  0.]
 [-1.  2. -1.]
 [ 0. -1.  1.]]
Displacement vector: 
[-29.43 -49.05 -58.86]
Elongation vector: 
[-29.43 -19.62  -9.81]
Internal Forces: 
[-29.43 -19.62  -9.81]
Singular value matrix:
 [[3.2469796  0.         0.        ]
 [0.         1.55495813 0.        ]
 [0.         0.         0.19806226]]
The Stiffness Matrix has condition number: 16.393731622284225
```

### Using the SVD solver

In the event that you would like to use the SVD solver for some other case, the function parameters and returns are as follows:
```
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
```


### SVD Results comparison

All of the following are visible in the SVD_comparison.ipynb

The following array was used for the comparison:
```
A = np.array([[5, 2, 3],
              [4, 5, 6],
              [7, 8, 9],])
```

The following is output comparing my custom solver to numpy's solution for SVD
```
Custom U:
[[ 0.32717864  0.93556421 -0.13294265]
 [ 0.50256733 -0.29141461 -0.81394324]
 [ 0.8002376  -0.19949221  0.56552864]]

NumPy U:
[[-0.32717864  0.93556421 -0.13294265]
 [-0.50256733 -0.29141461 -0.81394324]
 [-0.8002376  -0.19949221  0.56552864]]

Custom Vt
[[ 0.5317045   0.55017589  0.64389193]
 [ 0.83522779 -0.46657511 -0.29103642]
 [ 0.14030273  0.69254181 -0.70760228]]

NumPy Vt
[[-0.5317045  -0.55017589 -0.64389193]
 [ 0.83522779 -0.46657511 -0.29103642]
 [ 0.14030273  0.69254181 -0.70760228]]

Custom S (Sigma):
[[17.39279188  0.          0.        ]
 [ 0.          2.53310192  0.        ]
 [ 0.          0.          0.27237001]]

NumPy S (Sigma):
[17.39279188  2.53310192  0.27237001]

Custom Reconstructed Matrix (U @ S @ Vt):
[[5. 2. 3.]
 [4. 5. 6.]
 [7. 8. 9.]]

Numpy Matrix A reconstructed
[[5. 2. 3.]
 [4. 5. 6.]
 [7. 8. 9.]]
 ```

 As we can see above, not every value of every matrix is exactly the same. However, this does not mean that either solution is incorrect. There is simply more than one functional SVD decomposition for a given matrix.

 It is clear that both solutions work as the reconstructed matrices are identical to the provided A matrix for this example.

 On top of this, the inverse matrix and condition numbers of my custom solver and numpy mathed up as well. Below are those comparisons
 ```
 Custom SVD solver condition number and inverse matrix:
63.85722159418202
[[ 0.25       -0.5         0.25      ]
 [-0.5        -2.          1.5       ]
 [ 0.25        2.16666667 -1.41666667]]
Numpy condition number and inverse matrix:
63.85722159418491
[[ 0.25       -0.5         0.25      ]
 [-0.5        -2.          1.5       ]
 [ 0.25        2.16666667 -1.41666667]]
 ```

 The minor difference in condition number is caused by floating point imprecision.


### Two Free End Examination

As discussed in lecture 8, having two free ends of such a system does not make physical sense. This is seen in the example where you have 3 masses and 2 springs in a free-free system. This creates a stiffness matrix which is a 3x3 with a rank of two. This means that it is not invertible and therefore is not solvable. The issue stems from having more unknowns than equations. This means that there will not be a unique solution to the system. The stiffness matrix must have full rank (in this case rank of 3) in order to be solvable. This is only achievable with one of the boundary conditions that I have implemented in the SVD algorithm.