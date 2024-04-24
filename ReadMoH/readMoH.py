
import csv
import os

def simplified_data(input_data, output_data):
    """Writes label, sentence, index into file for easier data understanding"""
    weird_char = [';', ':', '!', "*", "]", "["]
    with open(input_data, "r") as input: 
        reader = csv.reader(input, delimiter="\t") 
        row = next(reader)
        with open(output_data, "w") as output: 
            writer = csv.writer(output, delimiter="\t") 
            row = next(reader)
            for row in reader:
                count = row[2].split("<b>")[0].count(" ") + 1
                sentence = row[2].replace("<b>", "").replace("</b>", "")
                usage = row[3]
                if usage == "literal":
                    usage_int = 0
                else:
                    usage_int = 1
                #print(usage_int, sentence, count)
                writer.writerow((usage_int, sentence, count))
      
    return 
     



def main():
    input_file = os.path.join(os.path.dirname(__file__), "../DataSources/moh.tsv")
    output_file = os.path.join(os.path.dirname(__file__), "simplified_moh.tsv")

    try:
        w = open(input_file, "r")
        w.close()
    except:
        print("Input file not found")

    with open (output_file, "w+"):
        pass
    simplified_data(input_file, output_file)
    return
    
if __name__=="__main__": 
    main() 