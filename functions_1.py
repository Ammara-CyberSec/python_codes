# PROGRAM   1:
# Print Greeting statement
def say_goodbye():
	print("Goodbye, Friends!")
say_goodbye()
say_goodbye()

# PROGRAM  2:
# Print Square of a number
def square_n(n):
	return n*n
print(f"Sqaure of 6 is: {square_n(6)}")
print(f"Square of 8 is: {square_n(8)}")

# PROGRAM  3:
# Print difference of two numbers
def sub_n(a,b):
	return a - b
print(f"10 - 6 = {sub_n(10,6)}")
print(f"25 - 8 = {sub_n(25,8)}")

# PROGRAM  4:
# Print Cube of a number
def cube_n(n):
	return n*n*n
print(f"Cube of 3: {cube_n(3)}")
print(f"Cube of 5: {cube_n(5)}")

# PROGRAM  5:
# Print Greater value
def max_n(a,b):
	if a > b:
		return a
	else:
		return b
print(f"Greater number is: {max_n(18,9)}")
print(f"Greater number is: {max_n(20,12)}")

# PROGRAM  6:
# Check positive and negative value
def is_positive(n):
	if n > 0:
		return True
	else:
		return False
print(f"Is 7 positive? {is_positive(7)}")
print(f"Is -9 positive? {is_positive(-9)}")

# PROGRAM  7:
# Calculate Discount of a price
def cal_disc(original_price,discount_per):
	Discount = original_price*(discount_per)/100
	Final_price = original_price - Discount
	return Final_price
print(cal_disc(1000,8))

# PROGRAM  8:
# Fahrenhiet to Celcius
def f_to_c(f):
    c = (f - 32) * 5 / 9
    return c
print(f_to_c(45))

# PROGRAM  9:
# Power of a number
def pow_n(b,e):
	return b**e
print(pow_n(2,3))
print(pow_n(4,2))