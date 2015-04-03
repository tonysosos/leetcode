class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        start = 0
        max = 0
        l = 0
        se = set()
        for i in range(len(s)):
            if s[i] not in se:
                se.add(s[i])
                l += 1
            else:
                if max < l: max = l
                while (s[i] in se):
                    se.remove(s[start])
                    start += 1
                    l -= 1
                se.add(s[i])
                l += 1
        if max < l: max = l
        return max