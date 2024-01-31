class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        heap = []
        n = len(temp)
        ans = [0 for i in range(n)]
        i = 0
        while i < n:
            while heap and temp[i] > heap[-1][1]:
                ele = heap.pop()
                ans[ele[0]] = i - ele[0]
            heap.append((i, temp[i]))
            i+= 1
        return ans
