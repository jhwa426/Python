"""
Name : Jeff Hwang
User name : jhwa426
ID number : 107793487

Question 5

"""

import random

current_score = 0

print("*" * 45)
print("REACH 100 IN THREE ROUNDS! Initial total:", current_score)
print("*" * 45)
print()


#Round 1
print("Round 1:")

round1_random1 = str(random.randrange(1,7))
round1_random2 = str(random.randrange(1,7))
round1_random3 = str(random.randrange(1,7))
round1_random4 = str(random.randrange(1,7))
round1_random5 = str(random.randrange(1,7))

print("Your dice:", round1_random1, round1_random2, round1_random3, round1_random4, round1_random5, sep=" ")

round1_total = round1_random1 + round1_random2 + round1_random3 + round1_random4 + round1_random5

user_tens1 = int(input("  Tens? "))
stor_tens1 = round1_total[user_tens1 - 1]
user_units1 = int(input("  Units? "))
stor_units1 = round1_total[user_units1 - 1]

dice_value1 = int(stor_tens1)*10 + int(stor_units1)

print("Dice value:", dice_value1)

total_value = current_score + dice_value1

print("Your current total:", total_value)

print()
print()

#Round 2
print("Round 2:")

round2_random1 = str(random.randrange(1,7))
round2_random2 = str(random.randrange(1,7))
round2_random3 = str(random.randrange(1,7))
round2_random4 = str(random.randrange(1,7))
round2_random5 = str(random.randrange(1,7))

print("Your dice:", round2_random1, round2_random2, round2_random3, round2_random4, round2_random5, sep=" ")

round2_total = round2_random1 + round2_random2 + round2_random3 + round2_random4 + round2_random5
user_ten2 = int(input("  Tens? "))
stor_ten2 = round2_total[user_ten2 - 1]
user_units2 = int(input("  Units? "))
stor_units2 = round2_total[user_units2 - 1]

dice_value2 = int(stor_ten2)*10 + int(stor_units2)

print("Dice value:", dice_value2)

current_score = total_value + dice_value2

print("Your current total:", current_score)

print()
print()

#Round 3
print("Round 3:")

round3_random1 = str(random.randrange(1,7))
round3_random2 = str(random.randrange(1,7))
round3_random3 = str(random.randrange(1,7))
round3_random4 = str(random.randrange(1,7))
round3_random5 = str(random.randrange(1,7))

print("Your dice:", round3_random1, round3_random2, round3_random3, round3_random4, round3_random5, sep=" ")

round3_total = round3_random1 + round3_random2 + round3_random3 + round3_random4 + round3_random5
user_ten3 = int(input("  Tens? "))
stor_ten3 = round3_total[user_ten3 - 1]
user_units3 = int(input("  Units? "))
stor_units3 = round3_total[user_units3 - 1]

dice_value3 = int(stor_ten3)*10 + int(stor_units3)

print("Dice value:", dice_value3)
print()

final_score = current_score + dice_value3

output_score = abs(100 - final_score)

print("*" * 29)
print("Your final score:", final_score)
print("You are", output_score, "away from the goal")
print("*" * 29)







