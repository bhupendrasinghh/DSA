def func(s,left,right):
    if left>=right:
        return True 
    if s[left]!=s[right]:
        return False
    return func(s,left+1,right-1)

class Solution(object):
    def validPalindrome(self, s):
        left=0
        right=len(s)-1
        while left<right:
            if s[left]!=s[right]:
                return func(s,left+1,right)or func(s,left,right-1)
            left+=1
            right-=1
        return True