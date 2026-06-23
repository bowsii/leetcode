"""Problem 9: IsPalindrome"""

y=str(x)
        l=[]
        for i in y:
            l.append(i)
        z=''
        for i in range(len(l)-1,-1,-1):
            z+=l[i]
        if y==z:
            return True
        else:
            return False
