"""
Name : Jeff Hwang
User name : jhwa426
ID number : 107793487

Question 3

"""


alphabet = "abcdefghijklmnopqrstuvwxyz"
shift = 6


encrypted_input = input("Enter encrypted string: ")

first_letter = encrypted_input[0]
second_letter = encrypted_input[1]
third_letter = encrypted_input[2]
fourth_letter = encrypted_input[3]

result1 = alphabet[alphabet.find(first_letter)-shift]
result2 = alphabet[alphabet.find(second_letter)-shift]
result3 = alphabet[alphabet.find(third_letter)-shift]
result4 = alphabet[alphabet.find(fourth_letter)-shift]
final_resutl = result1 + result2 + result3 + result4


print()
print("Unencrypted string:", final_resutl)










