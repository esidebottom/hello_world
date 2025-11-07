import numpy as np
import pandas as pd

# load mnist training data into arr
arr = np.loadtxt("mnist_train.csv",delimiter=",", dtype=str)

testarr=np.copy(arr)
#shorten the training dataset for testing
testarr=testarr[0:100]
#map the labels to a vector, y
y=testarr[:,0]
#delete the labels and column names
testarr=np.delete(testarr, (0), axis=0)
testarr=np.delete(testarr, (0), axis=1)
#convert string array to float
testarr=np.array(testarr,dtype=float)

#normalise pixel brightness values in input
for x in range(99):
    for i in range(784):
        testarr[x,i]=testarr[x,i]/285

#create weight matrix for first set of neurons - 16 neurons
weights1=np.random.randn(16,784)

#create bias vector
bias1=np.random.randn(16)

#create linear combination of weights and inputs (each column is the full set of weights for that neuron)
multarr=np.dot(testarr,weights1)


