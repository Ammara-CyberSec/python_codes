# Assignment no 1
# Project 1
# Python + Numpy  Foundation
import numpy as np
students = {
"Ali": 100,
"Ahmed":89,
"Muhammad":85,
"Zahra":80,
"Samia":88,
"Usama":79,
"Uzair":37,
"Fatima":78,
"Azka":80,
"Sidra":45
}

marks = np.array(list(students.values()))
average = np.mean(marks)
print(f"Average =",average)
higest = np.max(marks)
print(f"Highest marks:",higest)
lowest = np.min(marks)
print(f"Lowest marks:",lowest)

print("\n Passed Students:")
for name,marks in students.items():
	if marks > 50:
		print(f"{name} = {marks}")

print("\n Failed Students")
for name,marks in students.items():
	if marks < 50:
		print(f"{name} = {marks}")
		
print("\n Total Students:", len(students))
print("Average :",average)
print("Lowest marks:",lowest)
print("Higest marks:",higest)

