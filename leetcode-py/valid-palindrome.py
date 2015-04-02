class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        i = 0
        j = len(s)-1
        if i>=j:
            return True
        while not (s[i].isalpha() or s[i].isdigit()) and i < j:
            i += 1
        while not (s[j].isalpha() or s[j].isdigit()) and j > i:
            j -= 1
        
        while i<j:
            if s[i].upper()!=s[j].upper():
                return False
            else:
                i += 1
                while not (s[i].isalpha() or s[i].isdigit()) and i < j:
                    i += 1
                    
                j -= 1
                while not (s[j].isalpha() or s[j].isdigit()) and j > i:
                    j -= 1
        return True