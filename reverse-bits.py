class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        mask = 0
        for i in range(31):
            mask = mask | (n & 1)
            mask <<= 1
            n >>= 1
        return mask | n