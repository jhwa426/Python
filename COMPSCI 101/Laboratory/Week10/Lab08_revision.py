##Q1_revision
def get_letter_from_user():
    user_input = input("Enter a letter: ")
    return user_input.upper()
    

def print_baby_name(letter, baby_names_dictionary):
    for key in baby_names_dictionary:
        if key == letter:
            print(baby_names_dictionary[key])
            



##Test
##def main():
##    baby_boy_names_dictionary = {'A': 'Alex', 'B': 'Benjamin', 'C': 'Connor', 'D': 'Daniel', 'E': 'Ethan', 'F': 'Finn', 'G': 'George', 'H': 'Hunter', 'I': 'Isaac', 'J': 'Joshua', 'K': 'Kingston', 'L': 'Liam', 'M': 'Max', 'N': 'Noah', 'O': 'Oliver', 'P': 'Phoenix', 'Q': 'Quinn', 'R': 'Riley', 'S': 'Samuel', 'T': 'Thomas', 'U': 'Ute', 'V': 'Victor', 'W': 'William', 'X': 'Xavier', 'Y': 'Yukio', 'Z': 'Zachary'}
##    baby_girl_names_dictionary = {'A': 'Abby', 'B': 'Bella', 'C': 'Charlotte', 'D': 'Daisy', 'E': 'Ella', 'F': 'Faith', 'G': 'Grace', 'H': 'Hannah', 'I': 'Isabella', 'J': 'Jade', 'K': 'Kate', 'L': 'Lily', 'M': 'Maddison', 'N': 'Natalie', 'O': 'Olivia', 'P': 'Phoebe', 'Q': 'Q', 'R': 'Rebecca', 'S': 'Samantha', 'T': 'Tayla', 'U': 'Ute', 'V': 'Violet', 'W': 'Willa', 'X': 'Xena', 'Y': 'Yuki', 'Z': 'Zoe'}
##    letter = get_letter_from_user()
##    print_baby_name(letter, baby_boy_names_dictionary)
##    print_baby_name(letter, baby_girl_names_dictionary)
##
##     
##main()


##Q2_revision
def get_filename_from_user():
    user_input = input("Enter a letter: ")
    return user_input


def get_list_of_names(filename):
    input_file = open(filename, "r")
    contents = input_file.read().split()
    input_file.close()
    return contents

def create_baby_names_dict(names_list):
    name_dic = {}
    for name in names_list:
        key = name[0]
        value = name
        name_dic[key] = value
    return name_dic

def display_baby_names(baby_names_dictionary):
    for key in baby_names_dictionary:
        print(key, baby_names_dictionary[key],end = ", ")



####Test
##def main():
##    filename = get_filename_from_user()
##    names = get_list_of_names(filename)
##    baby_names_dictionary = create_baby_names_dict(names)
##    display_baby_names(baby_names_dictionary)
##
##main()
#### baby_boy_names.txt



##Q3_revision
def get_list_of_names(filename):
    input_file = open(filename, "r")
    contents = input_file.read().split()
    input_file.close()
    return sorted(contents)

def create_names_count_dictionary(names_list):
    name_dic = {}
    
    for name in names_list:
        if name not in name_dic:
            name_dic[name] = 1
        else:
            name_dic[name] += 1

    return name_dic

def produce_name_counts_report(name_counts_dict):
    print("Report")
    print("======")
    for key in name_counts_dict:
        print("{} appears {} times".format(key, name_counts_dict[key]))

##Test
##def main():
##    filename = get_filename_from_user()
##    names = get_list_of_names(filename)
##    name_count_dictionary = create_names_count_dictionary(names)
##    produce_name_counts_report(name_count_dictionary)
##
##main()
## top10_boy_names.txt



##Q4_revision
def get_list_of_names(filename):
    input_file = open(filename, "r")
    contents = input_file.read().split()
    input_file.close()
    return sorted(contents)

def create_baby_names_dictionary(names_list):
    name_dic = {}
    
    for name in names_list:
        key = name[0]
        if key in name_dic:
            name_dic[key].append(name)
        elif name not in name_dic:
            name_dic[key] = [name]

    return name_dic



def display_baby_names(baby_names_dict):
    for key in baby_names_dict:
        print("{}: ".format(key), sep="", end = "")
        names_list = baby_names_dict[key]
        for value in range(len(names_list)):
            print(names_list[value],end = " ")
        print()
        


##Test
def main():
    filename = get_filename_from_user()
    names = get_list_of_names(filename)
    baby_name_dictionary = create_baby_names_dictionary(names)
    display_baby_names(baby_name_dictionary)
        
main()
## 2019Top_boy_names.txt
