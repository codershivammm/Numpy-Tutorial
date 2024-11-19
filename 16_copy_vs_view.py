import numpy as np

#####   COPY  #####

var = np.array([1,2,3,4])
co = var.copy()
print("Var Before:-",var)
print("Copy Before:-",co)

#Now Changing the Value of Array and lets see will it change in its copy also ?
var[2]=40
print("Var After:-",var)
print("Copy After:-",co) #Copy will remain same 

#####  VIEW  #####

var1 = np.array([1,2,3,4])
vi= var1.view()
print("Var Before:-",var1)
print("Copy Before:-",vi)

#Now Changing the Value of Array and lets see will it change in its copy also ?
var1[2]=40
print("Var After:-",var1)
print("Copy After:-",vi) #Copy will also get change

#### So This is the major difference between Copy() and View() Function