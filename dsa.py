# def generate_subsets(nums):
#     def backtrack(start, path):
#         # Add the current subset to the result
#         result.append(path)
#         # Generate all possible subsets by including each number starting from 'start'
#         for i in range(start, len(nums)):
#             # Include nums[i] in the current subset and proceed recursively
#             backtrack(i + 1, path + [nums[i]])

#     result = []
#     backtrack(0, [])
#     return result

# # Example usage
# nums = [1, 2, 3]
# print(generate_subsets(nums))



#2nd:
def permute(string):
    def backtrack(path, choices):
        # If the path has the same length as the original string, we have a complete permutation
        if len(path) == len(string):
            result.append(''.join(path))
            return
        # Iterate through all choices
        for i in range(len(choices)):
            # Include the current choice in the path and proceed recursively
            backtrack(path + [choices[i]], choices[:i] + choices[i+1:])

    result = []
    backtrack([], list(string))
    return result

# Example usage
string = "abc"
permutations = permute(string)
for perm in permutations:
    print(perm)


#3. 
def trap(height):
    if not height:
        return 0

    left, right = 0, len(height) - 1
    left_max, right_max = height[left], height[right]
    water_trapped = 0

    while left < right:
        if height[left] < height[right]:
            left += 1
            left_max = max(left_max, height[left])
            water_trapped += left_max - height[left]
        else:
            right -= 1
            right_max = max(right_max, height[right])
            water_trapped += right_max - height[right]

    return water_trapped

# Example usage
height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(trap(height))  # Output: 6

#4.
def longest_consecutive(nums):
    num_set = set(nums)
    longest_streak = 0

    for num in num_set:
        # Only start counting if 'num' is the start of a sequence
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1

            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1

            longest_streak = max(longest_streak, current_streak)

    return longest_streak

# Example usage
nums = [100, 4, 200, 1, 3, 2]
print(longest_consecutive(nums))  # Output: 4

#5 Q5Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that
#is missing from the array. Implement an efficient algorithm in O(n) time complexity..

def find_missing_number(nums):
    n = len(nums)
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum

# Example usage
nums = [3, 0, 1, 4, 5, 6]
print(find_missing_number(nums))  # Output: 2
