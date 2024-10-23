#if-elif-else:
# a = 1
# b = 2
# if a > b: 
#     print("a is greater than b.")
# else:
#     print("b is greater.")


# a = 5
# b = 6
# print("True") if a > b else print("False")

# traffic_lights = input("Enter the traffic light:")
# if traffic_lights == "red": 
#     print("Stop!")
# elif traffic_lights == "green":
#     print("Go ahead.")
# elif traffic_lights == "yellow":
#     print("Look Ahead")
# else:
#     print("Something is Wrong.")

#Grades Based on the marks:

# marks = int(input("Enter the marks out of 100: "))
# if marks <= 100:
#     print("You got",marks,"marks. Here's your Grade:")
#     if marks >= 90:
#         print("You got 'A' Grade")
#     elif marks < 90 and marks >= 80:
#         print("You got 'B' Grade.")
#     elif marks < 80 and marks >= 70:
#         print("You got 'C' Grade.")
#     elif marks < 70:
#         print("You got 'D' Grade.")
# else:
#     print("You entered marks above 100.")

#Nesting if-else:
age = int(input("Enter the age: "))
if age <80:
    if age >= 18:
        print("You can drive or vote.")
    else:
        print("You can't drive or vote.")
else:
    print("You can't drive but can vote.")