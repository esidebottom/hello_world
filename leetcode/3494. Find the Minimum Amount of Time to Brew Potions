import numpy as np
#https://leetcode.com/problems/find-the-minimum-amount-of-time-to-brew-potions/?envType=daily-question&envId=2025-10-09

class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        w=len(skill)
        p=len(mana)
        N = np.array([[x * y for y in skill] for x in mana]) #create a matrix of potion completion times
        for x in range(p):
            for y in range(1,w):
                N[x][y]+=N[x][y-1]
        for x in range(1,p):
            N[x]+=N[x-1][0]
        for x in range(1,p):
            for y in range(w-1):
                if N[x][y]<N[x-1][y+1]:
                    v=N[x-1][y+1]-N[x][y]
                    N[x:]+=v
        return(int(N[p-1][w-1]))
        
