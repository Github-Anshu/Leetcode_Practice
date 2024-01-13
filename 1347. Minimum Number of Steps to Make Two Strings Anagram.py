class Solution:
    def minSteps(self, s: str, t: str) -> int:

        count = defaultdict(int)
        
        for c in s:
            count[c] += 1
        
        for c in t:
            count[c] = count[c] - 1
        
        s = 0

        for v in count.values():
            s += abs(v)
        return math.ceil(s/2)
