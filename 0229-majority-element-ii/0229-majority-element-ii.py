class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if len(nums)<=1:
            return nums
        v=[]

        
        s=set(nums)
        if len(s)==len(nums) and len(nums)>3:
            return []
        for i in s:
            if nums.count(i)>len(nums)//3:
                v.append(i)
        return v
                