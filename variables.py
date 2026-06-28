#PROGRAM  1:
# Print Data type
mark = 95
print(f"Data type of variable: {type(mark)}")


#PROGRAM  2:
#Check data type
height = 5.8
print(f"Data type: {type(height)}")


#PROGRAM  3:
#Combine two string with space
f_name = "John"
l_name = "Smith"
full_name = f_name + " " + l_name
print(full_name)

#PROGRAM  4:
#Check data type
is_student = True
print(type(is_student))



# TYPE CONVERION
#PROGRAM  5:
# Convert integer into  string
n = 150
y = str(n)
print(f"My score is {y}")

#PROGRAM  6:
#Convert float into integer:
num = 45.99
new_n = int(num)
print(new_n)


#PROGRAM  7:
#Convert string into integer
price = "250"
new_price = int(price)
print(f"Price is: {new_price + 50}")

#PROGRAM  8:
#Convert integer into float
x = 9
y = float(x)
print(type(y))


#PROGRAM  9:
#Convert float into string
value = 7.5
new_v = str(value)
print(new_v)


#TRICKEY PRACTICE QUESTIONS:
#PROGRAM  10:
#String → Int → Multiply → String 
value = "75"
new_v = int(value)
n = new_v * 4
result = str(n)
print(f"Final Result: {result}")

#PROGRAM  11:
#String + Integer
a = "20"
b = 30
s = int(a)
sum_n = b + s
print(sum_n)

#PROGRAM  12:
#Float → Int → Boolean
value = 99.99
new_v = int(value)
result = new_v == 100
print(result)

#PROGRAM   13:
#None → String → Int → Subtract
value = None
value = "150"
new_v = int(value)
print(f"Final Result: {new_v -24}")

#PROGRAM  14:
#Mixed Data Types
first = "Cyber"
second = "Security"
number = 101
new_n = str(number)
print(f"{first} {second}  {new_n}")