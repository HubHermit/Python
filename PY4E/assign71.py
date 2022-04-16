# Use words.txt as the file name
fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print('The file name does not exist: ', fname)
    quit()

for line in fh:
    line = line.rstrip()
    print(line.upper())
