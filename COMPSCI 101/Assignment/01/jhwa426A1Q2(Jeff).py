"""
Name : Jeff Hwang
User name : jhwa426
ID number : 107793487

Question 2

"""

import random

print("*" * 45)
print("  University of Auckland Username Generator")    
print("*" * 45)
print()


user = input("Please enter your name: ")
print()

first_name_space = user.find(" ")
first_name_index = user[:first_name_space]
first_name_low = first_name_index[0].lower()

last_name_space = user.rfind(" ")
last_name_index = user[last_name_space+1:]
last_name_low = last_name_index[:3].lower()

random_number = "000" + str(random.randrange(1, 1000, 3))
random_number = random_number[-3:]

reslut = first_name_low + last_name_low + random_number

print("Your username is", reslut)

