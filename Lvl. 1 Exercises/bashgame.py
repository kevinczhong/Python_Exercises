def canWin(n):
    if n % 3 == 1:
        return False
    else:
        return True

print(canWin(6))