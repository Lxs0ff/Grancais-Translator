file_name = input("Input file name: ")
file = open(file_name+".txt","r")
new_file = open(file_name+"_new.txt","w")
lines = file.split()
words = lines.split(" ")
count = 0
for line in lines:
    count=0
    for word in words:
        count+=1
        if word != "\n":
            if word[0] != "a":
                word = word[0:]
                word = word[1:]
                if count == 1:
                    word = "Ga" + word
                else:
                    word = "ga" + word
            else:
                word = word[0:]
                if count == 1:
                    word = "G" + word
                else:
                    word = "g" + word
            new_file.write(word+" ")
            print(word+" ")
        else:
            new_file.write("/n")
            print("/n")
            
