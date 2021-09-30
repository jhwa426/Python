    def read_birds_dataset(self):
        try:
            csvfile = open(self.__csv_filename, mode='r')
            csv_dict_reader = csv.DictReader(csvfile)
            index = 1
            
            for row in csv_dict_reader:
                name = row["ScientificName"]
                number = row["ID"]
                
                ##from Q1 and Q3
                common_name = BirdDatasetReader.__get_longest_common_name(row["VernacularNamesForScientific"])
                biostatus = BirdDatasetReader.__get_biostatus(row["Biostatus"])
                if common_name == None:
                    common_name = name
                if index <= 20:
                    print("{} Ave<{}> {}, Status = {}".format(number, name, common_name, biostatus))
                index += 1

            csvfile.close()
            return []



        except FileNotFoundError:
            print("ERROR: File '{}' not found!".format(self.__csv_filename))
            return []
