'''item_list = ['apple','banana','milk','soap','cucumber','cabbage']
studentMarks = [89,90,67,78,70,82,93]
for i in range(len(studentMarks)):
    studentMarks[i]+=5
print(studentMarks)'''
import numpy as np

bikeName = ['suzuki ninja kawasaki v7', 'RE continental GT 650', 'RE classic 350','honda monkey','suzuki haybusa']
bikeHorsePower = [110,90,140,160,105]
bikeAcceleration = [19,12,21,11,18]

bikeInfoArr = np.array([bikeName,bikeHorsePower,bikeAcceleration])

meanOfHorsePower = np.array(bikeHorsePower)

# print(meanOfHorsePower[np.argmin(meanOfHorsePower)]) 

# print(meanOfHorsePower[np.argmin(meanOfHorsePower)]) 

# also .dtype() function helps in finding the datatype of numpy array just use np.array(listName, dtype ='dataType')
# .min and .max functions returns the actual min and max values
# .argmin and .argmax returns index
# .array function creates an numpy array out of python lists the nonhomogeneous datatypes are converted back to string
# x = np.where(meanOfHorsePower > 150)
# print(x)
# print(meanOfHorsePower[x])

# . where() helps in quering our array which returns the index/in format of tuple

###filtering###

#filterArray = meanOfHorsePower > 130

# output of filterArray = [ True False  True  True  True]

#print(meanOfHorsePower[filterArray])

# here using filtering we can create an logical array of an existing numpy array 

###sorting###
#meanOfHorsePower.sort() @this sorts the original array 

#newSortedArray = np.sort(meanOfHorsePower)
# print(newSortedArray)

# Numpy provides various mathematical functions such as sum(), add(), sub(), log(), sin() etc. which uses vectorization.

###broadcasting##

# Array 1
array1=np.array([5, 10, 15])
# Array 2
array2=np.array([5])
array3= array1 * array2 
print(array3)
