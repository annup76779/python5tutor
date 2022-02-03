try:
    var = 1
    print(var)

except NameError as e:
    print(e)

finally:
    print("That's all")