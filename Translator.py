file_name = input("Input file name + .txt: ")
file = open(file_name,"r")
file_name.remove(".txt")
new_file = open(file_name+"_new.txt","w")
lines = file.split()
words = lines.split(" ")

for line in lines:
    for word in words:
        if word != "\n":
            print("placeholder")
        else:
            new_file.write("/n")
            
