class Solution:
    # @return an integer
    def trailingZeroes(self, n):
        res = 0
        while n>0:
            n=int(n/5)
            res += n
        return res