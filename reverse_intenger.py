'''Question 5: Reverse Integer
Write a program that takes an integer as input and returns an integer with reversed digit
ordering.'''


def reverse(value):
    # convert the number into a string rever the string and convert it to a number again
    return int(str(value)[::-1])


value = int(input("Enter a number:"))
print("Reversed number is:", reverse(value))