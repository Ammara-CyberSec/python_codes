# PROGRAM  1:
# Multiple of 3 and non multiple of 3:
list_n = [2,3,5,6,9,67,34,56,90,10,19,18,21]
mult3 = [ ]
non_mult3 = [ ]
for i in list_n:
	if i % 3 == 0:
		mult3.append(i)
	else:
		non_mult3.append(i)
print(f"Multiple of 3: {mult3}")
print(f"Non multiple of 3: {non_mult3}")

# PROGRAM  2:
# Vowels and Consonant:
list_n = ['a','y','h','x','t','c','f','r','i','w','o','a']
vowels = [ ]
consonant = [ ]
for i in list_n:
	if i in "AEIOUaeiou":
		vowels.append(i)
	else:
		consonant.append(i)
print(f"Vowels: {vowels}")
print(f"Consonant : {consonant}")

# PROGRAM  3:
#  Pass and Fail Students Marks:
students_marks = [45,78,90,78,89,23,34,56,12,67]
fail = [ ]
Pass = [ ]
for i in students_marks:
	if i >= 50:
		Pass.append(i)
	else:
		fail.append(i)
print(f"Pass students: {Pass}")
print(f"Fail students: {fail}")

# PROGRAM   4:
# Uppercase words and Lowercase words
fruits = ["apple","MANGO","CHERRY","grapes","banana"]
Upper_words = [ ]
Lower_words = [ ]
for i in fruits:
	if i == i.upper():
		Upper_words.append(i)
	else:
		Lower_words.append(i)
print(f"Upper words: {Upper_words}")
print(f"Lower words: {Lower_words}")

# PROGRAM  5:
# Multiple of 2 and 5
num = [12,45,67,89,15,90,50,12,16,20,40]
mult_both = [ ]
non_mult = [ ]
for i in num:
	if i % 2 == 0 and i % 5 == 0:
		mult_both.append(i)
	else:
		non_mult.append(i)
print(f"Multiple of both 2 and 5: {mult_both}")
print(f"Non multiple of 2 and 5: {non_mult} ")

# PROGRAM  6:
# Single digit and Double digit
num = [2,3,4,7,8,90,23,45,56,777,89,4012,34,56]
single_digit = [ ]
double_digit = [ ]
for i in num:
	if i < 10:
		single_digit.append(i)
	else:
		double_digit.append(i)
print(f"Single digits: {single_digit}")
print(f"Double digits : {double_digit}")

# PROGRAM  7:
# Leap year and not Leap year
years = [2024,2023,2021,2019,2018,2017,2017,2016,2014,2002,1988]
leap_year = [ ]
non_leap_year = [ ]
for i in years:
	if (i % 4 == 0 and i % 100 != 0) or (i %400 == 0):
		leap_year.append(i)
	else:
		non_leap_year.append(i)
print(f"Leap year: {leap_year}")
print(f"Non leap year: {non_leap_year}")

# PROGRAM  8:
# Palindrome  and Non Palindrome
list_n = ["madam","hello","radar","queen"]
palin_words = [ ]
non_palin_words = [ ]
for i in list_n:
	if i == i [: : -1]:
		palin_words.append(i)
	else:
		non_palin_words.append(i)
print(f"Palindrome words: {palin_words}")
print(f"Non palindrome words: {non_palin_words}")

# PROGRAM  9:
# Greater than 100 and Less than 100
num = [23,45,67,777,120,340,560,890,113,156]
greater_100 = [ ]
less_100 = [ ]
for i in num:
	if i >= 100:
		greater_100.append(i)
	else:
		less_100.append(i)
print(f"Greater than 100: {greater_100}")
print(f"Less than 100: {less_100}")

# PROGRAM  10:
# Even length or odd length of words
list_n = ["apple","mango","banana","cherry","grapes"]
even_words = [ ]
odd_words = [ ]
for i in list_n:
	if len(i) % 2 == 0:
		even_words.append(i)
	else:
		odd_words.append(i)
print(f"Even words: {even_words}")
print(f"Odd words: {odd_words}")

# PROGRAM  11:
# Perfect Square and not Perfect Square:
num = [25,16,12,13,34,36,49,81,55,63,28,90,64]
perf_square = [ ]
non_perf_square = [ ]
for i in num:
	if int(i**0.5)**2 == i:
		perf_square.append(i)
	else:
		non_perf_square.append(i)
print(f"Perfect square: {perf_square}")
print(f"Non perfect square: {non_perf_square}")

