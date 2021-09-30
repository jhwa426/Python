import csv

class Ave:
    def __init__(self, scientific_name, common_name, biostatus, classification_hierarchy):
        self.__scientific_name = scientific_name
        self.__common_name = common_name
        self.__biostatus = biostatus
        self.__classification_hierarchy = classification_hierarchy
    def __str__(self):
        return '{}, Status = {}'.format(self.__common_name,self.__biostatus)
    def __repr__(self):
        return 'Ave'+'<'+str(self.__scientific_name)+'>'
    def __lt__(self, other):
        if self.__scientific_name < other.__scientific_name:
            return True
    def __eq__(self, other):
        if self.__scientific_name == other.__scientific_name and self.__common_name == other.__common_name and self.__biostatus == other.__biostatus and self.__classification_hierarchy == other.__classification_hierarchy:
            return True
        return False
    def find_in_classification_hierarchy(self, classification_rank):
        for i in self.__classification_hierarchy:
            if i[0] == classification_rank:
                result = i[-1]
            
                return result
        return None
    
    def lowest_classification_rank(self):
        return self.__classification_hierarchy[0][0]

    def get_scientific_name(self):
        return self.__scientific_name
    def get_common_name(self):
        return self.__common_name
    def get_biostatus(self):
        return self.__biostatus
class BirdDatasetReader:
    def __init__(self, filename):
        self.__csv_filename = filename
    def get_longest_common_name(all_common_names):
        all_common_names = all_common_names.strip()
        if all_common_names == "":
            return None
        else:
            list_ = all_common_names.split("|")
            maxi = list_[0]
            for i in list_:
                i = i.strip()
                if len(i) > len(maxi):
                    maxi= i
        if len(maxi) == 0:
            return None
        else:
            return maxi

    def get_classification_hierarchy(classification_ranks, classifications):
        num = 0
        new = []
        class_ranks = classification_ranks.split("|")
        classificate = classifications.split("|")
        if len(class_ranks) != len(classificate):
            print("ERROR: Invalid input, classification ranks do not match classifications!")
        else:
            while num < len(class_ranks):
                list_ = []
                list_.append(class_ranks[num])
                list_.append(classificate[num])
                tuple_ = tuple(list_)
                new.append(tuple_)
                num+=1
            return new
        return new
    def get_biostatus(biostatus_string):
        case = ["Endemic", "Non-endemic", "Exotic", "Indigenous"]
        biostatus_string = biostatus_string.strip()
        if biostatus_string == "":
            return "N/A"
        else:
            list_ = biostatus_string.split('|')
            ans = ""
            for i in list_:
                if i in case:
                    ans = i
                    break
            if ans == "":
                return "N/A"
            else:
                return ans
    def read_birds_dataset(self):
        new = []
        try:
            csvfile = open(self.__csv_filename, mode='r')
        except FileNotFoundError:
            print("ERROR: File '{}' not found!".format(self.__csv_filename))
            return []
        
        else:
            csv_dict_reader = csv.DictReader(csvfile)
            
            for row in csv_dict_reader:
                scientific = row['ScientificName']
                common_name = BirdDatasetReader.get_longest_common_name(row['VernacularNamesForScientific'])
                if common_name == None:
                    common_name = scientific
                bio = BirdDatasetReader.get_biostatus(row['Biostatus'])
                classification = BirdDatasetReader.get_classification_hierarchy(row['ClassificationRanks'],row['Classification'])
                ave = Ave(scientific, common_name, bio, classification)
                new.append(ave)
            csvfile.close()
            return new





csv_filename = 'NZOR-BirdsTaxonomicExcerpt.csv'
reader = BirdDatasetReader(csv_filename)
all_aves = reader.read_birds_dataset()
all_aves_sorted = sorted(all_aves)
count = 1
print("First 20 aves in file '{}', sorted by scientific name:".format(csv_filename))
for ave in all_aves_sorted[:20]:
    print(count, repr(ave))
    count += 1








        
