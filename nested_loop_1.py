# PROGRAM   1:
# Left half pyramid
for i in range(1,6):
	for j in range(i):
		print("*", end=" ")
	print()

# Output	
*
* *
* * *
* * * *
* * * * *


# PROGRAM   2:
# Inverted Left half Pyramid
for i in range(6):
	for j in range(i):
		print(" ",end = " ")
	for j in range(6-i):
		print("*", end=" ")
	print()
	
# Output 
* * * * * *
* * * * *
* * * *
* * *
* *
*

# PROGRAM  3:
# Right half Pyramid
for i in range(1,6):
	for j in range(6-i):
		print(" ", end= " ")
	for j in range(i):
		print("*", end= " ")
	print()
	
# Output
        *
      * *
    * * *
  * * * *
* * * * *

# PROGRAM  4:
# Inverted Right half pyramid
for i in range(6):
	for j in range(6-i):
		print("*",end = " ")
	for j in range(i):
		print(" ",end = " ")
	print()

# Output
* * * * * *
  * * * * *
    * * * *
      * * *
        * *
          *	

# PROGRAM  5:
# Full Pyramid(Centered Pyramid)	
for i in range(1,6):
	for j in range(6-i):
		print(" ",end = " ")
	for j in range((2*i)-1):
		print("*",end = " ")
	print()

# Output
        *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *


# PROGRAM   6:
# Inverted Full Pyramid
for i in range(1,6):
	for j in range(i):
		print(" ",end = " ")
	for j in range(2*(6-i)-1):
		print("*",end =" ")
	print()
	
# Output
* * * * * * * * *
  * * * * * * *
    * * * * *
      * * *
        *