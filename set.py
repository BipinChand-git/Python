# Set - collection of unordered,unique & immutable items.

nums = {1,2,4,3}
print(nums)

collection = {1,3,2,5,2,2,"hello", 12.5, "world","world"}
print(collection)
print(len(collection))
print(type(collection))

Empty_Set = set()       #Empty Set----
print(type(Empty_Set))

# Set Methods()----

new_set = set()
new_set.add(1)              # .add() method--
new_set.add(2)
new_set.add("hello")
new_set.add(2)
new_set.add((1,2,3))        #It is a tuple so we can pass the tuple to set.
'''new_set.add([2,4,5])        #Error : Unhashable type:'''
print(new_set)
print(len(new_set))

new_set.remove("hello")
print(new_set)
print(len(new_set))
new_set.remove((1,2,3))
print(new_set)

new_set.clear()             # .clear() method -Empties the set--
print(new_set)

new_set.add("banana")
new_set.add("mango")
new_set.add("apple")
new_set.add("guava")
print(new_set)

new_set.pop()               # .pop() methods remove the elements randomly.
new_set.pop()
print(new_set)

collection1 = {"hello","world","welcome"}
print(collection1)
'''collection1.remove("output")   #Raise Error:'''
collection1.discard("output")


# Union and intersection in python sets:

set1 = {1,2,3}              #Union:
set2 = {2,3,4}
final_set = set1.union(set2)
print(final_set)

final_set = set1.intersection(set2)
print(final_set)
