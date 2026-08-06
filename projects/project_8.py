# PROJECT  8:
# Generate Random Password

import random
import string
val = string.ascii_letters + string.digits+string.punctuation
pass_len = 12
password = " "
for i in range(pass_len):
	password += random.choice(val)
print(f"Your random password is: {password}")
