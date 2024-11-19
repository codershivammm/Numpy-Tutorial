import numpy as np

#Creates a Array of 2Rows and 3Columns with Random Values
a = np.random.rand(2,3)
print(a)

#Creates an Array of 2 Rows and 3 Columns with Random Values But Both Neagtive and Positive
b = np.random.randn(2,3)
print(b)


#np.random.randint(min , max , total_value ) 
c = np.random.randint(1,10,5)  # 1 se 10 ke beech me 5 random number ka 1D Array Banega
print(c)