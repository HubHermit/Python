#opening a file handle=open(filename, mode) example fhand= open('mbox.txt', 'r')
#fhand will be the variable we use to return a handle to manipulate the file
#mbox.txt is the file name
#r is the mode for read, w is the mode for write



#Loops are used to handle files as a sequence
#this block prints all lines
print('xfile lines')
xfile = open('mbox.txt')
for cheese in xfile:
    print(cheese)

#counting lines in a file
print('fhand count')
fhand=open('mbox.txt')
count = 0
for line in fhand: count = count +1
print ('Line Count:', count)

#$python filehandle.py

#reading the whole file
print('This section reads the whole file')
fileh=open('mbox.txt')
inp = fileh.read()
print(len(inp))
print(inp)

#print(inp[:20])
