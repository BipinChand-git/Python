#1  3inputs from user and store in a list.
# list = []
# movie1 = input("Enter your first favourite movie: ")
# movie2 = input("Enter your second favourite movie: ")
# movie3 = input("Enter your third favourite movie: ")
# list = [movie1,movie2,movie3]
# print(list)
# print(type(list))
# print(len(list))

#     #another way to do This:
# list1 = []
# list1.append(input("Enter your 1st movie: "))
# list1.append(input("Enter your 2nd movie: "))
# list1.append(input("Enter your 3rd movie: "))
# print(list1)


#2 palindrome check in list:
# person = [1,2,3,3,2,1]
# person1 = person.copy()
# print(person1)

# person1.reverse()
# print(person1)
# if person == person1:
#     print(person,"is a palindrome list.")
# else:
#     print(person,"is not a palindrome list.")

# #3  count the element in tuple:

# grades = ("C","D","A","A","B","B","A")
# students = grades.count("A")
# print(students,"students gets the 'A' grade")

# # Store the above values in list and sort them:

# grades_list =  ["C","D","A","A","B","B","A"]
# grades_list.sort()
# print("In Ascending Order:\n",grades_list)
# grades_list.sort(reverse = True)
# print("In Descending Order:\n",grades_list)

list1 = [1,2,4]
list2 = [1,3,4] 
new_list = list1 + list2
print(new_list)
new_list.sort()
print(new_list)