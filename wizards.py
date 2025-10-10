import numpy as np
#https://leetcode.com/problems/find-the-minimum-amount-of-time-to-brew-potions/?envType=daily-question&envId=2025-10-09
class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        w=len(skill)
        p=len(mana)
        N = np.array([[x * y for y in skill] for x in mana])
        for x in range(1,p):
            N[x][0]=N[x-1][0]
        for y in range(p):
            for x in range(1,w):
                    N[y][x]+=N[y][x-1]
        for y in range(1,p):
            for x in range(w-1):
                if N[y][x]<N[y-1][x+1]:
                    v=N[y-1][x+1]-N[y][x]
                    N[y:]+=v
        return(int(N[p-1][w-1]))
        
