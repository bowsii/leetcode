"""Problem 2529: Maximum Count"""

p=0
        n=0
        for i in nums:
            if i<0:
                n+=1
            if i>0:
                p+=1
        return max(p,n)
