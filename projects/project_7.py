# PROJECT   7:
#Guess The Number
import random
target = random.randint(1,100)
while True:
	userchoice = int(input("Enter your choice:"))
	if userchoice == target:
		print("Guess the number successfully")
		break
	elif userchoice < target:
		print("Your choice is too small: Please enter the bigger choice")
	else:
		print("Your choice is too big : Please enter the smaller choice")
print("-------End Game-----")
		
