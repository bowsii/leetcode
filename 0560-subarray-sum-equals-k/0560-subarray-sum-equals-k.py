class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        seen = {0:1}
        t=c=0
        for n in nums:
            t+=n
            if t-k in seen:
                c+=seen[t-k]
            seen[t] = 1+seen.get(t,0)
        return c
