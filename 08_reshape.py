#Converting 1D Array to 2D and 3D and so on.....

import numpy as np

var1 = np.array([1,2,3,4,5,6]) #1D Array
var2 = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,2,2,3,4,2]) #1D Array

#converting to 2D Now :-

two_d_arr = var1.reshape(2,3) #2 rows and 3 columns 
print(two_d_arr)
print()
print("Dimension:-",two_d_arr.ndim,"D Array")

#converting to 3D Now :-
# var1.reshape(no_of_matrices, no_of_rows , no_of_column) 

three_d_array = var2.reshape(2,3,4) #3 Rows 4 Column ka 2 Matrices Banega 
print(three_d_array)
print()
print("Dimension:-",three_d_array.ndim,"D Array")