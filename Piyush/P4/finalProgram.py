class Items:
    item_code_index = {}

    def __init__(self, item_code, name, quantity=0, weight=0, unit='g', price=0.0):
        self.__item_code = item_code
        self.__name = str(name)
        self.__quantity = quantity
        self.__weight = weight
        self.__unit = unit
        self.__price = price

    @classmethod
    def create_object_by_user_input(cls, item_code):
        if item_code in cls.item_code_index:
            print("Error: Item code already exists.")
            return None

        name = input("Enter item name: ")
        quantity = input("Enter quantity (default=0): ")
        weight = input("Enter weight of product (default 0):")
        unit = input("Enter unit of wright (default `gram(g)`): ")
        price = input("Enter price of product (default `0.0`):")

        obj = cls(item_code, name)
        obj.update_quantity(quantity)
        obj.update_price(price)
        obj.update_weight(weight)
        obj.update_weight_unit(unit)
        return obj

    def item_code(self):
        return self.__item_code

    def update_name(self, name):
        self.__name = name

    def update_quantity(self, quantity):
        if isinstance(quantity, str) and quantity.isnumeric():
            self.__quantity = int(quantity)
        elif isinstance(quantity, int):
            self.__quantity = quantity
        else:
            print("Error: Quantity should be numeric.")

    def update_weight(self, weight):
        if isinstance(weight, str) and weight.replace(".", "").isnumeric():
            self.__weight = float(weight)
        elif isinstance(weight, float):
            self.__weight = weight
        else:
            print("Error: Weight should be numeric.")

    def update_weight_unit(self, unit):
        self.__unit = unit

    def update_price(self, price):
        if isinstance(price, str) and price.replace(".", "").isnumeric():
            self.__price = float(price)
        elif isinstance(price, float):
            self.__price = price
        else:
            print("Error: Price should be numeric.")

    # Getter methods
    def get_item_code(self):
        return self.__item_code

    def get_name(self):
        return self.__name

    def get_quantity(self):
        return self.__quantity

    def get_weight(self):
        return self.__weight

    def get_unit(self):
        return self.__unit

    def get_price(self):
        return self.__price

    def print_item_info(self):
        # Create a header row with column names
        headers = ["Item Code", "Name", "Quantity", "Weight", "Price"]

        # Create a row with the values of each instance variable
        values = [
            self.__item_code,
            self.__name,
            self.__quantity,
            f"{self.__weight} {self.__unit}",
            f"${self.__price:.2f}"
        ]

        # Determine the maximum width of each column
        column_widths = [max(len(str(header)), len(str(value))) for header, value in zip(headers, values)]

        # Print the header row
        header_row = " | ".join(header.center(width) for header, width in zip(headers, column_widths))
        print(header_row)
        print("-" * len(header_row))  # Print a separator line

        # Print the values row
        value_row = " | ".join(str(value).center(width) for value, width in zip(values, column_widths))
        print(value_row)


def print_items_data(items_list):
    if not items_list:
        print("No items to display.")
        return

    headers = ["Item Code", "Name", "Quantity", "Weight", "Price"]
    data_rows = []

    for item in items_list:
        data_rows.append([
            item.get_item_code(),
            item.get_name(),
            item.get_quantity(),
            f"{item.get_weight()} {item.get_unit()}",
            f"${item.get_price():.2f}"
        ])

    # Determine column widths
    column_widths = [max(len(str(header)), max(len(str(row[i])) for row in data_rows)) for i, header in enumerate(headers)]

    # Print the header
    header_row = " | ".join(header.center(width) for header, width in zip(headers, column_widths))
    print(header_row)
    print("-" * len(header_row))  # Separator

    # Print each data row
    for row in data_rows:
        print(" | ".join(str(value).center(width) for value, width in zip(row, column_widths)))


def main_menu():
    print("\n#### Emma Bakery - Inventory Management ####")
    print("1. Add New Item")
    print("2. Update Existing Item")
    print("3. Print Inventory")
    print("4. Quit")
    return input("Enter your choice (1-4): ")


def find_item_by_code(database, item_code):
    for item in database:
        if item.get_item_code() == item_code:
            return item
    return None


def update_item(item):
    while True:
        print("\n#### Update Item ####")
        print("1. Update Name")
        print("2. Update Quantity")
        print("3. Update Weight")
        print("4. Update Weight Unit")
        print("5. Update Price")
        print("6. Go Back to Main Menu")
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            new_name = input("Enter new name: ")
            item.update_name(new_name)
            print("Name updated successfully.")
        elif choice == "2":
            new_quantity = input("Enter new quantity: ")
            item.update_quantity(new_quantity)
            print("Quantity updated successfully.")
        elif choice == "3":
            new_weight = input("Enter new weight: ")
            item.update_weight(new_weight)
            print("Weight updated successfully.")
        elif choice == "4":
            new_unit = input("Enter new weight unit: ")
            item.update_weight_unit(new_unit)
            print("Weight unit updated successfully.")
        elif choice == "5":
            new_price = input("Enter new price: ")
            item.update_price(new_price)
            print("Price updated successfully.")
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please enter a valid option.")


def main():
    database = []

    while True:
        user_choice = main_menu()

        if user_choice == "1":
            # Add New Item
            item_code = input("Enter new item code: ")
            if find_item_by_code(database, item_code) is not None:
                print("Error: Item code already exists.")
            else:
                item = Items.create_object_by_user_input(item_code)
                if item is not None:
                    database.append(item)
                    print("Item added successfully.")
        elif user_choice == "2":
            # Update Existing Item
            item_code = input("Enter item code to update: ")
            item = find_item_by_code(database, item_code)
            if item is not None:
                update_item(item)
                print("Item updated successfully.")
            else:
                print("Item not found.")
        elif user_choice == "3":
            # Print Inventory
            print_items_data(database)
        elif user_choice == "4":
            # Quit
            print("Final Inventory:")
            print_items_data(database)
            break
        else:
            print("Invalid choice. Please choose a valid option.")


if __name__ == "__main__":
    main()
