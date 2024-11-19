import numpy as np

#SLICING IN 1-D ARRAY
#var[start:end:step]

var1 = np.array([10,20,30,40,50,60,70,80])
print(var1)
print()
print("start to 60:-",var1[:6])
print("20 to End:-", var1[1:])
print("20 to 60:-", var1[1:6])
print("Alternate Values:-",var1[0:7:2]) #Ek Skip krke Ek value Chaiye to Steps me 2 pass krne honge

#SLICING IN 2-D ARRAY

var2 = np.array([[1,2,3,4],[9,8,7,6],[8,5,2,4]])
                    #0        #1         #2

print(var2)
print("2 to 4 :-",var2[0,1:])
print("8 to 6 :-",var2[1,1:])
print("5 to 4 :-",var2[2,1:])
print("2 to 3 :-",var2[0,1:3])