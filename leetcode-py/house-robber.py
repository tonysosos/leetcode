class Solution:
    # @param num, a list of integer
    # @return an integer
    def rob(self, num):
        if not num:
            return 0
        n = len(num)
        res = [0]*n
        res[0] = num[0]
        if n==1:
            return num[0]
        res[1] = max(num[0],num[1])
        for i in range(2,n):
            res[i] = max(res[i-2]+num[i], res[i-1])
        return res[n-1]