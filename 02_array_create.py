import numpy as np

lists = [] 

for i in range(1,5):
    number = int(input("Enter Number:- "))
    lists.append(number)

print(np.array(lists)) #1D Array