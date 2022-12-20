# for loop:-  // iteration:-
# 1. definite loop
# 2. for all the iterable datatype

# syntax:
# for user_vari in iterable_variable:
#     condition // statement // performance

# it will take one element at atime from iterable_variable and assigin that to user_vari
#Eg 1
a = 'srini'
for i in a:
    print(i)

#Eg 1
a = [1,2,3,4,5]
for i in a:
    print(i)

# Iterations:- // Debuging the code
# 1. i = 's' ; s
# 2. i = 'r' ; r
# 3. i = 'i' ; i
# 4. i = 'n' ; n
# 5. i = 'i' ; i

#Eg 3
a = [1,2,3,4,5]
for i in a:
    if i%2 == 0:
        print('even',i)

#Eg 4
a = [1,2,3,4,5]
for i in a:
    if i%2 == 1:
        print('odd',i)

#Eg 5
a = [1,2,3,4,5]
for i in a:
    if i%2 != 0:
        print('odd',i)

#Eg 6
a = [1,2,3,4,56,7,8]
print(4 in a)
print(4 not in a)
print(5!=5)
print(4!=5)

#Eg 7
a = '1,2,3,4,5,67,8'
print('4' in a)

#Eg 8
a = 'i love india'
print('India' not in a)

#Eg 9
for i in range(1,11):
    print(i)
print("Loop Closed")

#Eg 10
Cricketers = ["sri","srini","pappu"]
for i in Cricketers:
    print(i)
print("Loop Closed")

#Eg 11
Cricketers = ["sri","srini","pappu"]
for i in range(0,3):
    print(i)
print("Loop Closed")

#Eg 12
Cricketers = ["sri","srini","pappu"]
for i in range(0,3):
    print(Cricketers[i])
print("Loop Closed")

#Eg 13
Cricketers = ["sri","srini","pappu"]
for i in range(len(Cricketers)):
    print(Cricketers[i])
print("Loop Closed")




syntax ; range(int)

range() # iterable - 0 -4

print(range(5)) # range(0,5)
print(list(range(5))) # range(0,5)
print(list(range(5,10))) # range(0,5)

#Eg 1
for i in range(5):
    print(i)

#Eg 2
for i in range(5,10):
    print(i)

#Eg 3
a = [11,22,32,42,52]
for i in range(5):
    print(a[i])

#Eg 4
a = [11,22,32,42,52]
for i in range(len(a)):
    print(a[i])

#Eg 5
a = [11,22,32,42,52]
for i in range(len(a)):
    print(i)

#Eg 6
a = [1,2,3,4,5]
b = [6,7,8,9,10]
# 1*6 2*7 3*8 4*9
# debugging:
for i in range(len(a)):
    print(a[i] * b[i])

#Eg 7
a = 'magesh'
b = [1,2,3,4,5,6]

for i in range(len(a)):
    print(a[i] * b[i])

#Eg 8
b = [1,2,3,4,5,6]
a = 'magesh'
c = (11,12,13,14,15,16)
for i in range(len(a)):
    print('value of i ',i)
    print(a[i])
    print(b[i])
    print(c[i])
    print('------------------------')

print(list(range(10,20,3)))

print('magesh' * 3)