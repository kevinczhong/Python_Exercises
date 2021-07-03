def find_init_t(s, t):
    start, end = 0, len(s) - 1
    while start + 1 < end:
        mid = (start + end) // 2
        if s[mid] >= t:
            end = mid
        else:
            start = mid
    if s[start] >= t:
        return start
    if s[end] >= t:
        return end
    return len(s)

test_array = [1, 2, 2, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4]
print(find_init_t(test_array, 3))