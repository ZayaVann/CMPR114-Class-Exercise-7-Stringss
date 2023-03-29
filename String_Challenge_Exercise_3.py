#########################################################################
# Program: m7 Class exercise #7a Sets Challenge Exercise #3
# Programmer: Isaiah Vann
# Class: CMPR 114 Spring 2023
# Instructor: Professor Durendal Huynh
# Date: 3/27/23
#########################################################################

# This program deomonstrates how to tokenize strings.

def main():
    # Strings to tokenize
    str1 = 'one to three four'
    str2 = '10:20:30:40:50'
    str3 = 'a/b/c/d/e/f'

    # Display the token in each string.
    display_tokens(str1, ' ')
    print()
    display_tokens(str2, ':')
    print()
    display_tokens(str3, '/')
    print()

# The display_tokens function displays the tokens
# in a string. The data parameter is the string 
# to tokenize and the delimiter parameter is the 
# delimiter.
def display_tokens(data, delimter):
    tokens = data.split(delimter)
    for item in tokens:
        print(f'Token: {item}')

# Execute the main function.
if __name__ == '__main__':
    main()