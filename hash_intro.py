def twoSum(s, t):
    hash = {}
    for i in range(len(s)):
        if t - s[i] in hash:
            return [hash[t - s[i]], i]
        hash[s[i]] = i
    return [-1, -1]

test_case = [2, 2, 11, 15]
print(twoSum(test_case, 4))