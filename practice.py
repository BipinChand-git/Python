'''Swapping first and last number in the list'''

list1 = [2,4,6,8,3,9,5,7]
# print(type(list1))
# print(len(list1))
# print(list1)
# print(list1[0])
# x = list1[0]
# list1[0] = list1[len(list1)-1]
# list1[len(list1)-1] = x
# print(list1)

#2nd method:
# list1[0] , list1[-1] = list1[-1] , list1[0]
# print(list1)


#3rd method-
# x = list1.pop(0)
# print(list1)
# y = list1.pop(len(list1)-1)
# print(list1)
# list1.insert(0,y)
# print(list1)
# list1.append(x)
# print(list1)

# list_x = [1,2,3,4,5]
# result = list_x.sort()
# print(list_x)
# print(result)  #sort return none value

'''1st:::print the sum of the current and previous number.'''
# prev_num = 0
# for i in range(0,11):
#     sum = prev_num + i
#     print("Current Number:",i ,"Previous Number:", prev_num ,"sum:",sum)
#     prev_num = i

# current_number = int(input("Enter the number:"))
# previous_number = 0
# while(previous_number < 5):
#     sum = current_number + previous_number
#     print(current_number, previous_number, sum)
#     previous_number = current_number
#     current_number += 1

'''2nd question: str= "pynative" print characters present at only even index value: '''    
str = "pynative"
i = len(str)
for i in range(0 , len(str)-1 , 2):
    print(str[i])

#using slicing:

str = "pynative"
i = list(str)
print(i)
print(list(i))




 
    