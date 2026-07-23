# PROGRAM  1:
# Linear Search
list1 = [10,20,30,50,70,80,90]
target = 50
position = -1
for i in range(len(list1)):
	if  list1[i] == target:
		position = i
		break
if position != -1:
	print(f"{target} is found at index {position}")
else:
	print(f"{target} not found")


# Pseudo Code
START
SET list1
Take target
SET position = -1
FOR i from  0 to n -1  DO
	IF list1[i] == target THEN
		position = i
		break
END FOR
IF position != -1 THEN
	DISPLAY target is found
ELSE:
	DISPLAY target is not found
END

	
		
# PROGRAM  2:
# Find largest number from list				
list1 = [10,30,50,80,90,670]
max_list = list1[0]
for i in list1:
	if i > max_list:
		max_list = i
print(max_list)
	