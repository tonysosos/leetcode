class Solution:
    # @param n, an integer
    # @return an integer
    def hammingWeight(self, n):
        return bin(n).count("1")