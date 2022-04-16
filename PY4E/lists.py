#working with lists
#python lists.py in cmd to run
#these list can contain items of the same or different types
#EG playlist = ['fire', 2.4, 25]
# anotherlist = [1, 2, 3]
#listinlist = [1, [2, 3], 4]
#[x] index operator

friends = ['Joseph', 'Glenn', 'Sally']
for friend in friends:
    print('Happy New Year:' , friend)
print('Done!')
print('Length of friends:', len(friends))
print(range(len(friends)))

#Lists are Mutable, meaning we can change an element of a list using the indext operator
#Strings, however, are immutable, meaning we can not change the content of a string
#we must make a new string to make any changes
#example
fruit = 'Banana'
print(fruit)
#to print this in lower case we will need to assign a copy of the string to a new variable
x = fruit.lower()
print(x)
#x is the new variable the string fruit will be copied and assigned to. The .lower() copies the string
#Anyway this is about Lists. The following example shows the change
lotto = [2, 4, 12, 26, 41, 63]
print(lotto)
lotto[2]= 28
print(lotto)
print('lotto[1:3= ', lotto[1:3])
#lists can be sliced
#Building a list from scratch
#Create an empty list then add elements using the append method
stuff= list()
stuff.append('book')
stuff.append(99)
print(stuff)
stuff.append('cookie')
print(stuff)
#the list stays in order and new elements are added at the end of the list
#Is something in the list?
some = [1, 9, 21, 10, 16]
some.sort()
print(some)
print(len(some))
print(max(some))
print(min(some))
print(sum(some))

#creating a list with a loop
numlist = list()
#while True:
#    inp = input('Enter a number: ')
#    if inp == 'done' : break
#    value = float(inp)
#    numlist.append(value)
#average = sum(numlist)/len(numlist)
#print('Average:', average) #this is best used for large amounts of data
#now for strings and lists combinations

abc = 'With three words'
morestuff = abc.split() #copies each word into a list
print(morestuff)
print(morestuff[0])
#delimiter characters can be used to specify what to use in splitting
line = 'A lot             of spaces'
etc = line.split()
print(etc)

linetwo = 'first;second;third'
thing = linetwo.split()
print(thing)
print(len(thing))
thing = linetwo.split(';')
print(thing)
print('Thing now:', len(thing))

#remember that parsing exercise? Here is a simplified version
#fhand = open('mbox-short.txt')
#for line in fhand:
#    line.rstrip()
#    if not line.startswith('From ') : continue
#    words = line.split()
#    print(words[2])

#From stephen.marquad@uct.ac.za Sat Jan  5  09:14:16 2008
#words = line.split()
#email = words[1] prints stephen.marquad@uct.ac.za
#pieces = email.split('@')
