#lists lst = [] or lst = list()
#dictionaries dictname = {} or dictname = dict()
#tuples tupname = () or (x,y) = (4, 'Fred')
#dictname.items() gives you a list of tuples
name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

counts = dict()
for line in handle:
    line = line.rstrip()
    if not line.startswith('From ') : continue
    words = line.split()
    for word in words:
        if ':' in word:
            atpos = line.find(':')
            word = line[atpos-2:atpos]
            counts[word] = counts.get(word, 0) + 1
a = sorted(counts.items())
for key,val in a:
    print(key, val)
