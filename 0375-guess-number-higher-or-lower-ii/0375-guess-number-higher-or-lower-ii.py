class Solution:
    def getMoneyAmount(self, n: int) -> int:
        # 1 2 3 4 5 6 7 8 9 10
        # 1 2 3 4 / 6 7 8 9 10
        dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
        # (n+1)*(n+1) metrix
        for lo in range(n, 0, -1):
            for hi in range(lo+1,n+1):
                dp[lo][hi] = min(pivot + max(dp[lo][pivot-1], dp[pivot+1][hi])
                                for pivot in range(lo, hi))
        return dp[1][n]