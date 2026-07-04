# PROGRAM  1:
# Check Scholarship Eligibility
marks = int(input("Enter your marks:"))
attendance = int(input("Enter your attendance:"))
if marks >= 75:
	if attendance >= 80:
		print("Eligible for scholarship")
	else:
		print("Attendance is short")
else:
	print("Not eligible")


# PROGRAM   2:
# Check Login Access
username = input("Enter username:")
password = input("Enter password:")
if username == "admin":
	if password == "1234":
		print("Login successful")
	else:
		print("Wrong password")
else:
	print("Login unsuccessful")



# PROGRAM   3:
# Check ATM Withdrawal
acc_balance = int(input("Enter your account balance:"))
withdrawal_amt = int(input("Enter your withdrawal amount:"))
if acc_balance >= 1000:
	if withdrawal_amt <= acc_balance:
		print("Withdrawal successful")
	else:
		print("Withdrawal is not successful")
else:
	print("Insufficient account balance")