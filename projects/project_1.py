# PROGECT   1:
# Cafe Managment System
menu = {"Pizza": 100,
"Cofee": 80,
"Bariany":150,
"Sweat": 200,
"Salad":300
}

print("Welcome to Cobra resturant")
print("Pizza : Rs 100 \nCofee : Rs 80 \nBariany :Rs150 \nSweat : Rs 200 \nSalad : Rs 300 ")

total_order = 0
items_1 = input("Enter your first item:")
if items_1 in menu:
	total_order += menu[items_1]
	print(f"Your item {items_1} has been order")
else:
	print("Please order item from available items")

another_items = input("Do you want to order another items? (Yes/No)")
if another_items == "Yes":
	item_2 = input("Enter your second item:")
	if item_2 in menu:
		total_order += menu[item_2]
		print(f"Your item {item_2} has been order")
	else:
		print("This item is not Available")
print(f"Total items amount you will pay: {total_order}")

	