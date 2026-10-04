class Solution(object):
    def reverse(self, x):
        sign = -1 if x < 0 else 1
        x = abs(x)

        total = 0

        while x > 0:
            digit = x % 10
            total = total * 10 + digit
            x //= 10

        total *= sign

        if total < -2**31 or total > 2**31 - 1:
            return 0

        return total