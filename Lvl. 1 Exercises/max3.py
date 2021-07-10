def max3(x, y, z):
    if z > y:
        if y > x:
            return z
        elif y < x:
            if x > z:
                return x
            else:
                return z
    elif z < y:
        if y > x:
            return y
        elif y < x:
            return x

x = 296
y = 3
z = 1

print(max3(x, y, z))