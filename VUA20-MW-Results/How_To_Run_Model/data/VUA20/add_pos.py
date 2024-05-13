with open("data/VUA20/train.tsv", "r") as t:
    with open("data/VUA20/train2.tsv", "w+") as w:
        for r in t:
            r = r.split("\t")
            start = r[0]
            b = r[1]
            sentence = r[2]
            pos = r[3]
            position= int(r[4][:-1]) - 1
            line = start + "\t" + b + "\t" + sentence + "\t" + pos + "\t" + str(position) + "\n"
            w.writelines(line)

