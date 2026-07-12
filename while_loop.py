# PROGRAM  1:
# Reverse number  from 20 to 1
n = 20
while n >= 1:
	print(n)
	n -= 1

# PROGRAM  2:
# Print all odd number from 1 to 25
i = 1
while i <= 25:
	if i % 2 != 0:
		print(i)
	i += 1

# PROGRAM  3:
# Sum of all even number from 1 to N
n = int(input("Enter a number:"))
i = 1
Sum = 0
while i <= n:
	if i % 2 == 0:
		Sum += i
	i += 1
print(Sum)

# PROGRAM  4:
# Reverse multiplication table
n = 5
i = 10
while i >= 1:
	result = n * i
	print(f"{n} * {i} = {result}")
	i -= 1

# PROGRAM  5:
# Reverse a number
n = int(input("Enter a number:"))
reverse_n = 0
while n > 0:
	digit = n % 10
	reverse_n = (reverse_n * 10) + digit
	n = n// 10
print(reverse_n)


# PROGRAM  6:
# Check Palindrome number
n = int(input("Enter number:"))
original_n = n
reverse_n = 0
while n > 0:
	digit = n % 10
	reverse_n = (reverse_n *10) + digit
	n = n //10
print(reverse_n)
if original_n == reverse_n:
	print("Palindrome")
else:
	print("Not Palindrome")

# PROGRAM  7:
# Find largest digit
n = int(input("Enter number:"))
largest = 0
while n > 0:
	digit = n % 10
	if digit > largest:
		largest = digit
	n = n//10
print(largest)

# PROGRAM  8:
# Find smallest digit
n = int(input("Enter number:"))
smallest = 9
while n > 0:
	digit = n % 10
	if digit < smallest:
		smallest = digit
	n = n //10
print(smallest)

# PROGRAM  9:
# Count The number of Even digits
n = int(input("Enter number:"))
count = 0
while n > 0:
	digit = n % 10
	if digit % 2 == 0:
		count += 1
	n = n//10
print(count)

# PROGRAM  10:
# Product of all digits
n = int(input("Enter nber:"))
product = 1
while n > 0:
	digit = n % 10
	product *= digit
	n = n//10
print(product)

