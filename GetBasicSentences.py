
import sys
import requests
import json
import os

def parse_json_obj(json_file, BasicSentences):
    with open(json_file, 'r') as i:
        with open(BasicSentences, 'a') as o:
            jsonObj = json.load(i)
            define_word = jsonObj[0]["def"][0]["sseq"]
            for x in define_word:
                try:
                    if len(x[0][1]['dt']) > 1:
                        sentence = x[0][1]['dt'][1][1][0]['t'].replace("{wi}", "").replace("{/wi}", "")
                        print(sentence)
                    o.write(sentence+ "\n")
                except:
                    continue

def load_words(data_file_name):
    with open( data_file_name, "r") as f:
        l = json.load(f)
    return l

def getBasicSentencess(json_sentences, data_file_name):
    with open (data_file_name, "w") as d:
        with open("not_found.txt", "a") as n:
            for w in json_sentences:
                found_word = False
                try:
                    s = w[0]['def'][0]['sseq'][0][2][1]['dt'][1][1][1]['t']
                    d.write(s)
                    d.write("\n")
                    found_word = True
                except:
                    pass
                try:
                    s = w[0]['def'][0]['sseq'][0][2][1]['dt'][1][1][1]['t']
                    d.write(s)
                    d.write("\n")
                    found_word = True
                except:
                    pass
                try:
                    s = w[0]['def'][0]['sseq'][0][1][1]['dt'][1][1][1]['t']
                    d.write(s)
                    d.write("\n")
                except:
                    pass
                try:
                    s = w[0]['def'][0]['sseq'][0][1][1]['dt'][1][1][2]['t']
                    d.write(s)
                    d.write("\n")
                    found_word = True
                except:
                    pass
                try:
                    s = w[0]["def"][0]["sseq"][0][0][1]["dt"][1][1][0]['t']
                    d.write(s)
                    d.write("\n")
                    found_word = True
                except:
                    pass
                try:
                    s = w[0]["def"][0]["sseq"][1][0][1]["dt"][1][1][0]['t']
                    d.write(s)
                    d.write("\n")
                    found_word = True
                except:
                    pass
                try:
                    s = w[1]['def'][0]['sseq'][0][0][1]['dt'][0][1]
                    d.write(s)
                    d.write("\n")
                    found_word = True
                except:
                    pass
                try:
                    s = w[0]['def'][0]['sseq'][0][0][1]['sdsense']['dt'][1][1][0]['t']
                    d.write(s)
                    d.write("\n")
                    found_word = True
                except:
                    pass
                try:
                    s = w[0]['def'][0]['sseq'][0][0][1]['dt'][1][1][2]['t']
                    d.write(s)
                    d.write("\n")
                    found_word = True
                except:
                    pass
                try:
                    s = w[0]['def'][0]['sseq'][0][0][1]['dt'][1][1][1]['t']
                    d.write(s)
                    d.write("\n")
                    found_word = True
                except:
                    pass
                if found_word == False:
                    try:
                        n.write(w[0]["meta"]["id"])
                        n.write("\n")
                    except:
                        print(w)
                        print("\n")

def getBasicSentences2(json_sentences, data_file_name):
    i = 70
    for w in json_sentences:
        try:
            print(w[0]['meta']['id'])
            print(w[0]['def'][0]['sseq'][0][0][1]['dt'][0][1])
            print("\n")
        except:
            pass



def getBasicSentences3(json_sentences, data_file_name):
    i = 50
    s = json_sentences[i][0]
    print(s)
    print("\n")
    
    quit()
    

def main():
    min = 1000
    if (min != 0):
        min += 1
    max = 1607
    input_file_name = "VUA20/JSON_obj_MW/data_" + str(min) + "-" + str(max)+ ".json"
    data_file_name = "VUA20/BasicSentences/BasicSentences_" + str(min) + "-" + str(max) + ".txt"
    data_file_name2 = "VUA20/BasicSentences/BasicSentences2_" + str(min) + "-" + str(max) + ".txt"
    if os.path.exists(input_file_name) == False:
        print("No input file of that name")
        quit()
    if os.path.exists(data_file_name) == False:
        with open(data_file_name, "w+") as f:
            f.write("[]")
    w = load_words(input_file_name)
    getBasicSentencess(w, data_file_name)
    #getBasicSentences3(w, data_file_name2)
    
if __name__=="__main__": 
    main() 
