'''Question 6: Count Vowels
Write a program that counts the number of vowels in a sentence.
'''


def vowel(text):
    vowel_list = 'aeiouAEIOU'
    counter = 0  # initialize counter
    set = []
    for char in text:
        # check whether the character if vowel is in the vowel set if not add it to the set else d0 nothing
        if char in vowel_list and char not in set:
            counter += 1
            set.append(char)
        else:
            pass  # do nothing if character is not a vowel
    return counter


text = input("Enter text here::")
# use ascii '\033[0m' to display number of voiwels in green color
print(f"{text} => has \033[32m{vowel(text)}\033[0m vowels")
