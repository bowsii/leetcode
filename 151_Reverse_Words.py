"""Problem 151: Reverse Words"""

l=[]
        for i in s.split():
            l.append(i)
        l=l[::-1]
        x=''
        for i in range(len(l)):
            x+=l[i]
            if(i!=len(l)-1):
                x+=" "
        return x
