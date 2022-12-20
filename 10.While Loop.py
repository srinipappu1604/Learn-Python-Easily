syntax:

# while (Condition):
#     statement

# while True:
#     print(5)

print(5)

a = 0
b = 4

while a<b:
    print(5)
    # a = a +2
    a+=1

# 1. a = 0, b = 4 ; 0 < 4 : 5 a = 0+1
# 2. a = 1, b = 4 ; 1 < 4 : 5 a = 1 + 1
# 3. a = 2, b = 4 ; 2 < 4 : 5 a = 2+1
# 4. a = 3, b = 4 ; 3 < 4 : 5 a = 3+1
# 5. a = 4, b = 4 ; 4 < 4

a = [1,2,3,4,5]
a[5]
a = 'magesh'
a[6]


a = [1,2,3,4,5]

l = len(a)
i = 0
while l>0:
    print(a[i])
    i = i +1
    l = l-1



a = [1,2,3,4,5]
l = len(a)
while l>0:
    print(l)
    print(65)
    l = l-1

a = [1,2,3,4,5]
i = 0
while i<len(a):
    print(a[i])
    i = i+1
    
# While Loop
i = 1
while i<=10:
    print(i)
    i = i + 1
print("Loop Closed")