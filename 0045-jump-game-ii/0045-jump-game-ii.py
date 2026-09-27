class Solution:
    def jump(self, nums: list[int]) -> int:
        k = 0
        j = 0
        tj = 0
        while j< len(nums)-1:
            g = 0
            for i in range(k,j+1):
                g = max(g,i+nums[i])
            k = j+1
            j = g
            tj+=1
        return tj