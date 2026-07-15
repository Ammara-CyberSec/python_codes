# PROJECT   5:
# Library Management System
library = { } 
def add_books(book,name):
	library[book] = name
	print(f"Added {book} by {name}")
def delete_book(book):
	if book in library:
		del library[book]
		print(f"{book} is successfuly deleted ")
	else:
	 print(f"{book} not found")
def search_book(book):
	if book in library:
		library[book]
		print(f"{book} found")
	else:
		print(f"{book} is not found")
def display_all_books():
	for book,name in library.items():
		print(f"{book} = {name}")
def main():
	while True:
		print(f"\n Library Management System")
		print("1: Add a new book")
		print("2: Delete a Book")
		print("3: Search for a book")
		print("4: Display all Books")
		print("5: Exit")
		choice = int(input("Enter your choice:"))
		if choice == 1:
			book = input("Enter your book:")
			name = input("Enter your book name:")
			add_books(book,name)
		elif choice == 2:
			book = input("Enter your book:")
			delete_book(book)
		elif choice == 3:
			book = input("Enter your book:")
			search_book(book)
		elif choice == 4:
			display_all_books()
		elif choice == 5:
			print("Loop Closing")
			break
		else:
			print("Invalid choice")
main()
			
			
			
			
			
	
	
	
	
	
	
	

	
		
		
		
	
		
		
	
		
		
	
		
	
		
		
	
		
	