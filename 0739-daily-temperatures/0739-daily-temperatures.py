class Solution:
    def dailyTemperatures(self, t: List[int]) -> List[int]:
        res = [0]*len(t)
        st = []
        for i,temp in enumerate(t):
            while st and t[st[-1]] < temp:
                idx = st.pop()
                res[idx] = i-idx
            st.append(i)
        return res