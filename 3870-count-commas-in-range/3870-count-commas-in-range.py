class Solution:
    def countCommas(self, n: int) -> int:
        if n<1000:
            return 0
        else:
            ans = n - 999
            return ans