class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        m = len(word1)
        n = len(word2)
        if m != n or set(word1) != set(word2):return False

        count1 = defaultdict(int)
        count2 = defaultdict(int)
        
        for n in word1:
            count1[n]+= 1
        
        for n in word2:
            count2[n]+= 1
        
        c1 = [v for v in count1.values()]
        c2 = [v for v in count2.values()]
        c1.sort()
        c2.sort()
        return c1 == c2
