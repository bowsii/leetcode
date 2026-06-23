"""Problem 189:Rotate"""

n = len(nums)
        
        rotated = [0] * n

        for i in range(n):
            rotated[i] = nums[(i-k)%n]
        
        for i in range(n):
            nums[i] = rotated[i]
