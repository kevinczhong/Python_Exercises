def find_max_rot(s):
    start, end = 0, len(s) - 1
    while start + 1 < end:
        mid = (start + end) // 2
        if s[mid] < s[start]:
            end = mid
        else:
            start = mid
    if s[start] > s[end]:
        return start
    else:
        return end

test_array = [6, 7, 8, 1, 2, 3, 4, 5]
test_array_3 = [9, 1, 2, 3, 4, 5, 6, 7, 8]
print(find_max_rot(test_array_3))