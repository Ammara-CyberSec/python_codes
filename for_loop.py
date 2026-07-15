# PROGRAM  1:
# Table of 12 from 1 to 10
n = 12
for i in range(1,11):
	result = n*i
	print(f"{n} * {i} = {result}")


# PROGRAM  2:
# Sum of numbers from 1 to 50
total = 0
for i in range(1,51):
	total += i
print(f"Sum of 1 to 50: {total}")

# PROGRAM  3:
# Factorial of 6
n= 6
f = 1
for i in range(1, n +1):
	f *= i
print(f"Factorial of 6: {f}")


# PROGRAM  4:
# Print even number from 2 to 30
for i in range(2,31):
	if i % 2 == 0:
		print(i)

# OR
# Second method
for i in range(2,31,2):
	print(i)


# PROGRAM  5:
# Print Odd nber from 1 to 25
for i in range(1,26):
	if i % 2 != 0:
		print(i)

# OR
# Second method
for i in range(1,26,2):
	print(i)

# PROGRAM  6:
# Print Square of number from 1 to 10
for i in range(1,11):
	print(i*i)

# PROGRAM  7:
# Sum of Even nber from 1 to 100
sum_n = 0
for i in range(1,101):
	if i % 2 == 0:
		sum_n += i
print(sum_n)

# PROGRAM  8:
# Sum of all Odd number from 0 to 100
sum_n = 0
for i in range(1,101):
	if i % 2 != 0:
		sum_n += i
print(sum_n)

# PROGRAM  9:
# Count down 20 to 1
for i in range(20,0,-1):
	print(i)

# PROGRAM  10:
#Count number divisible by 3
count_n = 0
for i in range(1,31):
	if i % 3 == 0:
		count_n += 1
print(count_n)

# PROGRAM  11:
# Print number divisible by both 3 and 5
for i in range(1,51):
	if i % 3== 0 and i % 5 == 0:
		print(i)


# PROGRAM  12:
# Product of number from 1 to 5
pro_n = 1
for i in range(1,6):
	pro_n *= i
print(pro_n)

