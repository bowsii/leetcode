"""Problem 1480: Running sum"""

s=0
        r=[]
        for i in range(len(nums)):
            s=s+nums[i]
            r.append(s)
        return r
