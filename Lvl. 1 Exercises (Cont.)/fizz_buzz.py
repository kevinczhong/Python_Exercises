class Solution:
    def fizz_buzz(self, n):
        results = []
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                results.append("fizz buzz")
            elif i % 3 == 0:
                results.append("fizz")
            elif i % 5 == 0:
                results.append("buzz")
            else:
                results.append(i)
        return results

s = Solution()
print(s.fizz_buzz(15))