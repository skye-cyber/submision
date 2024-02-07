'''Question 1: FizzBuzz
Write a program that prints the numbers from 1 to 100. For multiples of 3, print "Fizz"; for
multiples of 5, print "Buzz"; and for numbers that are multiples of both 3 and 5, print
"FizzBuzz".'''


def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print(f"{i} FizzBuzz")
        # check whether number is a mutiple of 3 taking its modulus
        elif i % 3 == 0:
            print(f"{i} Fizz")
        # check whether number is a mutiple of 5 taking its modulus
        elif i % 5 == 0:
            print(f"{i} Buzz")
        # no operation if the number is not a mutiple of 3 or and 5
        else:
            pass


fizzbuzz()