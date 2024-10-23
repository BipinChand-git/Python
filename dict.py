# Dictionaries: Is used to store data values in "key-values" pairs.

# info = {
#     "name" : "Bipin",
#     "age"  :  21,
#     "is adult" : True,
#     21  :  21,
#     21.5  : 24.2,
#     (1,2,3) : ["tuple"],
#     True : 1,
#     None : 0,
#     "list" : ["value can be list",1,2],
#     "name" : "Chand",
# }
# print(info)
# print(len(info))

# null_dict = {}         #Empty Dictionary:
# print(null_dict)
# null_dict["name"] = "Bipin"
# null_dict["age"] = 21
# print(null_dict)
# print(type(null_dict))
# print(len(null_dict))

# '''print(null_dict[0])     #"Error": We can't access them using Indexing'''

# # So If we want to access the Data values in dictionary we can use keys to access them:

# print(null_dict["name"])
# print(null_dict["age"])


# Nested Dictionary:

# students = {
#     "student1" : {
#         "name" : "Bipin",
#         "age" : 21,
#         "subjects" : ("Python","C++")
#     },
#     "student2" : {
#     "name" : "Harsh",
#     "age" : 20,
#     "subjects" : ("Java","SQL")
#     },
#     "student3" : "Govind"
# }
# print(students)
# print(students["student1"])
# print(students["student2"]["age"])
# print(students["student3"])
# print(students["student1"]["subjects"])
# print(students.keys())
# print(list(students.keys()))        ##Typecasting<-

#  Dictionary Methods:

student = {                         #  .keys() method-
    "name" : "Bipin Rajwar",
    "age" : 21,
    "subjects" : {
        "physics" : 90,
        "Maths" : 98,
        "Chemistry" : 85,
    }
}
print(student)
print(student.keys())
print(list(student.keys()))
print(type(student.keys()))
print(len(list(student.keys())))

print(student.values())         #  .values() method-
print(len(list(student.values())))
print(type(student.values))

#  .items() - it returns all the key,value pairs as tuples.

print(student.items())
print(len(student.items()))
pairs = list(student.items())
print(pairs)
print(pairs[0])
print(pairs[0:2])
print(pairs[::-1])

#  .get() method- returns the value according to keys.
print(student.get("subjects"))
print(list(student.get("subjects")))
print(len(student.get("name")))     #--it will give the len of all the characters present in the value.

print(student["name"])
print(student.get("name"))

#  .update() method - insert or update the dictionary.

# student.update({"address" : "Pithoragarh" , "MobileNo." : 1234567789})
# print(student)

new_dict = {"address": "Pithoragarh","MobileNo." : 1234567899}
student.update(new_dict)
print(student)

new_dict = {"name" : "Bipin Chand"}
student.update(new_dict)
print(student)