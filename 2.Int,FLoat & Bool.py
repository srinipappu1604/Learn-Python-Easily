
# declaration of variable:
# 1. variable always assigned to any of the datatype
# 2. variable should not be void

# int & float:
#Eg 1
a = 45
b = ''
c = '7401.165'
c = 45.
print(type(c))
print(c) # 45.0

#Eg 2
a= 1
b = 2
print(a+b)
print(a-b*b)

# 1. float:
# whenever we have any operand of float the always output will be float
#Eg 1
a = 1.5
b = 1.5
print(a+b)
print(type(a+b))

#Eg 2
a = 1.5
b = 10
print(a*b)
print(type(a*b))

# Division:-
# always output will be float
# syntax: /
#Eg 1
a = 10
b = 2
print(a/b) # 5.0
print(type(a/b))



# Floor Division:-
# it will take quotient as output (i.e) elements before decimal
# syntax: //
#Eg 1
a = 10
b = 3
print(a//b) 
print(type(a//b))

#Eg 2
a = 7
b = 10
print(a//b) 
print(type(a//b))

#Eg 3
a = 10
b = 2.5
print(a//b) 
print(type(a//b))

#Eg 4
a = 11.5
b = 2
print(a//b) 
print(type(a//b))


# Modolo operator :-
# it will take reminder as output 
# syntax: %
#Eg 1
a = 7
b = 10
print(a%b) 
print(type(a%b))

#Eg 2
a = 11
b = 2.5
print(a%b) 
print(type(a%b))

#Eg 3
a = 11.4512
b = 2.5
print(a%b) 
print(type(a%b))


# Equality Operators:
# always the output will be bool

# > , < , >= , <= , == , !=
#Eg 1
a = 4
b = 4
print(a>b)

#Eg 2
a = 4
b = 4
print(a!=b)

print(type(45) == int)
print(int)

print(True + 45 + False)

print(False == True)
print(False > True)
print(False < True)

b = int('magesh')
print(b)


b = int('13245')
print(b)

b = int(564564.6544)
print(b)
