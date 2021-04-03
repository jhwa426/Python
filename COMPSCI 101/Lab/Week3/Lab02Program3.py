"""
Jeff Hwang , 

Exercise 3
"""

name_user = input("Enter your name in the first-name middle-name family name : ")

first_space = name_user.find(" ")
first_name = name_user[:first_space]

last_space = name_user.rfind(" ")
last_name = name_user[last_space+1:]

middle_name = name_user[first_space+1:last_space]



print("Your new name is", last_name, middle_name, first_name)


