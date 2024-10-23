#Tuples: Immutable sequence of values.

tup = (2,3,4,5,6)
print(tup)
print(type(tup))

tup1 = ()    # Empty Tuple:
print(tup1)
print(type(tup1))

tup2 = (2,)   #if we have single element present in the tuple then we create it like this (,) is mandatory.
print(tup2)
print(type(tup2))

tup3 = (3) #otherwise it will become integer without (,):
print(tup3)
print(type(tup3))

print(len(tup))  # can calculated length too.

print(tup[0])      #We can access each value using indexing.
print(tup[0:3])     #Slicing can used too.
print(tup[ : : -1])         #Negative Slicing is also used.
print(tup[-4 : -1])



'''tup[0] = 4    #Error :::::can't change tuple because it's immutable.'''


tup5 = ("bipin", 24 , 54,47.0,)
print(tup5)
print(type(tup5))
print(len(tup5))

# Tuple Methods:

score = (2,6,8,12,8,23,25)
print(type(score))
print(score.index(25))       #tup.index(element)-to find index of an element.

print(score.count(2))       #tup.count(element)- to count the occurrences of an element.