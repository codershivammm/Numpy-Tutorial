import numpy as np

var = np.array([1,2,3,4])
print("Data Type:- " , var.dtype)  #int64

var = np.array([1.2,2.3,3.5,4.8])
print("Data Type:- " , var.dtype)  #float64

var = np.array(["A" ,"B" ,"C"])
print("Data Type:- " , var.dtype)  #U1 Unsigned 

var = np.array(["A","B","C",1,2,3])
print("Data Type:- " , var.dtype)  #U21 Unsigned 

#Changing The Data Type

var = np.array([1,2,3,4] , dtype = np.int8)  #Changes to dt of int8
print("Data Type:- " , var.dtype)  

var = np.array([1,2,3,4] , dtype = np.float64)
print("Data Type:- " , var.dtype)  
print(var)

#Another Method using astype function
var = np.array([1,2,3,4] )  #datatype = int
new_var = var.astype(float)  #changing to float
print("Data Type:- " , new_var.dtype)  #chnaged into float 
print(new_var) # [1. 2. 3. 4.]




