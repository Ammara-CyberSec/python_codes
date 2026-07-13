# PROJECT  3:
# Student grade management system
students_grade = { }
def add_students(name,grade):
	students_grade[name] = grade
	print(f"Added {name} with {grade}")
def update_students(name,grade):
	if name in students_grade:
		students_grade[name] = grade
		print(f"Update {name} with {grade}")
	else:
		print(f"{name} is not found")
def delete_students(name):
	if name in students_grade:
		del students_grade[name]
		print(f"{name} is successfuly deleted")
	else:
		print("name is not found")
def display_all_students():
    if students_grade:
        for name, grade in students_grade.items():
            print(f"{name} = {grade}")
    else:
        print("No student found")
def main():
		while True:
			print("\n Student grade management System")
			print("1: Add students")
			print("2: Update students")
			print("3: Delete students")
			print("4: Display all students")
			print("5: Exit")
			choice = int(input("Enter your choice:"))
			if choice == 1:
				name = input("Enter your name:")
				grade = int(input("Enter your grade:"))
				add_students(name,grade)
			elif choice == 2:
				name = input("Enter your name:")
				grade = int(input("Enter your grade:"))
				update_students(name,grade)
			elif choice == 3:
				name = input("Enter your name:")
				delete_students(name)
			elif choice == 4:
				display_all_students()
			elif choice == 5:
				print("Closing Loop")
				break
			else:
				print("Invalid choice")
main()
				
		
	
	
	

