def find_peak_element(s):
    start, end = 0, len(s) - 1
    while start + 1 < end:
        mid = (start + end) // 2
        if s[mid] > s[mid - 1] and s[mid] > s[mid + 1]:
            return mid
        elif s[mid] < s[mid + 1]:
            start = mid
        else:
            end = mid
    if s[start] > s[start + 1] and s[start] > s[start - 1]:
        return start
    if s[end] > s[end + 1] and s[end] > s[end - 1]:
        return end
    return -1

test_array = [1, 2, 1, 3, 4, 5, 7, 6]
print(find_peak_element(test_array))