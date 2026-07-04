#  PROGRAM  4:
# Age and Driving License 
age = int(input("Enter your age:"))
license = input("Enter your license:")
if age >= 18:
	if license == "12X4YT":
		print("Eligible for driving")
	else:
		print("Invalid license")
else:
	print("Not eligible for driving")

# PROGRAM  5:
# Check Student Result
marks = int(input("Enter your marks:"))
if marks >= 40:
	print("Pass")
	if marks >= 80:
		print("Excellent")
	else:
		print("Good")
else:
	print("Fail")

# PROGRAM  6:
# Electricity Bill discount
elect_bill = int(input("Enter your electricity bill:"))
if elect_bill >= 5000:
	bill = elect_bill - (elect_bill *10/100 )
	print("After 10% discount electric bill is:",bill)
else:
	print("No discount")

# PROGRAM  7:
# Movie Ticket Eligibility
age = int(input("Enter your age:"))
ticket = input("Do you have ticket?")
if age >= 18:
	if ticket == "Yes":
		print("you are allowed to watch a movie")
	else:
		print("Ticket is missing")
else:
		print("Not eligible")


# PROGRAM  8:
# Number Checker
n = int(input("Enter a number:"))
if n > 0:
	print("Number is positive")
	if n % 5 == 0 and n % 10 == 0:
		print("Number is divisible by both 5 and 10")
	else:
		print("Number is not divisible by both 5 and 10")
else:
	if n == 0:
		print("Zero")
	else:
		if n < 0:
			print("Negative number")