class Solution(object):
    def isPalindrome(self, x):
        num=x
        total = 0
        while num > 0:
            id = num % 10
            total = (total * 10 )+ id 
            num = num // 10
        if total == x:
            return True
            
        return False 