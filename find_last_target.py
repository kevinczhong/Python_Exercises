def find_last_t(s, t):
    start, end = 0, len(s) - 1
    while start + 1 < end:
        mid = (start + end) // 2
        if s[mid] <= t:
            start = mid
        else:
            end = mid
    if s[start] >= t:
        return start
    if s[end] >= t:
        return end
    return len(s)

test_array = [1, 2, 2, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4]
print(find_last_t(test_array, 3))