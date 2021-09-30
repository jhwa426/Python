import csv

# Question 01
def get_longest_common_name(vernacular_names):
    common_name_list = []
    if len(vernacular_names) == 0:
        return None
    else:
        position = vernacular_names.split("|")
        count = 0
        name = ""
        
        for word in position:
            space = word.count("  ")

            if len(word) > count and space < 1:
                count = len(word)
                name = word
                
        if count <= 1:
            return None
        else:
            return name

# Question 02
def get_classification_hierarchy(classification_ranks, classifications):
    a_list = []

    count_classification_ranks = classification_ranks.count("|")
    count_classifications = classifications.count("|")

    if count_classification_ranks == count_classifications:
        word_classification_ranks = classification_ranks.split("|")
        word_classifications = classifications.split("|")

        
        for rank, word in zip(word_classification_ranks, word_classifications):
                a_list.append((rank,word))
            
            
    else:
        print("ERROR: Invalid input, classification ranks do not match classifications!")


    return a_list

# Question 03
def get_biostatus(biostatus_string):
    biostatus_cases = ["Endemic","Non-endemic","Exotic","Indigenous"]
    biostatus_string = biostatus_string.split("|")
    
    for word in biostatus_string:
        if word in biostatus_cases:
            return word
    else:
        return "N/A"

# Question 04
class Ave:
    def __init__(self, scientific_name, common_name, biostatus, classification_hierarchy):
        self.__scientific_name = scientific_name
        self.__common_name = common_name
        self.__biostatus = biostatus
        self.__classification_hierarchy = classification_hierarchy

    def get_scientific_name(self):
        return self.__scientific_name

    def get_common_name(self):
        return self.__common_name

    def get_biostatus(self):
        return self.__biostatus

    def __str__(self):
        return "{}, Status = {}".format(self.__common_name, self.__biostatus)

    def __repr__(self):
        return "Ave<{}>".format(self.__scientific_name)

    def find_in_classification_hierarchy(self, classification_rank):
        for word in self.__classification_hierarchy:
            if word[0] == classification_rank:
                return word[-1]
        return None

    def __lt__(self, other):
        if self.__scientific_name < other.__scientific_name:
            return True

    def __eq__(self, other):
        if (self.__scientific_name == other.__scientific_name) and (self.__common_name == other.__common_name) and (self.__biostatus == other.__biostatus) and (self.__classification_hierarchy == other.__classification_hierarchy):
            return True
        else:
            return False
        
    def lowest_classification_rank(self):
##        for word in self.__classification_hierarchy:
##            return word[0]
        
        return self.__classification_hierarchy[0][0]
            


# Question 05
class BirdDatasetReader:
    def __init__(self, csv_filename):
        self.__csv_filename = csv_filename
        self.__bird_list = []

    ### Question 01
    def __get_longest_common_name(vernacular_names):
        common_name_list = []
        if len(vernacular_names) == 0:
            return None
        else:
            position = vernacular_names.split("|")
            count = 0
            name = ""
            
            for word in position:
                space = word.count("  ")

                if len(word) > count and space < 1:
                    count = len(word)
                    name = word
                    
            if count <= 1:
                return None
            else:
                return name
    ### Question 02
    def __get_classification_hierarchy(classification_ranks, classifications):
        a_list = []

        count_classification_ranks = classification_ranks.count("|")
        count_classifications = classifications.count("|")

        if count_classification_ranks == count_classifications:
            word_classification_ranks = classification_ranks.split("|")
            word_classifications = classifications.split("|")

            
            for rank, word in zip(word_classification_ranks, word_classifications):
                    a_list.append((rank,word))
                
                
        else:
            print("ERROR: Invalid input, classification ranks do not match classifications!")


        return a_list
    ### Question 03
    def __get_biostatus(biostatus_string):
        biostatus_cases = ["Endemic","Non-endemic","Exotic","Indigenous"]
        biostatus_string = biostatus_string.split("|")
        
        for word in biostatus_string:
            if word in biostatus_cases:
                return word
        else:
            return "N/A"

    def read_birds_dataset(self):
        try:
            csvfile = open(self.__csv_filename, mode='r')
            csv_dict_reader = csv.DictReader(csvfile)
        
            for row in csv_dict_reader:
                name = row["ScientificName"]
                ##from Q1 and Q3
                common_name = BirdDatasetReader.__get_longest_common_name(row["VernacularNamesForScientific"])
                classification = BirdDatasetReader.__get_classification_hierarchy(row['ClassificationRanks'],row['Classification'])
                biostatus = BirdDatasetReader.__get_biostatus(row["Biostatus"])
                
                if common_name == None:
                    common_name = name
                    
                ave = Ave(name, common_name, biostatus, classification)
                self.__bird_list.append(ave)


            csvfile.close()
            return self.__bird_list


        except FileNotFoundError:
            print("ERROR: File '{}' not found!".format(self.__csv_filename))
            return self.__bird_list


