##Week 7 timed quiz

##Ex 1
def get_sum_string_lengths(words):
    if len(words) == 0:
        return 0
    else:
        return len(words[0]) + get_sum_string_lengths(words[1:])


##Ex 2
def evaluate_f(number):
    
    if number <= 1:
        return 0
    elif number == 2:
        return 1
    else:
        return evaluate_f(number-1) + evaluate_f(number-2)

##print(evaluate_f(3)) 
##val = evaluate_f(8)
##print(val)




##words = ["This", "is", "a", "test"] # 11
##print(get_sum_string_lengths(words))

##Ex 3
def decimal_to_binary(number):
    if number == 0:
        return 0
    else:
        result = (number % 2 + 10 * decimal_to_binary(number // 2))

        return result



binary_number = decimal_to_binary(4)
print(binary_number)
print(type(binary_number))
                
##def binary_to_decimal(number):
##    if number > 1:
##        binary_to_decimal(number//2)
##    print(number % 2, end = "")
