class Solution():
    def findbinary(self, n):
        rawbin = "{0:b}".format(n)
        return rawbin

    def isPalindrome(self, n):
        str = self.findbinary(n)
        left, right = 0, len(str) - 1
        while left < right:
            if str[left] != str[right]:
                return False
            else:
                left += 1
                right -= 1
        return True

s = Solution()
print(s.isPalindrome(26))
