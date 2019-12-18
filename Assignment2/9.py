# 9. Find the minimum element in an array of integers. You can carry some extra
# information through method arguments such as minimum value.

# array
array = [11,13,14,5,16,7]

def findMin(array):
   # when the length of the array is 0
    if len(array) == 1:
       return array[0]
    else:
       # return the min value
       return min(array[0], findMin(array[1:]))


# call the funtion
answer =findMin(array)
# print
print (answer)