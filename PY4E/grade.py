score = input("Please enter a score between 0.0 and 1.0: ")
try:
    iscore = float(score)
except:
    print("Please enter a number")
    quit()

if iscore > 1.0:
    print("Error, the score is out of range.")
elif iscore < 0.0:
    print("Error, the score is out of range.")
elif iscore >=0.9:
    print ("A")
elif iscore >=0.8:
    print("B")
elif iscore >=0.7:
    print("C")
elif iscore >=0.6:
    print("D")
elif iscore < 0.6:
    print("F")
