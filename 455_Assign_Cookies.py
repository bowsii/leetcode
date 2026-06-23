"""Problem 455: Assign Cookies"""

if len(s)==0:
            return 0
        g.sort()
        s.sort()
        m=0
        ci=len(s)-1
        chi=len(g)-1
        while ci>=0 and chi>=0:
            if s[ci]>=g[chi]:
                m+=1
                ci-=1
                
            chi-=1
        return m
