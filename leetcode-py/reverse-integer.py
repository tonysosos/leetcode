class Solution:
    # @param {integer} x
    # @return {integer}
    def reverse(self, x):
        res = 0
        y = abs(x)
        while y!=0:
            res = res*10+y%10
            y = y / 10
        if res >= 2147483648:
            return 0

        if x > 0 :
            return res
        else:
            return res * -1

a = Solution()
print(a.reverse(1534236469))