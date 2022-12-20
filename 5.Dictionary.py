# Dict:
# 1. We can take value with the help of keys
# 2. If a key is not there in my dict we will be getting key error
# 3. Key will try to have unique elements
# 4. For value it can be any data type
# 5. For key str,int,flot,bool, tuple,None
# Syntax: a =  {'key1':'value1'}

#Eg 1
a = {'key1':'value1','key2':'value2','key3':'value3'}
print(a['key3'])
# print(a['key4'])
# print(a[2]) # it will take elements as key

# To add new Key in the dict
#Eg 1
a = {'key1':'value1','key2':'value2','key3':'value3'}
a['key4'] = 45 # if key is not ther it will create a new key value pair if the key is present it will replace the value
a['key2'] = 'srini'
print(a)

# It will take the latest key
#Eg 1
a = {'key1':'value1','key2':'value2','key3':'value3','key2':'newval'}
print(a)

#Eg 2
a = {'key1':'value2','key2':'value2','key3':'value2','key2':'latest1','key2':'latest2'}
print(a)

#Eg 3
a = {'key1':'value2','key2':'value2','key3':'value2','key2':'latest1','key2':'latest2'}
a['key2'] = 'latest3'
print(a)

#Eg 4
a = {True:'value2',45:'value2','key3':{'value2':'super'},(1,2,3):[1,2,3,4,5]}
print(a)

# Datatype should not be given for key
#Eg 1
a = {[True]:'value2',45:'value2','key3':{'value2':'super'},(1,2,3):[1,2,3,4,5]}
print(a)

#Eg 2
a = {True:'value2',45:'value2',{'key3':45}:{'value2':'super'},(1,2,3):[1,2,3,4,5]}
print(a)

#Eg 3
a = {True:'value2',45:'value2',{'key3',1,2,3,4,5,6}:{'value2':'super'},(1,2,3):[1,2,3,4,5]}
print(a)

# How to take keys alone
#Eg 1
a = {'key1':'value2','key2':'value2','key3':'value2','key2':'latest1','key2':'latest2'}
print(a.keys())
print(list(a.keys()))

# How to take values alone
#Eg 1
a = {'key1':'value2','key2':'value2','key3':'value2','key2':'latest1','key2':'latest2'}
print(a.values())
print(list(a.values()))

# Items
# Tuple inside a list
#Eg 1
a = {'key1':'value2','key2':'value2','key3':'value2','key2':'latest1','key2':'latest2'}
print(a.items()) # tuple inside a list
# key,value -> tuple => key:value pair
print(list(a.items()))


## Example to take 12 as an output
#Eg 1:
a = {1:'magesh','rose':465,2:1,"jasmine":32,4:34,'elements':[5,'rose',[11,12,13,14]]}
print(a['elements'])
print(a['elements'][2][1])

#Eg 2:
a = {1:'magesh','rose':465,2:1,"jasmine":32,4:34,'elements':[5,'rose',[11,12,13,14]]}
print([5, 'rose', [11, 12, 13, 14]][-1][1])

#Eg 3:
a = {1:'magesh','rose':465,2:1,"jasmine":32,4:34,'elements':[5,'rose',[11,12,13,14]]}
print([5, 'rose', [11, 12, 13, 14]][2][1])