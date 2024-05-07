#author --> Deep Gupta
File = open("Task10.txt" , "r")

d = dict()

for line in File:
    line = line.strip()
    line = line.lower()

    words = line.split(" ")

    for word in words:
        if word in d:
            d[word] = d[word] + 1
        else:
            d[word] = 1

    #Also Print like This
    #print(word , d[word])

for key in list(d.keys()):
    print(key, ":" , d[key])
            
