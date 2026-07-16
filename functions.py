# PROGRAM  1:
# Simple Print greeting
def greet():
	print("Welcome to python")
greet()

# PROGRAM   2:
# Parameter and print greeting
def greet(name):
	print(f"Welcome {name}")
greet("Ali")
greet("Azka")


# PROGRAM  3:
# Parameters and Arguments
def sub_n(a,b):
	subtraction = a - b
	print(f"{a} - {b} = {subtraction}")
sub_n(9,3)

# PROGRAM  4:
# Subtraction of two numbers and then return 
def division_n(a,b):
	result = a/b
	return result
value = division_n(5,6)
print(f"Division of two nbers: {value}")
print(f"Division of 5 and 6: {division_n(5,6)}")

# PROGRAM  5:
# Print Simple text statement
def text():
	return "Python is awesome"
print(text())

# PROGRAM  6:
# Print statement using default value
def greet(city = "Sargodha"):
	print(f"Welcome to {city}")
greet("Mardan")
greet()

# PROGRAM  7:
# Print Area of Rectangle
def rect_area(length,width):
	area = length*width
	return area
print(f"Area of rectangle: {rect_area(4,6)}")

# PROGRAM  8:
# Check even and Odd values
def check(n):
	if n % 2 == 0:
		return True
	else:
		return False
print(check(5))

# PROGRAM  9:
# Print book name with marks
def sub_n(name,marks):
	print(f"{name} = {marks}")
sub_n("physics",90)

# PROGRAM  10:
# Print Average of 3 numbers
def avg_n(a,b,c):
	average = (a + b + c)/3
	return average
print(f"Average of 3 numbers: {avg_n(4,7,8)}")

# PROGRAM  11:
# Print full statement with name and country
def text(name,country = "Pakistan"):
	print(f"{name} is lives in {country}")
text("Ali")
text("Azka","England")

# PROGRAM  12:
# Print Square of a number
def sq_n(n):
	return n*n
print(sq_n(5))

# PROGRAM  13:
# Print Value in uppercase
def text(name):
	return name.upper()
print(text("Azka"))
	
# PROGRAM  14:
# Print and return Largest value
def larg_n(a,b):
	if a > b:
		return a
	else:
		return b
print(f"Largest number is: {larg_n(8,9)}")