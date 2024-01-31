class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        n = len(secret)
        countS = defaultdict(int)
        countG = defaultdict(int)
        bull = 0
        cow  = 0

        for s, g in zip(secret, guess):
            if s == g:
                bull+= 1
            else:
                countS[s]+= 1
                countG[g]+= 1
            
        for k in countS.keys():
            if countG[k] > 0:
                cow+= min(countG[k], countS[k])

        return str(bull)+"A"+str(cow)+"B"
