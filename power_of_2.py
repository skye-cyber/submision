'''Question 3: Power of Two
Write a program that takes an integer as input and returns true if the input is a power of two.
'''


def power(number):
    # special case for 0
    if number == 0:
        return False

    # keep dividing a number by 2 until it's not divisible anymore
    while number % 2 == 0:
        number //= 2

    if number == 1:
        return True
    else:
        return False


number = int(input("Enter a number:"))
print(f"Is{number} a power of 2?\033[32m {power(number)}\033[0m")  # write return value in green color using ASCII
