# Advantage
# short code
# more logical code
# easy to implement when it comes to find the solution complex problems
# used in recursive problem

# n! = n * n-1 * n-2 .... (n-(n-1)))

# forward process
# 1-> n= 5 => on hold
# 2-> n=5-1 => on hold
# 3 -> n= 5-2 => on hold
# 4-> n=5-3 => 2


# reverse procss => 120
# 1-> n= 5 => 5 * ((5-1) * ((5-2) * 2))
# 2-> n=5-1 => (5-1) * ((5-2) * 2)
# 3 -> n= 5-2 => (5-2) * 2
# 4-> n=5-3 => 2

def fact(n):
    if n == 2:
        return 2
    return n * fact(n-1)

print(fact(5))