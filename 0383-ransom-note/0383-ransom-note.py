class Solution:
    def canConstruct(self, r: str, m: str) -> bool:
        rd = {}
        md = {}

        for i in r:
            rd[i] = rd.get(i, 0) + 1

        for i in m:
            md[i] = md.get(i, 0) + 1

        for i in r:
            if rd[i] > md.get(i, 0):
                return False

        return True