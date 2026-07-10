# PROGRAM   1:
# Dictionary of Student
student = {"name":"Ali","marks":4000}
student.update({"grade":"A+","city":"Lahore"})
student["marks"] = 4500
print(student)

# PROGRAM  2:
# Product Dictionary and del the category
product = {"name":"scan pen","price":2000,"quantity":"Well","category":"Adult"}
del product["category"]
print(product)

# PROGRAM  3:
# Movie Dictionary and print value and keys seperate in one line
movie = {"mov1":"Taxila Gate","mov2":"Animal","mov3":"Dune"}
value = [ ]
key = [ ]
for i in movie.keys():
	key.append(i)
print(key)
for i in movie.values():
	value.append(i)
print(value)

# PROGRAM  4:
# Country Dictionary and print values and keys
country = {"country1":"Pakistan","country2":"India","country3":"Iran","country4":"Japan"}
for i,val in country.items():
	print(f"{i} = {val}")

# PROGRAM   5:
# Computer Dictionary and Ram
computer = {"brand":"Dell","processor":"icore9","ram":"17GB"}
if "ram" in computer:
	print(f"Found: {computer['ram']}")
else:
	print("Not Found")

# PROGRAM  6:
# Student Dictionary  and Add  Semester 
student = {"name":"Ali","gpa":"3.8","department":"IT"}
student["semester"] = 1
print(student)

# PROGRAM   7:
# Library Dictionary and Removed  1 key
library = {"book1":"Math","book2":"Computer","book3":"Physics","book4":"Islamic studies"}
removed = library.pop("book1")
print(f"Removed book: {removed}")

# PROGRAM  8:
# Marks Dictionary and sum of all marks
marks = {"math":200,"English":300,"Physics":600}
sum = 0
for i in marks.values():
	sum += i
print(f"Sum of all marks: {sum}")

# PROGRAM  9:
# Prices Dictionary and Print greater than 100 marks
prices = {"scan pen":2500,"book":80,"pencil":50,"eraser":150}
greater = [ ]
for i in prices.values():
	if i > 100:
		print(i)

# PROGRAM  10:
# Employee and Print Only All keys
employees = {"Ali":2300,"Zahra":3400,"Talha":67000}
for i in employees.keys():
	print(i)