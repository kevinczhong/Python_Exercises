def max_mountain(s):
    start, end = 0, len(s) - 1
    while start + 1 < end:
        mid = (start + end) // 2
        if s[mid] < s[mid + 1]:
            start = mid
        else:
            end = mid
    if s[start] > s[end]:
        return start
    else:
        return end

test_array = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4]
test_array_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 8]
print(max_mountain(test_array_2))