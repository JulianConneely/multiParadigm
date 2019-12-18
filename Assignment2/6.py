#6. Find index in array for item. Given an array, and an element to search for return
# the index of the element in the array or -1 if the element is not present in the array.

# array of values
array = [4,3,8,5,6,7,9,13,21]

# counter
index=0

# number to find
number = 13

# define function take in the array, number to find and an index
def findIndex(array, number, index):
    # if the array index is equal to 13
    if array[0] == number:
        # return the the index
        return index
    else:
        # counting the index 
        index = index +1
        #print(i)
        return findIndex(array[1:], number, index)

# call the function
answer =findIndex(array,number, index)
# print
print (answer)