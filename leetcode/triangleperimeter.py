import numpy as np
from typing import List
#https://leetcode.com/problems/largest-perimeter-triangle/?envType=daily-question&envId=2025-10-10
nums=[3,6,2,3]
l=len(nums)

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        l=len(nums)
        nums.sort()
        for x in range(l-1,1,-1):
            if nums[x]<nums[x-1]+nums[x-2]:
                print(x)
                return(nums[x]+nums[x-1]+nums[x-2])
            
        return(0)

if __name__ == "__main__":
    sol = Solution()
    print(sol.largestPerimeter([2,1,2]))      # expected 5
    print(sol.largestPerimeter([1,2,1]))      # expected 0
    print(sol.largestPerimeter([1,2,1,10]))    # expected 10