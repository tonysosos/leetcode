class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        map = {}
        for x in range(len(num)):
            if num[x] in map:
                return map[num[x]]+1, x+1
            else:
                map[target - num[x]] = x