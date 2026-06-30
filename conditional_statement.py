#PROGRAM   1:
#Check number is divisible by 3 and 5
num = int(input("Enter a number:"))
if num % 3 == 0 and num % 5 == 0:
	print(num, "is divisible by both 3 and 5")
else:
	print(num,"is not divisible by both 3 and 5")

#PROGRAM    2:
#Check eligibility criteria
age = int(input("Enter your age:"))
if age >= 60:
	print("Eligible for senior citizen discount")
else:
	print("Not eligible for senior citizen discount")


#PROGRAM  3:
#Check number is a three_digits or not
num = int(input("Enter number:"))
if num >= 100 and num <= 999:
	print("Three-digits number")
else:
	print("Not a three-digits number")


#PROGRAM  4:
#Print Greater number 
n1 = int(input("Enter 1 number:"))
n2 = int(input("Enter 2 number:"))
n3 = int(input("Enter 3 number:"))
if n1 >= n2 and n1 >= n3:
	print(n1, "is greater")
elif n2 >= n1 and n2 >= n3:
	print(n2,"is greater")
else:
	print(n3,"is greater")

#PROGRAM   5:
#Check Leap year
year = int(input("Enter year:"))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
	print(year, "is leap")
else:
	print(year, "is not leap")


#PROGRAM   6:
#Check character is vowel or consonant
character = input("Enter a character:")
if character in "AEIOUaeiou":
	print(character,"is vowel")
else:
	print(character ,"is consonant")

#PROGRAM   7:
#Check number is multiple of 10 or not
n = int(input("Enter a number:"))
if n % 10 == 0:
	print(n,"is multiple of 10")
else:
	print(n,"is not multiple of 10")


#PROGRAM  8:
#Check number lies between 50 and 100
n = int(input("Enter a number:"))
if n >= 50 and n <= 100:
	print(n,"lies between 50 and 100")
else:
	print(n,"does not lie between 50 and 100")