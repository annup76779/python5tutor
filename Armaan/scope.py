# scopes in python
n = 78

def something():
    n = 81
    print(n)

print(n) # 78
something() # 81
print(n) # 78