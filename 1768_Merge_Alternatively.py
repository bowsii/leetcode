"""Problem 1768: Merge Alternatively"""

i=0
        j=0
        m=''
        while i<len(word1) or j<len(word2):
            if i<len(word1):
                m+=word1[i]
                i+=1
            if j<len(word2):
                m+=word2[j]
                j+=1
        
        return m
