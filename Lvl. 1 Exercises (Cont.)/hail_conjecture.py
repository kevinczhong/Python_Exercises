class Solution():
    def collatz(self, n):
        array = [n]
        index = 0
        while array[index] != 1:
            if array[index] % 2 == 0:
                array.append(array[index] // 2)
                index += 1
            else:
                array.append(3 * (array[index]) + 1)
                index += 1
        return len(array) - 1

s = Solution()
print(s.collatz(12))
