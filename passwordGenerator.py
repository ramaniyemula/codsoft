
#APPROACH 1

print("Running approach 1.........")

import string
import random

length = int(input("Enter the length of the password: "))
lower_char = string.ascii_lowercase
upper_char = string.ascii_uppercase
numbers = string.digits
symbols = string.punctuation

all = lower_char + upper_char + numbers + symbols
pwd=random.sample(all,length)
password = "".join(pwd)
print(password)

#--------------------------------------------------------------------------------------------------
#APPROACH 2

print("Running approach 2.........")


import string,random
length=int(input("Enter the length of the password: "))
ch = string.printable

pwd = random.choices(ch, k=length)
print(f"Password: {''.join(pwd)}")