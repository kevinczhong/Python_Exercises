class Solution():
    def isalphanum(self, c):
        if c.isalpha() is True:
            return True
        elif c.isnumeric() is True:
            return True
        else:
            return False

s = Solution()
print(s.isalphanum("a"))
print(s.isalphanum("3"))
print(s.isalphanum("!"))