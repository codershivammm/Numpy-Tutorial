import numpy as np

#TWO DIMENSION ARRAY

two_d_arr = np.array([[1,2,3,4],[1,2,3,4]])
print(two_d_arr)
print(two_d_arr.ndim)  #ndim functions is used to find the dimensions of the array

#THREE DIMENSION ARRAY

three_d_array = np.array([[[1,2,3],[1,2,3],[1,2,3]]])
print(three_d_array)
print(three_d_array.ndim)

#N-DIMENSION ARRAY

N_D_ARRAY = np.array([1,2,3], ndmin=5) #This Creates a Five Dimesnion Array
print(N_D_ARRAY)
print(N_D_ARRAY.ndim)