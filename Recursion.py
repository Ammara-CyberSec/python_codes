# PROGRAM  1:
# Print number from 1 to 10
def count(n):
	if n >= 10:
		return n
	print(n)
	return count(n +1)
print(count(1))

# PROGRAM  2:
# Print number 10 to 1
def count(n):
	if n== 1:
		return n
	print(n)
	return count(n - 1)
print(count(10))


# PROGRAM   3:
# Sum of Natural number
def sum_n(n):
	if n == 1:
		return n
	return n + sum_n(n-1)
print(sum_n(5))

# OR
# Second Method
def sum_n(n):
	sum_f = 0
	if n == 1:
		return n
	sum_f += n
	return sum_f+sum_n(n-1)
print(sum_n(5))


# PROGRAM  4:
# Product of Natural number
def pro_n(n):
	if n == 1:
		return n
	return n*pro_n(n-1)
print(pro_n(5))


# OR
# Second mathod
def pro_n(n):
	pro_f = 1
	if n == 1:
		return n
	pro_f *= n
	return pro_f*pro_n(n-1)
print(pro_n(5))


# PROGRAM  5:
# Sum of digits in Number
def sum_d(n):
	sum_n = 0
	if n < 10:
		return n
	digit = n % 10
	sum_n += digit
	return sum_n + sum_d(n//10)
print(sum_d(234))


# PROGRAM  6:
# Count number of digits in a number
def count_n(n):
	count = 0
	if n < 1:
		return n
	count += 1
	return count + count_n(n//10)
print(count_n(12346))


# PROGRAM  7:
# Reverse of a number
def rev_n(n,rev = 0):
	if n == 0:
		return rev
	digit = n % 10
	rev = (rev*10) +digit
	return rev_n(n//10,rev)
print(rev_n(523))


# PROGRAM  8:
# Power of a number
def pow_n(b,e):
	if e == 0:
		return 1
	return b*pow_n(b,e-1)
print(pow_n(5,2))
