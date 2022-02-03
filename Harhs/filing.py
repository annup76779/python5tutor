"""
we will be taking product id, product name and product price/unit from 
shopkeeper and make a pritty printed list into a text file.
for example:

user input -> id, name, selling price, MRP

1	Haldi			60/unit   discount
2	Moongfali		95/unit	  discount
"""


def make_list(filename: str) -> None:
	"""
		takes the filename as parameter and then writes into the file 
		whatever yourse enters in it.

		Parameter: 
			filename: str: file name of the data list

		Returns: None
	"""
	with open(filename,"a") as data_list_file:
		while True:
			input_line = input()
			if input_line.strip() == "":
				print("Done Taking Input")
				break

			# dummy_lst.append(input_line)
			data = tuple(map(lambda x:x.strip(), input_line.split(",")[:3]))
			product_id = data[0] # product id 
			product_name = data[1] # product name
			price = data[2] # product price
			
			data_list_file.write(f"{product_id} has name '{product_name}' whose price is {price}INR.\n")


# make a trigger function
def main():
	print("Hello Shopkeeper sir!!!")
	print("Please start appending your new products to the data list")
	print("using the format:")
	print("product id, Product Name, Price/unit\n")

	make_list("data_list.txt")


main()