import numpy as np


a = np.zeros((2, 3))  # 2x3 array of zeros i.e of 2 rows 3 columns
b = np.ones((2,3))    # 2x3 array of ones
c = np.random.rand(2, 3)  # 2x3 array with random values
d = np.arange(1,5)  #Creates an array with a range of numbers from 1 to 4
e = np.linspace(0, 1, 5)  # 5 equally spaced numbers between 0 and 1
f = np.eye(3) #creates an array of 3 rows and 3 columns having Diagonal elements as 1 

print(a)
print(a.ndim)
print(b)
print(b.ndim)
print(c)
print(c.ndim)
print(d)
print(d.ndim)
print(e)
print(e.ndim)
print(f)
print(f.ndim)





