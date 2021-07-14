import re

class Solution():
    def isUpper(self, str):
        left, right = 0, len(str) - 1
        while left < right:
            if str[left].isupper() is True:
                return True
            elif str[right].isupper() is True:
                return True
            else:
                left += 1
                right -= 1
        return False
    
    def UpperFormat(self, str):
        regex = "[a-z]"
        return (re.sub(regex, "", str))
    
    def findLargestUpper(self, str):
        if self.isUpper(str) is False:
            return "NO"
        else:
            largchar = max(self.UpperFormat(str))
            return largchar

s = Solution()
print(s.findLargestUpper("imsorryIMSORRY"))
            
        