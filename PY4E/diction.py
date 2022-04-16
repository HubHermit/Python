#Working with dictionaries
purse = dict()
purse['money'] = 12
purse['candy'] = 3
purse['tissues'] = 75
print(purse)
print(purse['candy'])
purse['candy'] = purse['candy'] + 2
print(purse)
#lists are a collection of items, dictionaries are more like a bag of items
jjj = { 'Chuck' : 1, 'Fred' : 42, 'Jan' : 100 }
#Printing key value pairs
for key,value in jjj.items() :
    print(key, value)
