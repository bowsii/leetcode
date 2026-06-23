"""Problem 414: Third maximum number"""

n=list(set(nums))
        n.sort(reverse=True)
        if len(n)>2:
            return n[2]
        else:
            return max(n)
