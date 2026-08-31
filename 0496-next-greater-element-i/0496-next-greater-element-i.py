class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ngc=[]
        c=0
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i]==nums2[j]:
                    c=j
                    break
            nge=0
            for j in range(c,len(nums2)):
                if nums2[j]>nums1[i]:
                    nge=nums2[j]
                    break
            if nge!=0:
                ngc.append(nge)
            else:
                ngc.append(-1)
        return ngc