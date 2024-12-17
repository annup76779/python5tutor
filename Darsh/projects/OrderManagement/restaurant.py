file_path = r"projects\OrderManagement\reciept.txt"

def read_new_orders():
    order_file_object = open(file_path, 'r')
    new_orders = []
    orders_lines = order_file_object.readlines()

    for index, order in enumerate(orders_lines):
        if "- delivered" in order.lower():
            continue  # continue the loop and go out of the loop
        new_orders.append([order, index])
    return new_orders


def print_new_orders(new_orders):
    for index, order in enumerate(new_orders):
        print(f"Order {index}", order[0].strip())


def main():
    new_orders = read_new_orders()[: :-1]  # using slicing to reverse list
    processed_orders = []
    print_new_orders(
        new_orders=new_orders
    )

    while all(new_orders):
        print("Process Orders - ")
        index = input("Enter the number: ")
        if index.strip().isnumeric():
            index = int(index)

            # setting order delivered, when user enters the order number, and then save it in the file
            new_orders[index][0] = new_orders[index][0].strip() + "  - delivered"
            processed_orders.append(new_orders[index])
            new_orders[index] = None
        else:
            print("Invalid order number, please enter correct order number.")
            continue

    f_to_update = open(file_path)
    lines = f_to_update.readlines()
    for order, order_number in processed_orders:
        lines[order_number] = order + "\n"

    f_to_update = open(file_path, "w")
    f_to_update.writelines(lines)
    f_to_update.flush()
    f.close()


if __name__ == "__main__":
    main()
