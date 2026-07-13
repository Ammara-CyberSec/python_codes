# Project no 2:
# Fake headline generator
import random
subjects = ["Bilawal Bhutto","Maryam Nawaz","Naseem Shah",
"Shahbaz Sharif","Nawaz Sharif",
"Feroz Khan","Wahaj Ali"]
actions = ["Dance with ","Eating mangoes","order","Celebrating","Drink juice","Skating at mountain","Fishing"]
places_or_things = ["a plate of samosa","In shopping Mall","inside parliament","In the court","at the road","in the play ground","in river"]
while True:
	subject = random.choice(subjects)
	action = random.choice(actions)
	place_or_thing = random.choice(places_or_things)
	headline = f"Breaking News: {subject} {action} {place_or_thing}"
	print("\n" + headline)
	user_input = input("Enter your choice: (yes/no)").strip().lower()
	if user_input == "no":
		break
print("\n Thank you for using fake headline generator . Have a fun")
	