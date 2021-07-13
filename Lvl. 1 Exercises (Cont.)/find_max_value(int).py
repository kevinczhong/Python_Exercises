class Solution():
    def max_value(self, array):
        index = 0
        champion = 0
        while index < len(array):
            if index == 0:
                index += 1
            if index > 0:
                if array[index] > array[champion]:
                    champion = index
                    index += 1
                else:
                    index += 1
        return array[champion]

s = Solution()
test_array = [3, 2, 1, 4, 5]
print(s.max_value(test_array))