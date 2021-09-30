"""
Lab 7:

"""

def main():
    message = ("For this question you are required to submit\n" +
            "ONE line of text, the line numbered 100 from the\n" +
            "output file created by this program.")
    print(message)

    write_without_blank_lines("Lab07Q06_in.txt", "Lab07Q06_out.txt")


##def write_without_blank_lines(filename_in, filename_out):
##    input_file = open(filename_in, "r")
##    output_file = open(filename_out, "w")
##    contents = input_file.readlines()
##    input_file.close()
##    
##    index = 0
##    number = 1
##    
##    while index < len(contents):
##        element = contents[index]
##        no_line = element.strip()
##
##        if no_line == "":
##            index = index + 1
##        else: 
##            to_print = str(number) + ". " + no_line + "\n"
##            output_file.write(to_print)
##            number = number + 1
##            index = index + 1
##            
##    output_file.close()

##Q6_revision
def write_without_blank_lines(filename_in, filename_out):
    input_file = open(filename_in, "r")
    output_file = open(filename_out, "w")
    contents = input_file.readlines()
    input_file.close()

    index = 0
    number = 1

    while index < len(contents):
        name = contents[index]
        new_line = name.strip()

        if new_line != "":
            result = "{}. {}\n".format(number, new_line)
            output_file.write(result)
            number += 1
        index +=1
            
        
    output_file.close()    

main()








