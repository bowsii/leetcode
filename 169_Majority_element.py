"""Problem 169: Majority element"""

nums.sort(reverse=True)
        s=set(nums)
        for i in s:
            if nums.count(i)>len(nums)//2:
                return i
