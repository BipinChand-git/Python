#1 Even or Odd:

# num = int(input("Enter the number: "))
# if num % 2 == 0:
#     print("Entered Number is Even.")
# else:
#     print("Entered Number is Odd.")

#Without modulus operator check even or odd:

# n = int(input("Enter the number: "))
# x = int(n / 2) * 2
# if x == n:
#     print("Number is Even.")
# else:
#     print("Number is Odd.")

#2 Greatest of three numbers:

# num1 = int(input("Enter the value for num1->"))
# num2 = int(input("Enter the value for num2->"))
# num3 = int(input("Enter the value for num3->"))
# if num1 > num2 and num1 > num3:
#     print(num1,"is the greatest among them.")
# elif num2 > num1 and num2 > num3:
#     print(num2,"is the greatest among them.")
# else:
#     print(num3,"is the greatest among them.")

# Number is multiple of 7 or not:

# num = int(input("Enter the number->"))
# if num % 7 == 0:
#     print(num,"is multiple of 7.")
# else:
#     print(num,"is not a multiple of 7.")

# Greatest of four numbers:

num1 = int(input("Enter the value for num1->"))
num2 = int(input("Enter the value for num2->"))
num3 = int(input("Enter the value for num3->"))
num4 = int(input("Enter the value for num4->"))
if num1 >= num2 and num1 >= num3 and num1 >= num4:
    print(num1,"is the greatest among them.")
elif num2 >= num3 and num2 >= num4:
    print(num2,"is the greatest among them.")
elif num3 >= num4:
    print(num3,"is the greatest among them.")
else:
    print(num4,"is the greatest among them.")