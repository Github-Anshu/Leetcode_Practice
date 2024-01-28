class Solution:
    def countKeyChanges(self, s: str) -> int:
        count = 0
        last = s[0].lower()
        for i in range(1, len(s)):
            #print(last)
            if s[i].lower() != last:
                count += 1
            last = s[i].lower()
        return count
