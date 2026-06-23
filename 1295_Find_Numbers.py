"""Problem 1295: Find Numbers"""

c=0
        for i in nums:
            if len(str(i))%2==0:
                c+=1
        return c
