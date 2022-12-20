# Tuple:
# immutable datatype
# We cannot do item assignment in tuple
#Eg 1
a = (1,2,3,4,56)
a[3] = 'srini' # item assignment

#To do item assignment in tuple we need to convert tuple into list
#Eg 1
a = (1,2,3,4,56)
aa = list((1,2,3,4,56))
aa[3] = 'srini' # item assignment
print(a)
print(aa)

# We can add tuple inside tuple
#Eg 1
a = (1,2,3,4,56)
print(a+(1,2,3))

# 1. inbuilt functions / methods use for tuple
