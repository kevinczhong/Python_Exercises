def mount_search(s):
    if not s:
        return -1

    low, high = 0, len(s) - 1
    while low < high:
        mid = (low + high) // 2
        if s[mid] < s[mid + 1]:
            low = mid + 1
        else:
            high = mid

    return low

arr_test = [1, 2, 3, 4, 5, 4, 3, 2, 1]
arr_test_2 = [5, 4, 3, 2, 1]
arr_test_3 = [1, 3, 5, 7, 9]
arr_test_4 = []
arr_test_5 = [1]
print(mount_search(arr_test_4))