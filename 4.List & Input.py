# LIST : HETEROGENEOUS DATA TYPES
#Eg 1
a = ["srini",1,2,3,4]
print(a[0])
print(a[1:-1])
print(a[1:])

#Eg 2
a = ["srini",1,2,3,4,[5,"rose"]]
print(a[5])
print(a[5][1])

#Eg 2
a = ["srini",1,2,3,4,[5,"rose",["s","r","i","n","i"]]]
print(a[5][2][3])

# METHODS OF LIST:
# Sum:
#Eg 1
a =[1,2,3,4,5]
print(sum(a)) #It helps to add all the element in a list

# Maximum:
#Eg 1
a =[1,2,3,7,4,5]
print(max(a)) # It helps to tell the highest int number

# Minimum:
#Eg 1
a =[1,2,3,0,4,5]
print(min(a)) # It helps to tell the highest int number

# Append:
#Eg 1
a =[1,2,3,4,5]
a.append("sri")
print(a)

#Eg 2
a =[1,2,3,4,5]
a.append(["sri",6,7,8,9])
print(a)

# Insert:
#Eg 1
a =[1,2,3,4,5]
a.insert(0,["sri",6,7,8,9])
print(a)

#Eg 2
a =[1,2,3,4,5]
a.insert(3,["sri",6,7,8,9])
print(a)

# Pop:
#Eg 1
a =[1,2,3,4,5]
a.pop()
print(a)

#Eg 2
a =[1,2,3,4,5]
a.pop(3)
print(a)

#Eg 3
a =[1,2,3,4,5]
print(a.pop())
print(a)

# Sort:
#Eg 1
a = [1,5,3,7,8,10,15,11]
a.sort()
print(a)
print(a[2])

# Sorted:
#Eg 1
a = [1,5,3,7,8,10,15,11]
b = sorted(a)
print(b)
print(b[2])
print(a[2])

# Reverse:
#Eg 1
a = [1,5,3,7,8,10,15,11]
a.reverse()
print(a)
print(a[2])

# Reversed
#Eg 1
a = [1,5,3,7,8,10,15,11]
b = reversed(a)
#print(b) # <list_reverseiterator object at 0x000001A2D90DB5B0>

#Eg 2
a = [1,5,3,7,8,10,15,11]
b = reversed(a)
print(list(b))
#print(b[2]) # TypeError: 'list_reverseiterator' object is not subscriptable
print(a[2])

# Count In List:
#Eg 1
a = [1,5,3,7,8,10,15,11]
print(a.count(5))

#Eg 2
a = [1,5,3,7,8,10,15,11]
print(a.count("5"))

# Copy:
#Eg 1
a = [5,4,3,2,1,0]
b = a.copy()
b[1] = 'magesh'
print(a)
print(b)

# Extend:
#Eg 1
a = [1,2]
a.extend([3,4])
print(a)

#Eg 2
a = [1,2]
a.extend([3,4])
a.extend("[3,4]")
print(a)

# Item Assignment:
#Eg 1
a = [1,5,3,7,8,10,15,11]
a[1] = "SRI"
print(a)

#Eg 2
a = [1,5,3,7,8,10,15,11]
b = a
b[2] = "SRINI"
print(b)

#Eg 3
a = [1,5,3,7,8,10,15,11]
a[1] = "SRI"
b = a
b[2] = "SRINI"
print(b)

# INPUT:
# Always the datatype will be string
#Eg 1
a = input("Enter You Name:")
print(a)

#Eg 2
a = input("Enter You Numbers:")
print(list(a))
print(a,split(","))