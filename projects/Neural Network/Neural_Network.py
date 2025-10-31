import numpy as np
import pandas as pd

arr = np.loadtxt("mnist_train.csv",delimiter=",", dtype=str)

testarr=np.copy(arr)
testarr=testarr[0:100]
y=testarr[:,0]
testarr=np.delete(testarr, (0), axis=0)
testarr=np.delete(testarr, (0), axis=1)
testarr=np.array(testarr,dtype=float)
for x in range(99):
    for i in range(784):
        testarr[x,i]=testarr[x,i]/285


weights1=np.zeros((784,16))
for q in range(784):
    for v in range(16):
        weights1[q,v]=np.random.randint(1000)/1000

multarr=np.dot(testarr,weights1)
print(multarr)