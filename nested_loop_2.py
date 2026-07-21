# PROGRAM  1:
# Square Pattern of 5 rows and 5 columns
for i in range(5):
	for j in range(5):
		print("*", end=" ")
	print()

# Output
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
	
	
# PROGRAM  2:
# Rectangle 4 rows and 5 columns
for i in range(4):
	for j in range(7):
		print("*",end = " ")
	print()
	
# Output
* * * * * * *
* * * * * * *
* * * * * * *
* * * * * * *

# PROGRAM  3:
# Left half Pyramid(numbers)
for i in range(1,7):
	for j in range(1,i):
		print(j,end =' ')
	print()

# Output

1
1 2
1 2 3
1 2 3 4
1 2 3 4 5

# PROGRAM  4:
# Left half Pyramid(Same number in each row)
for i in range(1,7):
	for j in range(i):
		print(i, end= " ")
	print()
	
# Output
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
6 6 6 6 6 6

# PROGRAM  5:
# Full centered Pyramid using number
for i in range(1,6):
	for j in range(6-i):
		print(" " ,end = " ")
	for j in range(1,(2*i)):
		print(j,end=" ")
	print()
	
# Output
        1
      1 2 3
    1 2 3 4 5
  1 2 3 4 5 6 7
1 2 3 4 5 6 7 8 9

# PROGRAM  6:
# Diamond  Shape
for i in range(1,6):
	for j in range(6-i):
		print(" ",end=" ")
	for j in range((2*i)-1):
		print("*",end= " ")
	print()
for i in range(2,6):
	for j in range(i):
		print(" ",end= " ")
	for j in range(2*(6-i)-1):
		print("*",end=" ")
	print()

# Output
        *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *
  * * * * * * *
    * * * * *
      * * *
        *
	
