#PROGRAM 11
#Find length using Loop
subject = "Computer Science"
count = 0
for i in subject:
	count += 1
print(f"Total length of string: {count}")


#PROGRAM 12:
#Check start
text = "image.png"
print(f"Is text start with image? {text.startswith('image')}")


#PROGRAM  13:
#Concatenation
word1 = "Good"
word2 = "Morning"
full_word = word1 + " " + word2
print(full_word)

#PROGRAM 14:
#Print full f string statement
Name = "John"
Age = 20
Country = "Canada"
print(f"{Name} is {Age} years old and lives in {Country}")


#PROGRAM 15:
#Print Second and Second last character
text = "Programming"
print(f"Second character: {text[1]}, Second-last Character: {text[-2]}")