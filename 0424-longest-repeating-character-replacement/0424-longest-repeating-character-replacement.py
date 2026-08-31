class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        a = 0
        n = len(s)
        for c in range(ord('A'), ord('Z')+1):
            c = chr(c)
            i, j, r = 0,0,0
            while j<n:
                if s[j] == c:
                    j+=1
                elif r < k:
                    j+=1
                    r+=1
                elif s[i]==c:
                    i+=1
                else:
                    i+=1
                    r-=1
                a = max(a,j-i)
        return a