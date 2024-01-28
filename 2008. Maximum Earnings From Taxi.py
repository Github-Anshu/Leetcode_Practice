class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        dp = {}
        rides.sort()
        n = len(rides)
        def recur(i):
            if i in dp: return dp[i]
            if i >= n:
                return 0
            ans = 0
            ride = rides[i]
            
            idx = bisect.bisect_left(a = rides, x = ride[1], lo = i, key = lambda ride:ride[0])
            ans = ride[1] - ride[0] + ride[2] + recur(idx)
            ans = max(ans, recur(i+1))
            dp[i] = ans
            return ans
        
        return recur(0)
