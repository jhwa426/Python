##Revision question

##Ex 1
##def create_string_len_tuple(words):
##    a_list = []
##    for word in words:
##        a_tuple = (word, len(word))
##        a_list.append(a_tuple)
##        
##    return a_list
##
####Test
##my_list = ['A', 'Big', 'Cat']
##print(create_string_len_tuple(my_list)) #[('A', 1), ('Big', 3), ('Cat', 3)]

##Ex 2
##user_rows = int(input("Enter number of rows: "))
##user_columns = int(input("Enter number of columns: "))
##
##for row in range(-1, user_rows - 1):
##    for column in range(2, user_rows - row):
##        print(" ",end = "")
##    for column in range(1, user_columns + 1):
##        if row != 1 or row != user_rows or column != 1 or column != user_columns:
##            print("*", end = "")
##        else:
##            print(" ", end = "")
##    print()


####Test
####    *****
####   *****
####  *****
#### *****
####*****


##Ex 3
##def create_surnames_dictionary(names):
##    a_dic = {}
##    for name in names:
##        position = name.find(" ")
##        surname = name[position+1]
##        if surname in a_dic:
##            a_dic[surname].append(name)
##            a_dic[surname].sort()
##        else:
##            a_dic[surname] = [name]
##
##    return a_dic
        

####Test
##my_dictionary = create_surnames_dictionary(['Dick Smith', 'Michael Hill'])
##for letter in sorted(my_dictionary.keys()):
##    print(letter, my_dictionary[letter])

####H ['Michael Hill']
####S ['Dick Smith']


##my_dictionary = create_surnames_dictionary(['Dick Smith', 'Michael Hill', 'Ann Cameron', 'Teererai Marange', 'James Finnie-Ansley' , 'Angela Chang', 'Burkhard Wuensche', 'Ragapriya Dhanapal', 'Damir Azhar', 'Adriana Ferraro'])
##for letter in sorted(my_dictionary.keys()):
##    print(letter, my_dictionary[letter])

####A ['Damir Azhar']
####C ['Angela Chang', 'Ann Cameron']
####D ['Ragapriya Dhanapal']
####F ['Adriana Ferraro', 'James Finnie-Ansley']
####H ['Michael Hill']
####M ['Teererai Marange']
####S ['Dick Smith']
####W ['Burkhard Wuensche']


##Ex 4
##filename = input("Enter a filename: ")
##input_file = open(filename, "r")
##contents = input_file.read()
##word_list = contents.split()
##input_file.close()
##
##a_list = []
##for name in word_list:
##    position = name.find(",")
##    first_name = name[position+1:]
##    last_name = name[:position]
##    full_name = first_name + " " + last_name
##    a_list.append(full_name)
##
##print(a_list)
####
####
######Test
######basic_names.txt


####Ex 5
##try:
##    filename = input("Enter a filename: ")
##    input_file = open(filename, "r")
##    contents = input_file.read()
##    word_list = contents.split()
##    input_file.close()
##
##    a_list = []
##    for name in word_list:
##        if "," in name:
##            position = name.find(",")
##            first_name = name[position+1:]
##            last_name = name[:position]
##            full_name = first_name + " " + last_name
##            a_list.append(full_name)
##        
##    
##    print(a_list)
##
##except FileNotFoundError:
##    print("ERROR: The file '{}' does not exist.".format(filename))
    

######Test
##empty.txt
##basic_names.txt

##Ex 6

##def rate(n):
##    total = 0
##    i = 1
##    count = 4
##    while i < n:
##        count += 4
##        j = 0
##        while j < n:
##            count += 3
##            total += j 
##            j += 1
##        i *= 2
##        
##    print("Number of operations:",count)
##
##
##rate(2) #Number of operations: 14
##rate(8) #Number of operations: 88
##rate(64) #Number of operations: 1180
##rate(128) #Number of operations: 2720


##Ex 7 to 12 not included in test 1



##Ex 13










