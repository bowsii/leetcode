"""Problem 11: Max Area"""

ma=0
        left=0
        right=len(height)-1
        while left < right:
            ma=max(ma,(right-left)*min(height[left],height[right]))
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return ma
