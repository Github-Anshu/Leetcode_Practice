class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        count = defaultdict(int)
        ma = -1
        for n in nums:
            count[n] += 1
            ma = max(ma, count[n])
        ans = 0
        for k, v in count.items():
            if v == ma:
                ans += v
        return ans
