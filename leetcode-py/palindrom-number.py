class Solution:
    # @param {integer} x
    # @return {boolean}
    def isPalindrome(self, x):
        res = 0
        y = abs(x)
        while y!=0:
            res = res*10+y%10
            y = y / 10
#        if res >= 2147483648:
#          return False
        if  res == x:
            return True
        else:
            return False

s = Solution()
print (s.isPalindrome(-2147447412))