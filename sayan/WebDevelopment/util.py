import os


def get_stock():
    try:
        with open(os.path.join(os.path.dirname(__file__), "static", "stock.txt"), "r") as stock_list:
            stock = []
            for line in stock_list.readlines():
                stock.append(line.split(","))

        return stock
    except IOError:
        print("Error reading file")


def update_stock_list(stock_list: list[float]):
    stock = get_stock()
    try:
        assert len(stock) == len(stock_list)
        with open(os.path.join(os.path.dirname(__file__), "static", "stock.txt"), "w") as stock_file:
            q = 0
            price = 0
            for i in range(len(stock)):
                row = stock[i]
                try:
                    if int(row[-1]) < int(stock_list[i]):
                        return False, None, None
                    row[-1] = str(int(row[-1])- int(stock_list[i]))  # convert the stock into string before saving into the row.
                except ValueError:
                    print("There was some error in the value type of the stock being updated, stock data must be an integer.")
                    return False, None, None
                if int(row[-1]) < 0:
                    row[-1] = "0"
                    stock_list[i] = 0
                q += int(stock_list[i])
                price += int(stock_list[i]) * float(row[1])

                stock_file.write(", ".join(map(lambda x: x.strip(), row)) + "\n")
                row.append(int(stock_list[i]))
        return stock, price, q
    except IOError:
        print("Error reading file")
        return False, None, None

    except AssertionError:
        print("Stock List provided is not matching the actual stock list.")
        return False, None, None


def update_transaction_stock(stock_list, name, price, quantity):
    with open(os.path.join(os.path.dirname(__file__), "static", "transactionlog.txt"), "a") as transaction_file:
        item_count = 0
        for item in stock_list:
            if item > 0:
                item_count += 1
        transaction_file.write(f"Record: {name}, {item_count}, {quantity}, {price}\n")
