class Solution:
    def earliestSecondToMarkIndices(self, nums: List[int], indices: List[int]) -> int:
        N = len(nums)
        M1 = len(indices)

        def isValid(M):
          lastOccur = {}
          #index:second
          for i in reversed(range(M)):
            if indices[i] not in lastOccur:
              lastOccur[indices[i]] = i + 1
          
          if len(lastOccur) < N: return False

          #second, index
          last = sorted([[s, i] for i, s in lastOccur.items()])
          spent = 0
          for s, i in last:
            req = nums[i - 1] + 1
            if req + spent > s:return False
            spent+= req
          return True
        
        # for M in range(1, M1 + 1):
        #   if isValid(M): return M
        left = 1
        right = M1
        ans = -1
        while left <= right:
          mid = (left + right)//2
          if isValid(mid):
            ans = mid
            right = mid - 1 
          else:
            left = mid + 1
        return ans
