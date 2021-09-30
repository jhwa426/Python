##Test A1

### Question 01
##def get_longest_common_name(vernacular_names):
##    common_name_list = []
##    if len(vernacular_names) == 0:
##        return None
##    else:
##        position = vernacular_names.split("|")
##        count = 0
##        name = ""
##        
##        for word in position:
##            space = word.count("  ")
##
##            if len(word) > count and space < 1:
##                count = len(word)
##                name = word
##                
##        if count <= 1:
##            return None
##        else:
##            return name
##            
##
##  
##
##
####Test
##all_common_names = "Red Phalarope|Grey (Red) Phalarope"
##print(get_longest_common_name(all_common_names)) #Grey (Red) Phalarope
##
##all_common_names = ""
##print(get_longest_common_name(all_common_names)) #None
##
##all_common_names = "Spur-winged Plover|Masked Plover|Spur-winged plover|Masked Plover"
##print(get_longest_common_name(all_common_names)) #Spur-winged Plover
##
##all_common_names = "   "
##print(get_longest_common_name(all_common_names)) #None
##
##all_common_names = " |  ||"
##print(get_longest_common_name(all_common_names)) #None

### Question 02
##def get_classification_hierarchy(classification_ranks, classifications):
##    a_list = []
##
##    count_classification_ranks = classification_ranks.count("|")
##    count_classifications = classifications.count("|")
##
##    if count_classification_ranks == count_classifications:
##        word_classification_ranks = classification_ranks.split("|")
##        word_classifications = classifications.split("|")
##
##        
##        for rank, word in zip(word_classification_ranks, word_classifications):
##                a_list.append((rank,word))
##            
##            
##    else:
##        print("ERROR: Invalid input, classification ranks do not match classifications!")
##
##
##    return a_list
##        
##
##classification_ranks = 'class|superclass|subphylum|phylum|kingdom'
##classifications = 'Aves|Gnathostomata|Craniata|Chordata|Animalia'
##hierarchy = get_classification_hierarchy(classification_ranks, classifications)
##print(hierarchy)
##
##print()
##
##classification_ranks = 'superclass|subphylum|phylum|kingdom'
##classifications = 'Aves|Gnathostomata|Craniata|Chordata|Animalia'
##hierarchy = get_classification_hierarchy(classification_ranks, classifications)
##print(hierarchy)


### Question 03

def get_biostatus(biostatus_string):
    biostatus_cases = ["Endemic","Non-endemic","Exotic","Indigenous"]
    biostatus_string = biostatus_string.split("|")
    
    for word in biostatus_string:
        if word in biostatus_cases:
            return word
    else:
        return "N/A"
        

##Test
biostatus_string = "Endemic|Present|Wild|New Zealand|Political Region|"
print(get_biostatus(biostatus_string))

biostatus_string = "|Present||New Zealand|Political Region|"
print(get_biostatus(biostatus_string))


biostatus_string = ""
print(get_biostatus(biostatus_string))

biostatus_string = "   "
print(get_biostatus(biostatus_string))

biostatus_string = "ErroneousEntry|Exotic|Sometimes Present|Wild|New Zealand|Political Region"
print(get_biostatus(biostatus_string))

biostatus_string = " | ||"
print(get_biostatus(biostatus_string))












