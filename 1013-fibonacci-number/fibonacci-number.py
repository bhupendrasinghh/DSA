def func(num):
        if num==0 or num==1:
            return num
        return func(num-1)+func(num-2)
class Solution(object):
    def fib(self, n):
        # answer = self.func(n)
        return func(n)