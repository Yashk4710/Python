#Dictionaries are used to store data values in key.value pairs
#they are unorded, mutable(changeble) & don't allows duplicate keys
'''
info = {
"name" : "Yash",
"age" : 19,
"std" : "2nd year",
"subject" : ["OOP", "BCN", "DSA", "DELD", "DF", "UHV"],
"marks" :(98, 87 , 67, 87),
19 : 20
}

info["age"] = 20 #overwrite
info["surname"] = "katarnaware"
print(type(info))
print(info["name"])
print(info)

null_dict = {}
null_dict["name"] = "Yash Katarnaware"

null_dict["age"] = 19 
print(null_dict)
'''
#Neasted dictionary
'''
Student = {
"Name": "Yash",
"Subject" : {
    "phy" : 92,
    "chem" : 95,
    "math" : 99
}

}
print(Student)
print(Student["Subject"])
print(Student["Subject"]["math"])
'''
'''Student = {
"Name": "Yash",
"Subject" : {
    "phy" : 92,
    "chem" : 95,
    "math" : 99
    }
}
print(Student.keys())
print(list(Student.keys())) #return all keys
print(len(Student))

print(Student.values())
print(list(Student.values())) #return all values


print(Student.items()) #return all (key, val) pairs as tuples
Pairs = list(Student.items())
print(Pairs[1])

print(Student.get("Name")) #returns the key acording to value
print(Student.get("name"))

Student.update({"city" : "nashik"}) #insert the specified items to the Dictionary
print(Student)
'''

#Set in python

'''collection = {1, 2, 5, "Yo", "Yeah", 6, 6, 6} #Set are ignore repeated values
print(collection)
print(type(collection))
print(len(collection)) #total number of items

collection1 = {} #empty dictionary 
collection2 = set() #empty set ; syntax
print(type(collection1))
print(type(collection2))
'''
#set method
'''collection = set() #empty set
collection.add(2) #adds an element
collection.add(5)
collection.add("spidey")
#collection.remove(5) #remove the element
#collection.clear() #empties the set 
print(collection)
print(len(collection))'''

'''collection = {"yash", "spidey", "Yo", "hello"}
print(collection.pop())'''

set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1.union(set2)) # combines both set values & return new 
print(set1)
print(set2)
set3 = {1, 2, 3}
set4 = {3, 4, 5}
print(set3.intersection(set4)) #combines common value & returns new
