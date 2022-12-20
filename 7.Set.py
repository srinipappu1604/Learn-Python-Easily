# set:
# To declare set as below
a = {}
a = set()

# 1. set is unordered datatype: we cannot do indexing in set
# 2. immutable elements(Element cannot get repeated) -> always takes only unique elements
# 3. only we can have tuple,str,int,bool

#Eg 1
a = {1,2,34,5,6,7,8,91,2}
print(a)
print(type(a))

#Eg 2
a = set([1,2,3,1,1,2,3,1,2,1,3,2,1,1,3,2,1])
print(a)

# Add
#Eg 1
a = set([1,2,3,1,1,2,3,1,2,1,3,2,1,1,3,2,1])
a.add(4)
print(a)

#Eg 3
a = set([1,2,3,1,1,2,3,1,2,1,3,2,1,1,3,2,1])
a.add((1,2,3,4,5,6))
print(a)

#Eg 3 (inside set we cannot have set,list,dict)
a = set([1,2,3,1,1,2,3,1,2,1,3,2,1,1,3,2,1])
a.add([1,2,3])
print(a)

# Update
#Eg 1
a = {1,2,3,4,5}
# a.update([5,4,6,7,8,9])
a.update((5,4,6,7,8,9))
print(a)

#Eg 2
a = {1,2,3,4,5}
a.update([5,4,6,7,8,9])
print(a)

# Intersection
#Eg 1
a = {1,2,3,4,5}
b = {4,5,6,7,8}
print(a.intersection(b))

# Union
#Eg 1
a = {1,2,3,4,5}
b = {4,5,6,7,8}
print(a.union(b))

# Difference
#Eg 1
a = {1,2,3,4,5}
b = {4,5,6,7,8}
print(a.difference(b)) # element in a not in b

#Eg 2
a = {1,2,3,4,5}
b = {4,5,6,7,8}
print(b.difference(a)) # element in b not in a

# Symmetric_difference
#Eg 1
a = {1,2,3,4,5}
b = {4,5,6,7,8}
print(b.symmetric_difference(a)) # opp of intersection

# Remove
#Eg 1
a = {1,2,3,4,5}
a.remove(4)
print(a)

#Eg 2
a = {1,2,3,4,5}
a.remove(41) # throw error if ele is not there
print(a)

# Discard (If the element is not there it donot show the error)
#Eg 1
a = {1,2,3,4,5}
a.discard(41)
a.discard(4)
print(a)

int,float,str,bool,list,dict,set,tuple
