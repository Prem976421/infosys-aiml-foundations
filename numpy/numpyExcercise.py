import numpy as np 

daysAndSteps = [[1,6012],[2,7079],[3,6886],[4,7230],[5,4598],[6,5564],[7,6971],[8,7763],[9,8032],[10,9569]]
newDaysAndSteps = np.array(daysAndSteps)
#   print(np.shape(newDaysAndSteps))

newDaysAndSteps[:,1] = newDaysAndSteps[:,1] + 2000
#print(newDaysAndSteps)

stepsWalkedOver = np.where(newDaysAndSteps[:,1] > 9000)

#print(newDaysAndSteps[stepsWalkedOver]) 

print(np.sort(newDaysAndSteps[:,1]))