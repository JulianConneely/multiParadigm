# 3. Remove all odd numbers 

def removeOdds(array):
    # If the input array contains no values return an empty list
    if not array:
        return []
    # otherwise use modulo to check that the value in the 1st position of the array 
    # returns a remainder.
    if array[0] % 2 == 0:
        # if it does not (ie is even) return the even number and continue recursion
        return [array[0]] + removeOdds(array[1:])
    return removeOdds(array[1:])


# input values to list
array = [3, 4, 5, 6, 7, 9, 2, 16]

print(removeOdds(array))