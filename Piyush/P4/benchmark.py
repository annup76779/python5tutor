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
            self.__weight = float(price)
        elif isinstance(price, float):
            self.__weight = price
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
