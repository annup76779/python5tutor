def max_of_three(x, y, z):
    if x > y:
        if x > z:
            return x
        else:
            return z
    else:
        if y > z:
            return y
        else: 
            return z

print(max_of_three(5, 6, 2))