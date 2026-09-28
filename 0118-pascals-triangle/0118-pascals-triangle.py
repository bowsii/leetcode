class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        ans = []
        for j in range(numRows):
            l = [1]
            for i in range(1,j + 1):
                v = l[-1] * (j - i + 1)//i
                l.append(v)
            ans.append(l)
        return ans