# Name-Rhozalin Nath
# PS ID: 2050395

input_word= input()
word=input_word.replace(" ","")
if word == word[::-1]:
    print(f"{input_word} is a palindrome")
else:
    print(f"{input_word} is not a palindrome")
