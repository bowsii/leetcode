class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if len(nums)==0:
            return 0
        nums = list(set(nums))
        nums.sort()
        i = 1
        c=1
        lcs = 0
        while i<len(nums):
            if nums[i]-1 == nums[i-1]:
                c+=1
                i+=1
            else:
                lcs = max(lcs,c)
                c=1
                i+=1
        lcs = max(lcs,c)
        return lcs
