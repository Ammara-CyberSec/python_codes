#PROGRAM    1:
# Bus Pass Eligibility
age = int(input("Enter ypur age:"))
id_card = input("Do you have national id card?")
if age >= 60:
	if id_card == "Yes":
		print("Bus pass Approved")
	else:
		print("National ID card required")
else:
	print("Not eligible due to low age")


#PROGRAM   2:
# Online Course Certificate
course_duration = int(input("Enter your course completed duration:"))
quiz_marks = int(input("Enter your quiz marks:"))
if course_duration == 100:
	if quiz_marks >= 50:
		print("Certificate Issued")
	else:
		print("Low quiz marks")
else:
	print("Not eligible for certificate due to low duration")
	
#PROGRAM   3:
# Hospital Appointment
doctor_schedule = input("Is doctor schedule available?")
fee_consultation = input("Has patient paid the fee consultation?")
if doctor_schedule == "Yes":
	if fee_consultation == "Yes":
		print("Appointment Confirmed")
	else:
		print("Fee is not paid")
else:
	print("Doctor schedule is not available")


#PROGRAM  4:
# Sports Team Selection
fitness_test = input("Is player fitness test passed?")
perf_score = int(input("What is player performance score ?"))
if fitness_test == "Passed":
	if perf_score >= 80:
		print("Selected for team")
	else:
		print("Low performance")
else:
	print("Fitness test is not clear")