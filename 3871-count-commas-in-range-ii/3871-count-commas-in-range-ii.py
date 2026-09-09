class Solution:
    def countCommas(self, n: int) -> int:
        if n < 1000:
            return 0
        tot = 0
        k = 1000

        while n >= k:
            tot += (n - k + 1)
            k *= 1000
        return tot