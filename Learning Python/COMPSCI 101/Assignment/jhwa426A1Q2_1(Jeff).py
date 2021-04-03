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


first_name, last_name = input("Please enter your name: ").split()
print()

first_name_index = first_name[0].lower()
last_name_index = last_name[:3].lower()
random_number = random.randrange(1, 1000, 3)

print("Your username is ", first_name_index, last_name_index, random_number,sep="")
