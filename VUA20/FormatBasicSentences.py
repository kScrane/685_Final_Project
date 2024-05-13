
import sys
import requests
import json
import os
import operator


def formatSentences(input, output):
    """ Saves metaphor bool, sentence, w_index in standard tsv """
    replace_chars = ["{wi}", "{/wi}", "{it}", "{/it}"]
    remove_chars = ["{ldquo}", "{/ldquo}", "{rdquo}", "{/rdquo}", "\n", "{gloss}=", "{\gloss}", "{d_link|"]
    with open(input, "r") as i:
        with open(output, "w+") as o:
            for line in i:
                for c in replace_chars:
                    line = line.replace(c, "*")
                for c in remove_chars:
                    line = line.replace(c, "")
                split_sentence = line.split("*")
                try:
                    word = split_sentence[1]
                    count = split_sentence[0]
                    index = operator.countOf(count, " ")+1
                    #print("0", line.replace("*", ""), str(index))
                    line = line.replace("*", "")
                    write_line = "0" + "\t"+ line+ "\t"+str(index) + "\n"
                    o.write(write_line)
                except:
                    print("error")
                    print(line)
                
    return
 
def formatBasicSentences():
    input_file = "BasicSentences/BasicSentences_0-1607.txt"
    output_file = "VUA20-BasicSentences/FormattedBasicSentences_0-1607.tsv"
    with open (output_file, "w+"):
        pass

    if os.path.exists(input_file) == False:
        print("No input file of that name")
        quit()

    formatSentences(input_file, output_file)
    
def main():
    #getBasicSentences2("","")
    formatBasicSentences()

    return
    
if __name__=="__main__": 
    main() 
