import numpy as np
# Defining Array 1
a = np.array([[1, 2],
              [3, 4]])

# Defining Array 2
b = np.array([[4, 3],
              [2, 1]])

# Adding 1 to every element
print("Adding 1 to every element:", a + 1)

# Subtracting 2 from each element
print("\nSubtracting 2 from each element:", b - 2)

# sum of array elements
# Performing Unary operations
print("\nSum of all array "
      "elements: ", a.sum())

# Adding two arrays
# Performing Binary operations
print("\nArray sum:\n", a + b)

# Subtract two arrays
# Performing Binary operations
print("\nArray difference:\n", a - b)

"""
Multiplication of Matrices using Nested List
To multiply the matrices, we can use the for-loop on both the matrices as shown in the code below:"""
M1 = [[8, 14, -6],
      [12,7,4],
      [-11,3,21]]

M2 = [[3, 16, -6],
           [9,7,-4],
           [-1,3,13]]

M3  = [[0,0,0],
       [0,0,0],
       [0,0,0]]

matrix_length = len(M1)

#To Multiply M1 and M2 matrices
for i in range(len(M1)):
    for k in range(len(M2)):
        M3[i][k] = M1[i][k] * M2[i][k]

#To Print the matrix
print("The multiplication of Matrix M1 and M2 = ", M3)

#Tranpoe of a given matrix
M4 = np.transpose(M3)
print("transpose of M3 :", M4)

"""
Stacking: Several
arrays can be stacked together along different axes.

•	np.vstack: To stack arrays along vertical axis.
•	np.hstack: To stack arrays along horizontal axis.
•	np.column_stack: To stack 1-D arrays as columns into 2-D arrays.
•	np.concatenate: To stack arrays along specified axis (axis is passed as argument).
"""

a = np.array([[1, 2],
              [3, 4]])

b = np.array([[5, 6],
              [7, 8]])

# vertical stacking
print("Vertical stacking:\n", np.vstack((a, b)))

# horizontal stacking
print("\nHorizontal stacking:\n", np.hstack((a, b)))

c = [5, 6]

# stacking columns
print("\nColumn stacking:\n", np.column_stack((a, c)))

# concatenation method 
print("\nConcatenating to 2nd axis:\n", np.concatenate((a, b), 1))
