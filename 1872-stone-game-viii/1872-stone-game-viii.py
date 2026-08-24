class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        n = len(stones) 

        p = [stones[0]] * n
        for i in range(1, n):
            p[i] = p[i - 1] + stones[i]

        dp = [0] * n
        dp[-1] = p[-1]

        for i in range(n - 2, 0, -1):
            dp[i] = max(dp[i + 1], p[i] - dp[i + 1])
            
        return dp[1]