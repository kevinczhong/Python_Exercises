class Solution():
    def gen_array_list(self, n):
        array = []
        for i in range(1, n + 1):
            array.append(i)
        return array

s = Solution()
print(s.gen_array_list(15))