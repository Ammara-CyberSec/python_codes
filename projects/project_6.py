# PROJECT  6:
# ATM Management System
balance = 5000
print("1: Check Balance")
print("2: Deposite Money")
print("3: Withdraw Money")
print("4: Exit")
choice = int(input("Enter your choice:"))
if choice == 1:
	print(f"Current Balance Rs: {balance}")
elif choice == 2:
	deposit_amount = int(input("Enter your deposit amount:"))
	if deposit_amount > 0:
		balance = balance+deposit_amount
		print(f"Total balance: {balance}")
	else:
		print("Invalid deposit_amount due to negative value")
elif choice == 3:
	withdraw = int(input("Enter withdraw amount:"))
	if withdraw > 0:
		print("Valid amount")
		if withdraw <= balance:
			balance = balance - withdraw
			print(f"Total balance is: {balance}")
		else:
			print("Insufficient balance")
	else:
			print("Invalid amount")
elif choice == 4:
			print("Thankyou for using our ATM")
else:
			print("Invalid choice")
			
			
	