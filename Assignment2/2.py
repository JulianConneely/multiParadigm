# 2. Product of an array 

test_array = [5,6,9,6,8,10,12]

# define the recursive function.
def prodarray(test_array):
    # Define the base case for the function.
    base_case = len(test_array)
    # If the length of the array is 1 this will return the only value in the array as this is the sum.
    if base_case == 1:
        return test_array[0]
    # Otherwise the function adds the value in index 0 with the output of the function 
    # when applied to value at index 1.
    else:
        multiplied = test_array[0]*prodarray(test_array[1:])
        return multiplied

# Print the result of calling the function
print("The product of this array is", prodarray(test_array))