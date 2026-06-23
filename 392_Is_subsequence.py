"""Problem 392: Is subsequence"""

i=0
        for ch in t:
            if i < len(s) and s[i]==ch:
                i+=1
        return i==len(s)
