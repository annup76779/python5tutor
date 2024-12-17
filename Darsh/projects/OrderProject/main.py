menu = [["burger" , 17.50], ["pasta" , 19.50] , ["pizza" , 22.50] , ["sandwich" , 12.50] , ["ice cream" , 7.50] , ["coffee" , 9.50] , ["iced coffee" , 13.50]]
cart = {}

def displayMenu():
    for index, item in enumerate(menu):
        print(index + 1, item[0],":", item[1])

def selectFromMenu() -> tuple[int, list[str, float]]:
    """
        function to ask for the index of the item, and then return the actual index of the item in menu
        - Return: - int - index of the item in the list
    """
    choice = input("Please choose any item from menu")
    index = -1
    if choice.strip().isnumeric():
        index = int(choice) - 1
    return index, menu[index] if index > -1 and index < len(menu) else None