from numpy import random

# wiz = random.randint(2,10)
# pots = random.randint(2,10)
# skill=[]
# mana=[]
# for x in range(wiz):
#     skill.append(random.randint(1,10))
# for x in range(pots):
#     mana.append(random.randint(1,10))
# print(f'skill={skill}')
# print(f'mana={mana}')

skill =[5,4]
mana =[3,2,6,1]
pots=len(mana)
wiz=len(skill)
#create a matrix of times each wizard takes to brew each potion
N = [[x * y for y in skill] for x in mana]
print(f'matrix of times for each wizard to finish each potion {N}')

#add the 0th index of each row to the next row so that the first wizard starts immediately after he finishes each potion
for x in range(pots):
    if x>0:
        N[x][0]=N[x][0]+N[x-1][0]
print(N)

#add the rows up in a running total. This way each row now represents the finish time of each wizard after the starting time in the first index.
for y in range(pots):
    for x in range(wiz):
        if x>0:
            N[y][x]=N[y][x]+N[y][x-1]
print(N)
#make a function that increments each value in a row by 1
def IncrementRow(z):
    for y in range(wiz):
        for x in range(pots):
            if x>z-1:
                N[x][y]+=1

#go through the rows. Increase all the values of the row by 1 when the finish time of wizard n-1 is sooner than wizard n finishes the previous potion
for y in range(1,pots):
    for x in range(wiz-1):
        while N[y][x]<N[y-1][x+1]:
            IncrementRow(y)

print(f"matrix of finish times {N}")
print(f"The wizards will take {N[pots-1][wiz-1]} seconds to finish the potions")




import numpy as np

class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        w=len(skill)
        p=len(mana)
        N = np.array([[x * y for y in skill] for x in mana])
        for x in range(1,p):
            N[x][0]+=N[x-1][0]

        for y in range(p):
            for x in range(1,w):
                    N[y][x]+=N[y][x-1]

        for y in range(1,p):
            for x in range(w-1):
                if N[y][x]<N[y-1][x+1]:
                    v=N[y-1][x+1]-N[y][x]
                    N[y:]+=v

        return(int(N[p-1][w-1]))
        
