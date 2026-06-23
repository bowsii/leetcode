"""Problem 125: Valid Palindrome"""

r=''
        for i in s:
            if i.isalpha() or i.isdigit():
               
                r+=i.lower()
        return r == r[::-1]
