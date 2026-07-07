# PROGRAM  1:
# Replace index 2 to December
months = ["January","February","March","April","May"]
months[2] = "December"
print(months)

# PROGRAM  2:
# Add one items at the end of list
mobile = ["apple","samsung","vivo"]
mobile.append("Oppo")
print(mobile)

# PROGRAM  3:
# Remove one items from list
vegetables = ["Tomato","Onion","pumpkin","Potato"]
vegetables.remove("Potato")
print(vegetables)

# PROGRAM  4:
# Print First and last items
numbers = [3,6,7,9,12]
print(f"First number: {numbers[0]} , Last number: {numbers[-1]}")

# PROGRAM  5:
# Add one items at specific index
countries = ["Pakistan","India","Japan","Chaina"]
countries.insert(2,"Turkey")
print(countries)

# PROGRAM  6:
# Add one items at the end of list
fruits = ["mango","apple","banana","cherry"]
fruits.append("orange")
print(fruits)

# PROGRAM  7:
# Add item at a specific index
fruits = ["mango","apple","banana","cherry"]
fruits.insert(2,"grapes")
print(fruits)

# PROGRAM  8:
# Remove one item from list
fruits = ["mango","apple","banana","cherry"]
fruits.remove("mango")
print(fruits)

# PROGRAM  9:
# Remove one items at a specific index
fruits = ["mango","apple","banana","cherry"]
fruits.pop(3)
print(fruits)

# PROGRAM  10:
# Print first and last items
numbers = [2,3,4,6,8,90,23]
print(f"First number: {numbers[0]}, Last numbers: {numbers[-1]}")

# PROGRAM  11:
# Print list using loop
fruits = ["mango","banana","orange","apple","cherry"]
for i in fruits:
	print(i)

# PROGRAM  12:
# Print list using list with index
fruits = ["mango","banana","orange","apple","cherry"]
for i , fruit in enumerate(fruits):
	print(f"{i}, {fruit}")

# PROGRAM  13:
# Check using membership operator
programming = ["java","C++","C","Python"]
print(f"Check python: {"Python" in programming}")

# PROGRAM  14:
#  Ascending order in list
numbers = [6,3,89,23,90,12,30]
numbers.sort()
print(numbers)

# PROGRAM  15:
# Descending ordee
numbers = [6,3,89,23,90,12,30]
numbers.sort(reverse= True)
print(f"Descending order: {numbers}")

# PROGRAM  16:
# Copy list
list_n = [2,3,4,5,6]
list1 = list_n.copy()
list1.append(8)
print(f"{list_n} \n {list1}")
 
# PROGRAM  17:
# Combine two lists
list1 = [3,4,5,6,7]
list2 = [6,79,12,4]
list_n = list1 + list2
print(list_n)

# PROGRAM  18:
# Count digit
num = [2,10,11,23,10,16]
print(f"Count 10: {num.count(10)}")

# PROGRAM  19:
# Print index of number
names = ["Huzaifa","Ali","Yousaf","Talha"]
print(f"Index of Ali: {names.index('Ali')}")

# PROGRAM  20:
# Clear the list
num = [2,10,11,23,10,16]
num.clear()
print(num)

# PROGRAM  21:
#  Print even and odd number
list_n = [2,34,5,7,90,99,79,67,44,22,36]
even = [ ]
odd = [ ]
for i in list_n:
	if i % 2 == 0:
		even.append(i)
	else:
		odd.append(i)
print(f"Even numbers: {even}")
print(f"Odd numbers: {odd}")

# PROGRAM  22:
# Print largest number
list_n = [2,34,5,7,90,99,79,67,44,22,36]
largest = list_n [0]
for i in list_n:
	if i > largest:
		largest = i
print(largest)

# PROGRAM  23:
# Print smallest number
list_n = [2,34,5,7,90,99,79,67,44,22,36]
smallest = list_n [0]
for i in list_n:
	if i < smallest:
		smallest = i
print(smallest)


