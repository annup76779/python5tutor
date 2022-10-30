def digit_counter(number):
    if number // 10 == 0:
        return number %10, [[number % 10, 1]]
    num, lst = digit_counter(number//10)
    if num == number % 10:
        lst[-1][1]+=1
    else:
        lst.append([number % 10, 1])
    return number%10, lst

print(*digit_counter(331))

def readBackNumber(number, i):
    
    for _ in range(i):
        _, counter_lst = digit_counter(number)
        number = 0
        for digit_count in counter_lst:
            num, count = digit_count
            if not number:
                number = count * 10
                number += num
            else:
                number *= 10
                number += count
                number *= 10
                number += num 
        print("next number (iteration %d): %d"%(_, number))


readBackNumber(331, 3)