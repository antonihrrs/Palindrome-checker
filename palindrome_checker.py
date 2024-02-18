
get_word = str(input("Enter a word : "))

word_to_letter = [letter for letter in (get_word)]
print(word_to_letter)

list_copy = word_to_letter.copy()
print (list_copy)

list_copy.reverse()
print(list_copy)

if list_copy == word_to_letter :
    print(f"{get_word} is a palindrome")
else :
    print(f"{get_word} is not a palindrome")
