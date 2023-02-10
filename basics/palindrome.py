# A palindrome is a word that reads the same backward and forward
# Ex. radar, Bob, Aya

import re

while True:
    str = input("Enter a word: ")

    if str == "exit":
        break

    # Regex pattern: we will keep these chars
    pattern = r'[^A-Za-z0-9]+'

    # Replace any chars that aren't in the pattern
    str = re.sub(pattern, '', str)
    str = str.lower()

    # Convert to char lists to do the comparison
    char_list = list(str)
    reversed_char_list = list(str)
    reversed_char_list.reverse()

    isPalindrome = True

    # Loop thru lists and compare char at index
    for i in range(len(char_list)):
        if char_list[i] != reversed_char_list[i]:
            isPalindrome = False

    if (isPalindrome):
        print(str + " is a palindrome")
    else:
        print(str + " is not a palindrome")