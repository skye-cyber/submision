'''Question 4: Capitalize Words
Write a program that accepts a string as input, capitalizes the first letter of each word in the
string, and then returns the result string.'''


def capitalize():
    messange = input("Enter a string:")
    # use title() method
    output = messange.title()
    return output


print(capitalize())