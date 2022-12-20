# str - iterable datatype
# each and every element will be considered

# STRING:
#Eg 1
a = str(1234)
print(a)

# Length:
#Eg 1
i = "srini"
print(len(i))

# Positive Index Number:
# Indexing starts from 0 to lenght-1
#Eg 1
i = "srini"
print(i[2])

# Negative Index Number: (r8 to left)
# Indexing starts from -1 to -length
#Eg 1
i = "srini"
print(i[-2])

# String Indexing:
# We can take one element ata atime from string:
# Syntax:- string_variable/string[index_number]
#Eg 1
i = "srini"
print(i[3])

#Eg 2
i = "srini"
print(i[len(i)-1])

#String Slicing:
#Eg 1
a = "I Love India"
print(a[2:6])

#Eg 2
a = "I Love India"
print(a[2:5+1])

# String Slicing In Reverse Direction:
# Syntax:- string_variable/string[ start_index_number : end_index_number+1 : skip    ]
#Eg 1
a = "I Love India"
print(a[5:2-1:-1])

#Eg 2
a = "I Love India"
print(a[5:1:-1])

#Eg 3
a = "I Love India"
print(a[::-1])

# String Methods:
# Upper:
a = "srini"
print(a.upper())

# Lower:
a = "SRINI"
print(a.lower())

# Count:
# Check for the continuous substring
# Casesensitive
#Eg 1
a = "I Love India"
print(a.count("India"))
print(a.count("I Love India"))
print(a.count(""))
print(a.count("4")) # Not available so the output is 0

# Index:
# Index of first occured substring
# Check for the continuous substring
# Casesensitive
# Substring is not there it will throw error
#Eg 1
a = "I Love India"
print(a.index("India"))
print(a.index("Love"))
#print(a.index("4")) # ValueError: substring not found

# Find:
# Siminlar to index
# Substring is not there it will -1 as output
#Eg 1
a = "I Love India"
print(a.find("India"))
print(a.find("4")) # substring not found then the output is -1

# Is Alpha:
#Eg 1
a ="srini"
print(a.isalpha())

#Eg 2
a ="srini3"
print(a.isalpha())

# Is Alpha Numeric:
#Eg 1
a ="srini"
print(a.isalnum())

#Eg 2
a ="srini3"
print(a.isalnum())

#Eg 3
a ="srini 3"
print(a.isalnum())

#Eg 4
a ="srini_3"
print(a.isalnum())

# Strip:
# Remove whitespace at exteremes
#Eg 1
a = "  srini  "
print(a.strip())

#Right Strip:
#Eg 1
a = "  srini  "
print(a.rstrip())

#Left Strip:
#Eg 1
a = "  srini  "
print(a.lstrip())

#Capitalize:
#Eg 1
a = "srini"
print(a.capitalize())

# Join:
# Substring is going to get added b/w all the elements
# (i.e) except extremes
# Join will only take str. it will not take int
# Syntax:- 'substring'.join(string/list)
#Eg 1
a = "srini"
print("5".join(a))
print("-".join(a))

# Split:
# It is going to break the string wherever it founds its substring
# Substring will not be in your output
# Always elements before  substring and after  substring should be considred
# Always the output will be in a format of list
#Eg 1
a = "srini"
print(a.split("n"))