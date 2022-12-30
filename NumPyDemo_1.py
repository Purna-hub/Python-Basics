import numpy as np
#creating  1D-arry using numpy array()
'''x = np.array([1, 2, 3])
print(x)

#creating  2D-arry using numpy array()
y = np.array([[1, 2, 3],[4, 5, 6]])

print(y)

#creating  1D-arry with complex data type using numpy array()
z = np.array([1, 2, 3], complex)
print(z)

a = np.array([[2, 4, 6, 8],[3, 6, 9, 12], [2, 2, 2, 2]])
print(a.ndim)

print("Item size = ", a.itemsize)
print("item shape = ", a.shape)
print("Data type of items= ")
print(a.dtype)
print("Reshaping of array")
print("before reshaping:")
print(a)
print("after reshaping:")
print(a.reshape(4, 3))

print(a[0, 2])


a = np.array([[[10, 11, 12], [13, 14, 15], [16, 17, 18]],
               [[20, 21, 22], [23, 24, 25], [26, 27, 28]],
               [[30, 31, 32], [33, 34, 35], [36, 37, 38]]])

print("Printing 3 X 3 3D-matrix :")
print(a)

print(a[0:, 0, 0:])

#reading single element
print(a[1, 0, 2])

print(a[0, 1, 1])

#reading row or column in 3D Matrix
#reading row

print(a[1,2])

print(a[2, :, 0]) #reading a column using slice operator

print(a[:, 1, 2]) #reading 1st row and 2nd column element form all the matrix of 3D-Array

#reading entire matrix from a 3D-Array

print(a[2])


#slicing in NumPy Array
a2 = np.array([[10, 11, 12, 13, 14],
               [15, 16, 17, 18, 19],
               [20, 21, 22, 23, 24],
               [25, 26, 27, 28, 29]])
print(a2)

a3 = np.array([[[10, 11, 12], [13, 14, 15], [16, 17, 18]],
               [[20, 21, 22], [23, 24, 25], [26, 27, 28]],
               [[30, 31, 32], [33, 34, 35], [36, 37, 38]]])


print(a3)

print(a3[0:2, 1:, 0:2])

print(a3[0:, 0, 0:])

'''
a = np.array([[1, 2, 3], [4, 5, 6]])

print(a)

a.reshape((2, 3))

print(a)

