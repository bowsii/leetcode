"""Problem 1672: Maximum wealth"""

m = 0
        for i in accounts:
            if sum(i)>m:
                m=sum(i)
        return m
