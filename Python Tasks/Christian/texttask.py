print("Reading and writing text files")
FILE_NAME = "test.txt"
f_i = open(FILE_NAME, 'r')
outputlist = f_i.readlines()
f_i.close()
print(outputlist)
    
print("Incrementing numbers by 1 and write in test.txt.")
f_o = open(FILE_NAME, 'w')
for line in outputlist:
    line = int(line) + 1
    print(line)
    f_o.write(str(line)+"\n")