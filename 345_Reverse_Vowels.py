"""Problem 345: Reverse Vowels"""

s=list(s)
        i=0
        j=len(s)-1
        v='AEIOUaeiou'
        while i<j:
            if s[i] in v:
                if s[j] in v:
                    s[i], s[j] = s[j], s[i]
                    i += 1
                    j -= 1
                else:
                    j-=1
            else:
                i+=1
        s=''.join(s)
        return s
