class Solution():
    def maxfloat(self, array):
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
test_array = [1.0, 2.1, -3.3, 4.0, -5.6, 20.0, 100.0, -50.0, 200.0]
print(s.maxfloat(test_array))




            
