# if coniditon:

# if - elif - else 

1. For an if - elif - else will be only one output 
2. Priority - if, elif , else
#Eg 1
if True:
    print(5)

#Eg 2
if 0:
    print(5)
else:
    print(6)

#Eg 3 (Whenever we have if it consider as one if condition)
if 'magesh' == 'magesh':
    print(1)
if 'magesh' == 'magesh':
    print(2)
if 'magesh' == 'magesh':
    print(3)
if 'magesh' == 'mages':
    print(4)
else:
    print(6)

# 2nd nearest elif condition - True  it will get executed after execution the if-else will terminated
#Eg 1
a = 1
b = 2
c = 3
if 'magesg' == 'magesh':
    print(1)
elif b>c:
    print(2)
elif c>b:
    print(3)
elif b>c:
    print(2)
else:
    print(4)

#Eg 2
a = 1
b = 2
c = 3
if 'magesg' == 'magesh':
    print(1)
elif c>b:
    print(3)
elif c>b:
    print(2)
else:
    print(4)

#Eg 3
a = 1
b = 3
c = 3
if c>a:
    print(1)
elif b>=c:
    print(2)
elif c>b:
    print(3)
else:
    print(4)

#Eg 4
a = 1
b = 2
c = 3
if c<a:
    print(1)
elif c%b:
    print(2)
elif b%c:
    print(3)
elif b<c:
    print(4)
elif c>a:
    print(5)
else:
    print(6)

#Eg 5
if 0:
    print(1)
elif False:
    print(3)
else:
    print(2)

#Eg 6
if 0:
    print(1)
elif True:
    print(3)

#Eg 7
if 0:
    print(1)
elif False:
    print(3)


#Eg 8
elif True:
    print(3)

#Eg 9
dhiya = True
srini = False

if dhiya or srini:
    print(1)
elif dhiya and not(srini):
    print(2)
else:
    print(0)
