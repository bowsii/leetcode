"""Problem 917: Reverse Only letters"""

i=0
        j=len(s)-1
        l=list(s)
        while i<j:
            if l[i].isalpha():
                if l[j].isalpha():
                    l[i],l[j]=l[j],l[i]
                    i+=1
                    j-=1
                else:
                    j-=1
                    
            else:
                i+=1
                
        s=''.join(l)
        return s
