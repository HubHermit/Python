fname = input("Enter file name: ")
try:
    fh = open(fname, 'r')
except:
    print('The file name does not exist', fname)

lst = list()
words = fh.read().split()
for word in words:
    if word not in lst :
        lst.append(word)
lst.sort()
print(lst)
