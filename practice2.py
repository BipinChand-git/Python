nums = [2,7,9,11]
print(nums)
print(nums.index(2))
target = int(input("Enter the number:"))
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i] + nums[j] == target:
            print(i,j)

'''2nd question'''

# # s = "hello"
# # print(s[::-1])
# # list = ["H", "a", "n", "n", "a","h"]
# # print(list[::-1])

# # nums = [1,2,3]
# # nums.insert(4,3)
# # print(nums)

# my_list = [3,4,5,6,7]
# for i in my_list:
#     my_list.remove(i)
#     print(my_list)
# # print(my_list)
