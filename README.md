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