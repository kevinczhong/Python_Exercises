class Solution():
    def lastwordlen(self, str):
        words = str.split()
        return len(words[-1])

s = Solution()
print(s.lastwordlen("Hello World"))