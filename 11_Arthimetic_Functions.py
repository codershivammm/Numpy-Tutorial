import numpy as np

#Dealing With The 1D Array..
var = np.array([1,2,3,4,5,6,7,8,9])
print("Minimum Value in Array:-",np.min(var))
print("Maximum Value in Array:-",np.max(var))
print(f"Minimum Value {np.min(var)} is at Index No:-",np.argmin(var))
print(f"Maximum Value {np.max(var)} is at Index No:-",np.argmax(var))   #Location of the minimum value in the array

#CUMSUM() FUNCTION

print(np.cumsum(var)) #1 , 1+2 , 3+3 , 6+4 , 10+5 , so on........

#Similar Functions:-
#np.sqrt(var) = for sqaure root
#np.cos(var) = for finding the cos Value
#np.sin(var) = for finding the sin value

#---------------------------------------------------------------------------------------------------------------------------------------------

#Dealing With 2D Array....

#NOTE = Axis 0 is Along column and Axis 1 is Along Rows

var2d = np.array([[1,2,3,4],[5,6,7,8]])
print("Minimum Value Along Axis 0 i.e Columns:-",np.min(var2d,axis=0))
print("Maximum Value Along Axis 1 i.e Rows:-",np.max(var2d,axis=1))
