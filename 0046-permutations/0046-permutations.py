class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        if len(nums)==1:
            return [nums[:]]
        res = []
        for i in range(len(nums)):
            n = nums.pop(0)
            p = self.permute(nums)
        
            for j in p:
                j.append(n)
            res.extend(p)
            nums.append(n)
        return res