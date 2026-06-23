"""Problem 136: Single number"""

res = 0
        for n in nums:
            res ^= n
        return res
