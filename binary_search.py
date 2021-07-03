def binsearch(s, t):
    start, end = 0, len(s) - 1
    while start + 1 < end:
        mid = (start + end) // 2
        if s[mid] == t:
            return mid
        elif s[mid] < t:
            start = mid
        else:
            end = mid
    if s[start] == t:
        return start
    if s[end] == t:
        return end
    return -1 
    

test_array = [1, 2, 3, 4, 5, 6, 7]
test_array_2 = [1, 2, 4, 5, 6, 7, 8, 9, 10, 12, 45, 900]
print(binsearch(test_array, 7))
print(binsearch(test_array_2, 12))
