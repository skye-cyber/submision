# Question 2: Fibonacci Sequence
# Write a program to generate the Fibonacci sequence up to 100.

def fibonacci():
    # initiaze sequence using the initial numbers of the sequence 0 and 1
    num1, num2 = 0, 1
    # print num1, num2
    print(num1)
    print(num2)
    while (num1 + num2) <= 100:
        # calculate next number in the sequence
        next_num = num1 + num2

        # update num1 and num2 for the next iteration
        num1, num2 = num2, next_num

        print(next_num)


print("Fibonacci sequence up to 100:")
# display the sequence
fibonacci()

