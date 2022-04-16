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
        counts[word] = counts.get(word, 0) + 1
bigkey = None
bigval = None
for key,val in counts.items():
    if '@' in key :
        if bigval is None or  val > bigval:
            bigkey = key
            bigval = val
print(bigkey, bigval)
