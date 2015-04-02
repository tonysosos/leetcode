class Solution:
    # @return a string
    def countAndSay(self, n):
        last = '1'
        for i in range(1,n):
            x = last[0]
            num = 0
            count = 0
            new = ""
            while num < len(last):
                if last[num] == x:
                    count += 1
                    if num + 1 == len(last):
                        new += str(count)
                        new += x
                    num += 1
                else:
                    new += str(count)
                    new += x
                    x = last[num]
                    count = 0
            last = new
        return last