class Solution:
    def largestRectangleArea(self, hs: List[int]) -> int:
        stack = []
        best = 0
        for i in range(len(hs) +1):
            if i < len(hs):
                h = hs[i]
            else:
                h = 0
            while stack and hs[stack[-1]] >= h:
                height = hs[stack.pop()]
                if stack:
                    left = stack[-1]
                else:
                    left = -1
                best = max(best,height*(i-left-1))
            stack.append(i)
        return best