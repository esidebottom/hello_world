#https://leetcode.com/problems/taking-maximum-energy-from-the-mystic-dungeon/?envType=daily-question&envId=2025-10-10
class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        dp = [0] * len(energy)
        for i in range(len(energy) - 1, -1, -1):
            dp[i] = energy[i]
            if i + k < len(energy):
                dp[i] += dp[i + k]
        return max(dp)