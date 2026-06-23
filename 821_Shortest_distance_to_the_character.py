"""Problem 821: Shortest distance to the character"""

l=[]
        r=[]
        for i in range(len(s)):
            if s[i]==c:
                r.append(i)
        j=0
        for i in range(len(s)):
            if i in r:
                l.append(0)
            
            else:
                min=max(l)
                for j in range(len(r)):
                    if abs(i-j)<min:
                        min=abs(i-j)
                l.append(min)
        return l
