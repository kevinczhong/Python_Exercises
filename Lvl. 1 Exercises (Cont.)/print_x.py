class Solution():
    def print_x(self, n):
        result = ["X"]
        init_x = "X"
        after_x = " X"
        index = 0
        for i in range(2, n + 1):
            init_x = init_x + after_x
            result.insert(0, init_x)
            result.insert(len(result), init_x)
        return result

s = Solution()
print(s.print_x(3))
        
        
