# tuple = (1,2,2,3,3,4,5,6)
# print(tuple)
# tuple2= ()

# for i in range (len(tuple)):
#     for j in range (i+1,len(tuple)):
#         if tuple[i]==tuple[j]:
#             tuple2(i,j)

# n= int(input("Enter the number:"))
# i = 0
# while i < n:
#     print(i**2)
#     i+=1


year = int(input("Enter the year:"))
if year%4==0:
    if year%100==0:
        if year%400==0:
            print("leap year")
        else:
            print("Not a leap year")
    else:
        print("leap year")
else:
    print("Not a leap year")