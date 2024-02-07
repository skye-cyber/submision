'''Question 6: Count Vowels
Write a program that counts the number of vowels in a sentence.
'''


def vowel(text):
    vowel_list = 'aeiouAEIOU'
    counter = 0  # initialize counter
    for char in text:
        if char in vowel_list:
            counter += 1
        else:
            pass  # do nothing if character is not a vowel
    return counter


text = input("Enter text here::")
# use ascii '\033[0m' to display number of voiwels in green color
print(f"{text} => has \033[32m{vowel(text)}\033[0m vowels")
