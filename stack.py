# Arrays (called lists in python) dynamic array
arr = [1, 2, 3]
print(arr)

# Can be used as a stack
arr.append(4) #push
arr.append(5)
print(arr)

arr.pop()
print(arr)

#LIFO(Last persons who got in, will get out early)

#unlike pushing and popping, inserting in the middle of an array is a Big(O) of n time operation
#arr.insert(1,7)

#not Big(O) of n times operation to index an array
#read and reassigning values
#constant time operation
arr[0] = 0
arr[3] = 0