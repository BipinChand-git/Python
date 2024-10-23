# marks = [23,34,34,45,68,"BipinChand"]
# print(marks)
# print(type(marks))
# print(len(marks))

# We can access values present in the list using indexing.

# print(marks[0])
# print(marks[0:4])  #list Slicing:
# print(marks[5])
# print(type(marks[5]))
# print(type(marks[0]))
# print(len(marks[5]))

# Strings and Lists:
# str = "hello world!"
# print(str[0])

# list1 = ['karan',23,'alibagh']
# print(list1[0])
# list1[0] = 'arjun'
# print(list1)

#List slicing:

# marks = [45,34,33,22,34]
# print(marks[1:2])
# print(marks[0:])
# print(marks[0:len(marks)])
# print(marks[:4])
# print(marks[-5:-3])
# print(marks[: :-1])
# print(marks[6])

# List Methods():

# marks = [7,3,5,12]
# marks.append(10)
# print(marks)

# marks.sort()    #Sorts automatically in ascending order:
# print(marks)

# marks.sort(reverse = True)   #Sorts in descending order:
# print(marks)


# list = ["litchi","banana","grapes","apple"]
# list.sort()
# print(list)
# list.sort(reverse = True)
# print(list)

list1 = [2,4,6,8,9]
list1.reverse()  #Reverse the list using reverse() method.
print(list1)
list2 = ["apple","grapes",'banana',"guava"]
list2.reverse()
print(list2)

list3 = [23,34,33,21,45,67,45]  # inserting a element in the list at particular index:
list3.insert(2,31)
print(list3)

list3.remove(45)         # removing the value when it found first.
print(list3)

list3.pop(0)    #it will remove the value present at index 0:
print(list3)

list3.pop(3)
print(list3)

list3.insert(2,31)
print(list3)

print(list3.count(31))  #count the occurrence of element in list.



# n = int(input("Enter the number"))
# list = []
# i = 0
# while i<=n:
#     list.insert(i,n)
#     i+=1
# print(list)