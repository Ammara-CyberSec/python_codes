#Arithematic Calculation
n1 = int(input("Enter 1 number:"))
n2 = int(input("Enter 2 number:"))
op = input("Enter operator: +,-,*,/ :")
if op == "+":
	print("Addition of two numbers:",n1 + n2)
elif op == "-":
	print("Subtraction of two numbers:",n1 - n2)
elif op == "*":
	print("Multiplication of two numbers:",n1 * n2)
elif op == "/":
	if n2 != 0:
		print("Division of two numbers:",n1/n2)
	else:
		print("Error! Division by zero is not allowed")
else:
	print("Invalid operator")