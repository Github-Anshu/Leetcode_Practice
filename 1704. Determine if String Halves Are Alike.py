class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n = len(s)
        a = 0 
        b = 0
        i=0
        while i < n//2:
            if s[i] in "AEIOUaeiou":
                a += 1
            i += 1
        i=n//2
        while i < n:
            if s[i] in "AEIOUaeiou":
                b += 1
            i += 1
        return a == b
