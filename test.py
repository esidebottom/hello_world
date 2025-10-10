import numpy as np
energy =[8,-5]
k = 1
i=np.zeros((len(energy)))
for x in range(0,len(energy)):
    for y in range(0,len(energy),3):
        print(x,y)
        if x+y<len(energy):
            i[x]+=energy[x+y]
print(i)

