def findUpperClosest(s, t):
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

def isLeftCloser(s, t, left, right):
    if left < 0:
        return False
    if right >= len(s):
        return True
    return t - s[left] >= s[right] - t

def kClosestNos(s, t, k):
    right = findUpperClosest(s, t)
    left = right - 1
    results = []
    for _ in range(k):
        if isLeftCloser(s, t, left, right):
            results.append(s[left])
            left -= 1
        else:
            results.append(s[right])
            right += 1
    return results

array_test = [1, 3, 4, 5, 6, 7, 8, 9, 20, 21, 25, 27]
print(kClosestNos(array_test, 2, 6))



