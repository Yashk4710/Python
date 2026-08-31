'''WAP to enter marks of 3 subjects from the user and store them in a dictionary.
start with an empty dictionary and empty dictionary and add one by one. use subject name as key 
and marks as value.'''
marks = {}
x = int(input("enter phy :"))
marks.update({"phy" : x}) 

x = int(input("enter chem :"))
marks.update({"chem" : x}) 

x = int(input("enter math :"))
marks.update({"math" : x}) 

print(marks)
