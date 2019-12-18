# 5. Replace a given character with '*'. Given a string, and a character to replace,
# return a string where each occurance of the character is replaced with '*'.

# statement
statement = "Recursion is not rocket surgery"

# takes in statement, old character, new character
def replaceChar(statement, old, new):
    # if statement contains no characters return nothing.
    if statement == '':
        return ''
    # if the character in the string is the same as the specified character
    # then replace it with the new character and call the function recursively.  
    if statement[0] == old:
        return new + replaceChar(statement[1:], old, new)
    return statement[0] + replaceChar(statement[1:], old, new)


#old character
old = 'n'
# new character
new = '*'

# call and print the result of replacing the specified character in the statement
print(replaceChar("Recursion is not rocket surgery", 'n', '*'))