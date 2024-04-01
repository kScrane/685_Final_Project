import sys
import csv
import pandas as pd
#Drop columns: https://www.geeksforgeeks.org/delete-a-csv-column-in-python/

def Split_By_word(dataset_name, modified_dataset):
    data = {}
    metaphor_bool = 0
    with open(dataset_name, "r") as input:
        for line in input:
            line = line.replace("\n", "")
            if(len(line.strip()) == 0 or line == "********************"):
                continue
            elif (line[0:3] == '***'):
                line = line.replace("*", "")
                curr_word = line
                #print(curr_word)
                #data{word}[0] = literal
                #data{word}[1] = metaphor
                data.update({curr_word: [[],[]]})
            elif(line == "*nonliteral cluster*"):
                metaphor_bool = 0
            elif(line == "*literal cluster*"):
                metaphor_bool = 1
            else:
                line = line.replace("/.", "").split("\t")
                if line[1] == "U":
                    continue
                data[curr_word][metaphor_bool].append(line[2])
    for x in data['absorb'][0]:
        print(x)
    with open(modified_dataset, "w+") as w:
        for key in data:
            for x in data[key][0]:
                w.write(key  + '\t' + "0" + '\t' + x + "\n")
            for x in data[key][1]:
                w.write(key  + '\t' + "1" + '\t' + x + "\n")


    return 
                
def count_metaphor_occurances(modified_dataset_name, counts_of_metaphors):
    """Removes columns not necessary for our work, writes result to modified_data_set
    name
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
                #writer.writerow([key])
                writer.writerow((key, metaphor_dict[key][0], metaphor_dict[key][1]))




def main(): 
    Split_By_word("DataSources/TroFiExampleBase.txt", "TroFi_Counts.txt")
    #count_metaphor_occurances("modifiedtrain.tsv", "counts_of_metaphors_train_w_counts.tsv")

    
  
if __name__=="__main__": 
    main() 