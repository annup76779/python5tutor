# lets create a function to calculate the average of 4 number

def average(a, b, c, d) -> float:
    '''
        this function calculates the average of 4 numbers
    '''
    total = a + b + c + d
    avg = total / 4
    return avg

avg1 = average(34, 56, 78, 98)
avg2 = average(56, 109, 456, 87)

print(avg1 + avg2)

# parameter
# argument 