"""Problem 485: Consecutive one"""

if set(nums)== {0}:
            return 0
        mc=0
        c=1
        for i in range(1,len(nums)):
            
                if(nums[i]==nums[i-1] and nums[i]==1):
                    c+=1
                else:
                    mc=max(mc,c)
                    c=1
            
        mc=max(mc,c)

        return mc
