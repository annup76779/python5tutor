menu = [['burger' , 17.50], ['pasta' , 19.50] , ['pizza' , 22.50] , ['sandwich' , 12.50] , ['ice cream' , 7.50] , ['coffee' , 9.50] , ['iced coffee' , 13.50]]

def print_menu():
    no = 0
    for i in menu:
        print(no , i)
        no += 1

def order_machine():
    
    print_menu()

    id = int(input("What would you like to order? "))
    amount = int(input("How many do you want ?"))

    
    source = menu[id]

    item = source[0]
    price = source[1]

    calc_price = price * amount

    final_price = calc_price * 1.65

    g = open("reciept.txt", "a")
    #item , ": " , price , "|" , calc_price , "|" , final_price , "|"
    g.write(item + ": " + str(price) + " | " + str(calc_price) + " | " + str(final_price) + "\n")
    g.flush()
    

while True:
    order_machine()

    j = input("anything else?").strip()

    if j == "y":
        continue
    elif j == "n" or j == "":
        break







    
