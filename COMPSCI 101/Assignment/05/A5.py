##Assignment 5

##Ex 1

##def split_digits(line):
##    a_list = []
##    for number in line:
##        a_list.append(int(number))
##    return a_list
##    
####Test
##print(split_digits('11155111')) #[1, 1, 1, 5, 5, 1, 1, 1] 
##print(split_digits('11111111')) #[1, 1, 1, 1, 1, 1, 1, 1]


##Ex 2

##def process_file(line):
##    input_file = open(line, "r")
##    contents = input_file.read().split()
##    input_file.close()
##    return contents
    

##Test
##print(process_file("steve.txt")) #['11111111', '11111111', '12222221', '22222222', '23422432', '22255222', '22122122', '22111122']
##print(process_file("steve_palette.txt")) #['1:brown', '2:bisque', '3:white', '4:purple', '5:tan']



    
##Ex 3

##def create_colours_dict(lines):
##    a_dict = {}
##    for name in lines:
##        key = name[:1]
##        value = name[2:]
##        a_dict[key] = value
##        
##    return a_dict
##
## 
####Test
##lines = ['1:brown', '2:bisque', '3:white', '4:purple', '5:tan']
##cd = create_colours_dict(lines)
##for k in sorted(cd.keys()):
##    print(k, cd[k])

##Ex 4

def split_digits(line):
    a_list = []
    for number in line:
        a_list.append(int(number))
    return a_list

def create_pattern_list(lines):
    a_list = []
    for element in lines:
        line = split_digits(element)
        a_list.append(line)

    return a_list    

    




##Test
lines = ['123', '456', '789']
print(create_pattern_list(lines))
lines = ['11221222', '13221121', '14421441', '24412442', '11344221', '21444421', '22444432', '22412411']
print(create_pattern_list(lines)) #[[1, 1, 2, 2, 1, 2, 2, 2], [1, 3, 2, 2, 1, 1, 2, 1], [1, 4, 4, 2, 1, 4, 4, 1], [2, 4, 4, 1, 2, 4, 4, 2], [1, 1, 3, 4, 4, 2, 2, 1], [2, 1, 4, 4, 4, 4, 2, 1], [2, 2, 4, 4, 4, 4, 3, 2], [2, 2, 4, 1, 2, 4, 1, 1]]
lines = ['11111111', '11111111', '12222221', '22222222', '23422432', '22255222', '22122122', '22111122']
print(create_pattern_list(lines)) #[[1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1], [1, 2, 2, 2, 2, 2, 2, 1], [2, 2, 2, 2, 2, 2, 2, 2], [2, 3, 4, 2, 2, 4, 3, 2], [2, 2, 2, 5, 5, 2, 2, 2], [2, 2, 1, 2, 2, 1, 2, 2], [2, 2, 1, 1, 1, 1, 2, 2]]










    
    








    
