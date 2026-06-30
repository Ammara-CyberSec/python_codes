#PROGRAM  1:
#Display corresponding day name using match_case:
day = int(input("Enter day number:"))
match day:
	case 1:
		print("Monday")
	case 2:
		print("Tuesday")
	case 3:
		print("Wednesday")
	case 4:
		print("Thursday")
	case 5:
		print("Friday")
	case 6:
		print("Saturday")
	case 7:
		print("Sunday")
	case _:
		print("Invalid day number")
		

#PROGRAM   2:
#Trafic color light color with action
light_color = input("Enter traffic light color:")
match light_color:
	case  "red":
		print("Stop")
	case "green":
		print("Go")
	case "yellow":
		print("wait")
	case _:
		print("invalid light color")

#PROGRAM  3:
#Fruit name and color using match case
fruit_name = input("Enter fruit name:")
match fruit_name:
	case  "apple":
		print("Red color")
	case "banana":
		print("Yellow color")
	case "mango":
		print("Yellow color")
	case _:
		print("Invalid fruit name")

#PROGRAM  4:
#Grade with an appropriate message
grade = input("Enter your grade:")
match grade:
	case grade if grade == "A":
		print("Excellent ")
	case grade if grade == "B":
		print("Very good")
	case grade if grade == "C":
		print("Good")
	case grade if grade == "D":
		print("Average")
	case grade if grade == "F":
		print("Fail")
	case _:
		print("Invalid grade")

#PROGRAM  5:
#Season with suitable activity 
season = input("Enter season:")
match season:
	case "summer":
		print("Go swimming/ Eat ice cream")
	case "winter":
		print("Drink hot tea")
	case "spring":
		print("Enjoy the flowers")
	case "autumn":
		print("Enjoy the cool weather")
	case _:
		print("Invalid season name")