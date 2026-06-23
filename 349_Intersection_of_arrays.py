"""Problem 349: Intersection of arrays"""

s=[]
        for i in nums1:
            if i in nums2 and i not in s:
                s.append(i)
       
        return s
