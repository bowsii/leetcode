"""Problem 167: Two Sum"""

i=0
        j=len(numbers)-1
        while i<j:
            s=numbers[i]+numbers[j]
            if s==target:
                return [i+1,j+1]
            if s<target:
                i+=1
            if s>target:
                j-=1
