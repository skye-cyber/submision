'''Question 5: Reverse Integer
Write a program that takes an integer as input and returns an integer with reversed digit
ordering.'''


# Define the reverse function to take an integer as input and return the reversed integer
def reverse(value):
    try:
        if isinstance(value, int):
            # Get the absolute value of the integer and reverse its digits
            result = str(abs(value))[::-1]
            # Convert the reversed string back to an integer
            return int(result) if len(result) > 0 else 0

        # Split the input string into parts separated by '-', reverse each part and join them back
        parts = value.split('-')
        reversed_parts = [int(i[::-1]) for i in parts]
        # Sum up all reversed parts and add a '-' sign if more than one part exists
        return sum(reversed_parts) if len(parts) > 1 else -abs(int(parts[-1][::-1]))
    except ValueError:
        # Raise an exception for invalid input
        print("Invalid Input")
        raise


# Define the reverse_negative_number function to store the input value globally
def reverse_negative_number(value):
    """
    This function processes the input value and calls the reverse function to get the reversed integer.

    :param value: An integer or a string representing an integer with an optional negative sign
    """
    global input_value
    input_value = value

# Main entry point of the script


if __name__ == "__main__":
    input_value = None
    try:
        if input_value is None:
            # Prompt the user for input and pass it to reverse_negative_number function
            value = int(input('Enter a number: '))
            reverse_negative_number(value)
            # Print the reversed integer with the negative sign if applicable
            print("Reversed Number is:", ("-%s" % (reverse(input_value))) if input_value < 0 else str(reverse(input_value)))
        else:
            # Process the predefined input value
            print("Reversed Number is:", ("-%s" % (reverse(input_value))) if input_value < 0 else reverse(input_value))
    finally:
        del input_value