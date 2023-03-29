#########################################################################
# Program: m7 Class exercise #7a Sets Challenge Exercise #5
# Programmer: Isaiah Vann
# Class: CMPR 114 Spring 2023
# Instructor: Professor Durendal Huynh
# Date: 3/27/23
#########################################################################

# This program counts the number of times
# the letter T (uppercase or lowercase)
# appears in a string.

def main():
    # Create a variable to use to hold the count.
    # The varaible must start with 0.

    count = 0

    # Get a string from the user.
    my_string = input('Enter a sentence: ')

    # Count the Ts.
    for ch in my_string:
        if ch == 'T' or ch == 't':
            count += 1
    
    # Print the result.
    print(f'The letter T appears {count} times.')

# Call the main function.
# Execute the main function
if __name__ == '__main__':
    main()