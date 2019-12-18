# 7. Sum of Digits Given a whole, number such as 23, return the sum of the digits in the
# number i.e. 2 + 3 = 5. For this would be useful to convert the number to a string
# then break it apart into digits.

# number
number = 888

def sumdig(number):
    # if it is equal to 0, return 0
    if number == 0:
        return number
    else:
        # otherwise modulo of the number is summed
        return number%10 + sumdig(number//10)

answer =sumdig(number)
print (answer)