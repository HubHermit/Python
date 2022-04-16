text = "X-DSPAM-Confidence:    0.8475"
data = text.find('0')
datapull = text[data:29]
datafloat = float(datapull)
print(datafloat)
datatotal = datafloat + 10
print(datatotal)
