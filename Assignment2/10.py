# Verify the parentheses Given a string, return true if it is a nesting of zero or more
# pairs of parenthesis, like “(())” or “((()))”.
# The only characters in the input will be parentheses, nothing else
# For them to be balanced each open brace must close and it has to be in the correct order

# ref. https://www.geeksforgeeks.org/check-for-balanced-parentheses-in-python/

def check(my_string): 
    brackets = ['()', '{}', '[]'] 
    while any(x in my_string for x in brackets): 
        for br in brackets: 
            my_string = my_string.replace(br, '') 
    return not my_string 
   
# Driver code 
string = "{[]{()}}"
# The zero means that "" is an input which would return true i.e. the empty string
print(string, "-", "True" 
# It's false anytime the braces don't balance for example "((", "(()", or "((())))".
      if check(string) else "False") 