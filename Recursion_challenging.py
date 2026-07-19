# PROGRAM  1:
# Palindrome with numbers
def reverse_n(n,rev= 0):
	if n == 0:
		return rev
	digit = n % 10
	rev =(rev*10) + digit
	return reverse_n(n//10,rev)
n = [123,121,232,456,678]
for i in n:
	if reverse_n(i) == i:
		print(f"{i} Palindrome")
	else:
		print(f"{i} not Palindrome")


# PROGRAM   2:
# Palindrome with Strings
def palindrome(s):
	if len(s) <= 1:
		return True
	if s[0] != s[-1]:
		return False
	return palindrome(s[1 : -1])
print(palindrome("madam"))
print(palindrome("radar"))
print(palindrome("hello"))


# PROGRAM  3:
# Fibonacci
def fib(n):
	if n == 0:
		return 0
	if n == 1:
		return 1
	return fib(n - 1) + fib(n-2)
print(fib(4))