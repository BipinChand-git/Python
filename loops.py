# while Loop----

# i = 1
# while i <= 5:
#     print("hello world",i)
#     i+=1                        # means i = i+1
# print(i)


# i = 0
# while i <= 5:
#     print(i)
#     i+=1
# print("loop ended:")

# j = 5       # TO print reverse the numbers:
# while j >= 1:
#     print(j)
#     j-=1                #means j = j-1
# print("Loop ended.")

# k = 1
# while k >= 0:
#     print(k)
#     k+=1
# print("loop ended")

#1. Print numbers from 1 to 100 using while loop.
# i = 1
# while(i <= 100):
#     print(i)
#     i+=1
# print("loop ended.")

# #2. print numbers from 100 to 1 using while loop.
# j = 100
# while(j >= 1):
#     print(j)
#     j-=1
# print("loop ended")

# #3. print the multiplication table of a number n :
# n = int(input("Enter the number for multiplication table:"))
# i = 1
# while(i <= 10):
#     print(n,"*",i,"=",n*i)
#     i+=1

#4. print the elements of list using a loop:
# list1 = [1,4,9,16,25,36,49,64,81,100]
# i=0             #index starts from 0-----
# while(i <= len(list1)-1):
#     print(list1[i])
#     i+=1

#5.Search for the number x in this list using loop.
x = int(input("Enter the number to find in the list:"))
list2 = [1,4,9,16,25,36,49,64,81,100]
print(len(list2))
j=0
while(j <= len(list2)-1):
    if x == list2[j]:
        print(x,"is find at index",j)
    j+=1
else:
    print(x,"is not in the list.")


# x = 81
# list2 = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# found = False
# index = 0

# while index < len(list2):
#     if list2[index] == x:
#         found = True
#         break
#     index += 1

# if found == True:
#     print(f"{x} found in the list.")
# else:
#     print(f"{x} not found in the list.")