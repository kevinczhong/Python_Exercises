def big_array_search(s, t):
    k = 2
    start, end = 0, k
    while s[end - 1] < t:
        k = k * 2
        start = end
        end = k
        if end > len(s) - 1:
            end = len(s) - 1
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

test_case = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
print(big_array_search(test_case, 19))