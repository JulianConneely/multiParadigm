# 8. Print an array - Given an array of integers prints all the elements one per line. This
# is a little bit dierent as there is no need for a 'return' statement just to print and recurse.

# Define the function
def print_array(array):
    # Set the base case, in this case, when the length of the array is 0.
    base_case = len(array)
    # if the base case has been reached return nothing
    if base_case == 0:
        return 0
    # Print the value at index 0 of the input array.
    else:
        print(array[0])
        print_array(array[1:])
# array of values
array = [3, 4, 5, 6, 7, 8, 10, 12 , 13]


# Call the function and print
print_array(array)



