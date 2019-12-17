# 1. Sum of an array 


# take in the array and N the length
def findSum(arr, N):
    # if the length of the array is equal to one
    if len(arr)== 1:
        # print that element
        return arr[0]
    else:
        # take the first element and add it to each element in the array
        return arr[0]+findSum(arr[1:], N)


# input values
arr = [8, 6, 7, 4, 7]

# calculating length of the array
N = len(arr)

ans =findSum(arr,N)
print ('Sum of the array is equal to',ans)