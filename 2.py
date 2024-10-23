#String:

# str1 = """This is "apnacollege's" tutorial"""   #Valid
# str2 = "Usually we will use this."
# print(str1)
# print(str2)

# str3 = "This is a string. \nString is a sequence of Characters."   #Escape Sequence Character. new line character.
# print(str3)

# str4 = "This is a string. \tString is a sequence of Characters."  # For Tab Space.
# print(str4)

# str = "Bipin \"Rajwar"
# print(str)

#Basic Operations:
#Concatenation-

# str1 = "Bipin"
# str2 = "Rajwar"
# final_string = str1 + " " + str2
# print(final_string)
# print(len(str2))  # Length of string-
# length = len(final_string)
# print(length)
# ch = str1[0]  #Indexing:
# print(ch)
# print(str2[4])

# Slicing:

# str = "Bipin Rajwar"
# print(str[0:5])
# print(str[0:4])
# print(str[0:8])
# print(str[0:11])
# print(str[0:12])
# print(str[0:len(str)]) #SAME as above line-
# print(str[0:])
# print(str[:5])

# Negative Index:
# str = "apple"
# print(str[-5:len(str)])
# print(str[:])
# print(str[-1:-6 :-1])
# print(str[::-1])
# print(str[0:6:1])

# String Functions:
#Str.endswith("substring"):

# str = "I am a coder."
# print(str.endswith("er."))

#   # str.capitalize()
# str1 = "i am a coder."
# print(str1.capitalize())
# print(str1)
# str1 = str1.capitalize()
# print(str1)

# str2 = "I am Learning Python."
# str2 = str2.replace("Python","Java")
# print(str2)

str3 = "I am from Pithoragarh."
print(str3.find("f"))
print(str3.find("Pithoragarh"))
print(str3.find("not"))
print(str3.count("from"))
print(str3.count("Q"))