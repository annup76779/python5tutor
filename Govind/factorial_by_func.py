# Advantage
# short code
# more logical code
# easy to implement when it comes to find the solution complex problems
# used in recursive problem


# n! = n * n-1 * n-2 .... (n-(n-1)))

def fact(n):
    if n == 2:
        return 2
    return n * fact(n-1)

print(fact(5))