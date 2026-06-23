"""Problem 242: Valid Anagram"""

if len(s)!=len(t):
            return False

        for ch in s:
            if s.count(ch) != t.count(ch):
                return False
        return True
