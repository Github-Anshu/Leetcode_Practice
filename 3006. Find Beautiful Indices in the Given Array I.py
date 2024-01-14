class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        l = len(s)
        l1 = len(a)
        l2 = len(b)
        
        
        def func1(a, oa, l1):
            for i in range(l - l1 + 1):
                if s[i:i+l1] == a:
                    oa.append(i)
            return oa
        
        oa = func1(a, [], l1)
        ob = func1(b, [], l2)
        #print(oa, ob)
        ans = []
        ans1 = set()
        i = 0
        j = 0
        while i < len(oa) and j < len(ob):
            if abs(oa[i] - ob[j]) <= k:
                ans.append(oa[i])
                i += 1
            elif oa[i] > ob[j]:
                j += 1
            else:
                i += 1
        return ans
