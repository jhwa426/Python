"""
Jeff Hwang , 19/03/2020

Prompts the user to enter their name and then displays their name, in uppercase,
as part of a banner

Exercise 1
"""

first_name = input("Enter your first name: ")
output_first_name = first_name.upper()

last_name = input("Enter your family name: ")
output_last_name = last_name.upper()

star = "#" * (len(output_first_name + output_last_name) + 1)

print(star)
print(output_first_name, output_last_name)
print(star)

