"""Problem 217: Contains Duplicate"""

s=set()
        for i in nums:
            if i in s:
                return True
            s.add(i)
        return False
