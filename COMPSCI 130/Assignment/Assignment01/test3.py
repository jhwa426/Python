def consistency_check(a_list_of_aves):
    count = 0
    for i in range(len(a_list_of_aves)):
        ave = all_aves[i]
        if Ave.get_scientific_name(a_list_of_aves[i]) != ave.find_in_classification_hierarchy((ave.lowest_classification_rank())):
            count+=1
            print ('Inconsistency found for bird #{} in the list! {} vs {}'.format(i+1,Ave.get_scientific_name(a_list_of_aves[i]),ave.find_in_classification_hierarchy((ave.lowest_classification_rank()))))
    if count == 0:
        return True
    return False




csv_filename = 'NZOR-BirdsTaxonomicExcerpt_15only_erroneous.csv'
reader = BirdDatasetReader(csv_filename)
all_aves = reader.read_birds_dataset()
check_passed = consistency_check(all_aves)
print(check_passed)
