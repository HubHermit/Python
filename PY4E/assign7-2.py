# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print('File name does not exist:', fname)
#remember to declare variables at the margin unless within a loop block
count = 0
datasum=0
dataavg = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    count = count +1
    data = line.find('0')
    datapull=line[data:29]
    datafloat=float(datapull)
    datasum+=datafloat
    dataavg = datasum/count
print('Average spam confidence:', dataavg)
