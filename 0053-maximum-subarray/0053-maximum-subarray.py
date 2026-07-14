class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        m=-(10**4)-1
        dp=[0]*len(nums)
       
        for i in range(len(nums)):
            dp[i]=max(nums[i],dp[i-1]+nums[i])
            m=max(m,dp[i])
        return m
