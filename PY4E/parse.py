data ='From stephen.marcquad@uct.ac.za Sat Jan 5 09:14:16 2008'
atpos = data.find('@')
print(atpos) #Displays the postion the @sign is - pos 21

sppos = data.find(' ', atpos)
print(sppos) #Displays where the fist space is after the @ sign - pos 31

host = data[atpos+1: sppos] #slicing. Remember s[0:4], this will be data[22:31]
print(host)#prints that range between the @ and ' '
