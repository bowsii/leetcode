class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return
        si={}
        ti={}
        for i in range(len(s)):
            if s[i] not in si:
                si[s[i]]=i
            if t[i] not in ti:
                ti[t[i]]=i
            if si[s[i]] != ti[t[i]]:
                return False
        return True