def binsearch_r(s, t):
    start, end = 0, len(s) - 1
    while start + 1 < end:
        mid = (start + end) // 2
        if s[mid] == t:
            return mid
        elif s[mid] >= s[start]:
            if t >= s[start] and t < s[mid]:
                end = mid
            else:
                start = mid
        else:
            if t <= s[end] and t > s[mid]:
                start = mid
            else: 
                end = mid
    if s[start] == t:
        return start
    if s[end] == t:
        return end
    return -1

array_test = [4, 5, 6, 7, 8, 0, 1, 2]
print(binsearch_r(array_test, 5))

