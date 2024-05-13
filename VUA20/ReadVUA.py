import sys
import csv
import pandas as pd
#Drop columns: https://www.geeksforgeeks.org/delete-a-csv-column-in-python/
"""Data manipulation on VUA20 dataset for easier calculations
"""

def simplified_data(dataset_name, modified_dataset):
    """Writes label, sentence, index into file for easier data understanding"""
    weird_char = [';', ':', '!', "*", "]", "["]
    with open(dataset_name, "r") as input: 
        reader = csv.reader(input, delimiter="\t") 
        with open(modified_dataset, "w") as output: 
            writer = csv.writer(output, delimiter="\t") 
            row = next(reader)
            for row in reader:
                label = int(row[1])
                sentence = row[2]
                index = int(row[5])
                word = row[2].split(" ")[index].lower()

                for i in weird_char:
                    word = word.replace(i, '')
                writer.writerow((label, sentence, index))
    return 
     
def remove_columns(dataset_name, modified_dataset):
    """Removes columns not necessary for our work, then gets relevant word based on the index
    writes result to modified_dataset"""
    weird_char = [';', ':', '!', "*", "]", "["]
    with open(dataset_name, "r") as input: 
        reader = csv.reader(input, delimiter="\t") 
        with open(modified_dataset, "w") as output: 
            writer = csv.writer(output, delimiter="\t") 
            row = next(reader)
            for row in reader:
                index = int(row[5])
                word = row[2].split(" ")[index].lower()
                for i in weird_char:
                    word = word.replace(i, '')
                writer.writerow((row[1], word))
    return 
                
def count_metaphor_occurances(modified_dataset_name, counts_of_metaphors, record_count=False):
    """
    Creates dictionary of [not metaphor, metaphor] counts given simplified vua20 dataset
    Writes all words with examples of metaphors but not basic into counts_of_metaphors
    record_count: True = record number of metaphor uses, False = Just write target word
    - Metaphor_bool     Word
    """
    #metaphor_dict = {word : [count metaphors, count basic]}
    metaphor_dict = {}
    with open(modified_dataset_name, "r") as input: 
        reader = csv.reader(input, delimiter="\t") 
        for row in reader:
            metaphor_bool = int(row[0])
            word = row[1]
            if word not in metaphor_dict:
                metaphor_dict[word] = [0,0]
            if metaphor_bool == 0: #not metaphor
                metaphor_dict[word][0] += 1
            else: #is metaphor
                metaphor_dict[word][1] += 1

    """Write down any words where there are examples of metaphors, but not basic"""
    with open(counts_of_metaphors, "w") as output: 
        writer = csv.writer(output, delimiter="\t") 
        for key in metaphor_dict:
            if metaphor_dict[key][0] == 0 and metaphor_dict[key][1] >= 1:
                if record_count == True:
                    writer.writerow((key, metaphor_dict[key][0], metaphor_dict[key][1]))
                else:
                    writer.writerow([key]) 

def main(): 
    return
    #simplified_data("DataSources/VUA20_train.tsv", "VUA20/VUA20-BasicSentences/Train.txt")
    #remove_columns("train.tsv", "modifiedtrain.tsv")
    #count_metaphor_occurances("modifiedtrain.tsv", "counts_of_metaphors_train_w_counts.tsv")

    
  
if __name__=="__main__": 
    main() 