# PROGRAM  1:
# Cube of a number
cube = lambda x: x*x*x
print(f"Cube of 6 is: {cube(6)}")

# PROGRAM  2:
# Subtraction of two numbers
sub_n = lambda a,b: a - b
print(f"Subtraction of 28 and 9 is: {sub_n(28,9)}")

# PROGRAM  3:
# Reminder of two numbers
divide = lambda a,b: a %b
print(f"Reminder of two numbers: {divide(4,9)}")


# PROGRAM  4:
# Combine two String using "-"
text = lambda s1,s2: s1 + "-" +s2
print(text("Hello","World"))
print(text("Good","Morning"))

# PROGRAM  5:
# Print Greater number
greater = lambda a,b: a > b
n1 = 9
n2 = 11
val = greater(n1,n2)
if val == True:
	print(f"{n1} is greater")
else:
	print(f"{n2} is greater")

# PROGRAM   6:
# Check number is even or odd
check_n = lambda a: a % 2 == 0
n1 = 9
val = check_n(n1)
if val:
	print(f"{n1} is Even")
else:
	print(f"{n1} is Odd")

# PROGRAM  7:
# Check Positive and Negative Number
check_n = lambda x: x > 0
print(check_n(8))

# PROGRAM  8:
# Length of String
text_l = lambda x: len(x)
print(text_l("Hello World"))


# PROGRAM  9:
# String in Uppercase
upper_st = lambda x: x.upper()
print(upper_st("World"))

# PROGRAM  10:
# Print last character of String
last_ch = lambda x: x[-1]
print(f"Last character: {last_ch('Hello')}")

# PROGRAM  11:
# Area of rectangle
rect_area = lambda length,width: length*width
print(f"Area of Rectangle: {rect_area(6,9)}")

# PROGRAM  12:
# Average of three numbers
avg_n = lambda a,b,c:(a+b+c)/3
print(f"Average of three numbers: {avg_n(8,9,7)}")

# PROGRAM  13:
# Two Strings are equal or not
check_l = lambda a,b: a ==  b
n1 = "Good"
n2 = "Morning"
val = check_l(n1,n2)
if val:
	print(f"{n1} and {n2} are equal")
else:
	print(f"{n1} and {n2} are not equal")
	
# PROGRAM  14:
# Sum of square
sq_n = lambda a,b: (a + b)*(a + b)
print(sq_n(2,4))

# PROGRAM  15:
# Add 10 if number greater than 50 ,Otherwise not
check_n = lambda a: a > 50
n1 = 52
val = check_n(n1)
if val:
	print(f"{n1+ 10}")
else:
	print(f"{n1}")

