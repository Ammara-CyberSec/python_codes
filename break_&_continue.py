# PROGRAM  1:
# Print from 1 to 11 but stop at 6
for i in range(1,11):
	if i == 6:
		break
	print(i)

# PROGRAM  2:
# Print 20 to 1 but stop at 15
for i in range(20,0,-1):
	if i == 15:
		break
	print(i)

# PROGRAM  3:
# Print 1 to 100 but stop at first multiple of 9
for i in range(1,101):
	if i % 9 == 0:
		break
	print(i)

# PROGRAM  4:
# Print python but stop at H
for i in "PYTHON":
	if i == "H":
		break
	print(i)

# PROGRAM  5:
# Print 1 to 10 but skip 5
for i in range(1,11):
	if i == 5:
		continue
	print(i)

# PROGRAM 6:
# Print 1 to 20 but Skip all even numbers
for i in range(1,21):
	if i % 2 == 0:
		continue
	print(i)

# PROGRAM  7:
# Print computer but skip p
for i in "COMPUTER":
	if i == "P":
		continue
	print(i)

# PROGRAM  8:
# Print 1 to 20 but skip 5 and stop at 15
for i in range(1,21):
	if i == 5:
		continue 
	print(i)
	if i == 15:
		break

# PROGRAM  9:
# Print 1 to 100 but skip multiple of 3 and stop at 50
for i in range(1,101):
	if i % 3 == 0:
		continue
	print(i)
	if i == 50:
		break

# PROGRAM  10:
# Print programming but skip G and stop at N
for i in "PROGRAMMING":
	if i == "G":
		continue
	print(i)
	if i == "N":
		break