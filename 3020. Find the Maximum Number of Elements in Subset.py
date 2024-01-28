class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        def helper(num):
            if num == 1:
                if count[num] % 2 == 0:
                    return count[num] - 1
                return count[num]
            length = 0
            while count[num] >= 2:
                num *= num
                length += 1
            if count[num] >= 1:
                return 2*length + 1
            return 2*length - 1
        seen = set(nums)
        count = Counter(nums)
        max_length = 0
        for num in nums:
            max_length = max(max_length, helper(num))
        return max_length

        
        
