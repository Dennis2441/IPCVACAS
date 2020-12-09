import numpy as np
myList = [['Installation', '64%'], ['C2', '14%'], ['NA', '14%'], ['C2', '14%'], ['NA', '14%'], ['na', '7%']]

mylist=np.unique(myList,axis=0)

print (mylist)