# Question 06
def consistency_check(all_aves):
    index = 0
    count = 0
    for word in all_aves:
        rank = Ave.lowest_classification_rank(word)
        name = Ave.find_in_classification_hierarchy(word,rank)
        scientific_name = Ave.get_scientific_name(word)
        index += 1
        
        if scientific_name != name:
            print('Inconsistency found for bird #{} in the list! {} vs {}'.format(index, scientific_name, name))
            count += 1
            

    if count == 0:
        return True
    else:
        return False



# Question 07
def print_histogram_of_biostatuses(all_aves):
    biostatus_cases = ["Endemic","Non-endemic","Exotic","Indigenous"]
    
    endemic_count = 0
    non_endemic_count = 0
    exotic_count = 0
    indigenous_count = 0
    na_count = 0

    a_dic = {}
    
    for word in all_aves:
        biostatus = Ave.get_biostatus(word)
        if biostatus == "Endemic":
            endemic_count += 1
            a_dic["Endemic"] = endemic_count
        elif biostatus == "Non-endemic":
            non_endemic_count += 1
            a_dic["Non-endemic"] = non_endemic_count
        elif biostatus == "Exotic":
            exotic_count += 1
            a_dic["Exotic"] = exotic_count
        elif biostatus == "Indigenous":
            indigenous_count += 1
            a_dic["Indigenous"] = indigenous_count
        else:
            na_count += 1
            a_dic["N/A"] = na_count

    print("Histogram of biostatus entries:")
    for key in sorted(a_dic):
        space_num = 12
        space = (space_num - len(key)) * " "
  
        print("{}: {}".format(key+space,a_dic[key]))
        
  

# Question 08 
def get_birds_with_specific_classification(all_aves, classification_rank, classification):
    a_list = []

    for word in all_aves:
        name = Ave.find_in_classification_hierarchy(word,classification_rank)
        if name == classification:
            a_list.append(word)
    return a_list
       

# Question 09
def find_bird_by_scientific_name_binary_search(all_aves_sorted, scientific_name):
    max_index = len(all_aves_sorted) - 1
    min_index = 0
    count = 0
    
    while (min_index <= max_index):
        mid_point = (min_index + max_index) // 2
        element = all_aves_sorted[mid_point].get_scientific_name()
        
        if element == scientific_name:
            count += 1
            return all_aves_sorted[mid_point], count
        elif scientific_name < element:
            max_index = mid_point - 1
        elif scientific_name > element:
            min_index = mid_point + 1

        count += 1
        
    return None,0



#### Below are a number of unit tests which your code has to fulfill. If you are interested in how this works, consider
#### looking at the documentation of the Python unittest module. However, you don't have to change anything below here,
#### just make sure that when you execute this class through Python command line or an IDE like IDLE, you receive the
#### message:
#### Ran 2 tests in x.xxx seconds.
#### OK

import unittest

class TestBirdsMethods(unittest.TestCase):

    def test_0_read_csvfile(self):
        csv_filename = 'NZOR-BirdsTaxonomicExcerpt_15only.csv'
        reader = BirdDatasetReader(csv_filename)
        all_aves = reader.read_birds_dataset()
        self.assertEqual(repr(all_aves), "[Ave<Callaeas cinerea>, Ave<Hirundapus>, Ave<Leucocarbo colensoi>, Ave<Egretta alba>, Ave<Vanellus miles>, Ave<Thalasseus>, Ave<Anthus novaeseelandiae>, Ave<Callaeas>, Ave<Rallus pectoralis muelleri>, Ave<Procellaria>, Ave<Emeidae>, Ave<Puffinus puffinus puffinus>, Ave<Phalaropus fulicarius>, Ave<Porzana>, Ave<Anas>]")

    def test_1_find_all_birds(self):
        csv_filename = 'NZOR-BirdsTaxonomicExcerpt.csv'
        reader = BirdDatasetReader(csv_filename)
        all_aves = reader.read_birds_dataset()
        all_aves_sorted = sorted(all_aves)
        largest_number_of_search_steps = -1000
        smallest_number_of_search_steps = 1000
        index = 0
        for ave in all_aves:
            bird, nr_search_steps = find_bird_by_scientific_name_binary_search(all_aves_sorted, ave.get_scientific_name())
            index += 1
            if nr_search_steps > largest_number_of_search_steps:
                largest_number_of_search_steps = nr_search_steps
            if nr_search_steps < smallest_number_of_search_steps:
                smallest_number_of_search_steps = nr_search_steps
        self.assertEqual(largest_number_of_search_steps, 11)
        self.assertEqual(smallest_number_of_search_steps, 1)

if __name__ == "__main__":
    unittest.main(verbosity=0)
