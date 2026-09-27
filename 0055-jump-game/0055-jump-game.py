class Solution:
    def canJump(self, nums: list[int]) -> bool:
        li = len(nums)-1
        for i in range(len(nums)-2,-1,-1):
            if i+nums[i]>= li:
                li = i
        if li == 0:
            return True
        return False