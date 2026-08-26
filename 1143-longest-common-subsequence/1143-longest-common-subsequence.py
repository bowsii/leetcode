class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp=[0]*len(text1)
        longest = 0
        for i in text2:
            cv=0
            for j,v in enumerate(dp):
                if cv<v:
                    cv=v
                elif i==text1[j]:
                    dp[j]=cv+1
                    longest = max(longest,cv+1)
        return longest
