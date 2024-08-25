import re

def calculate_count(sentence):
    sentence = sentence.strip()  # Remove leading and trailing spaces
    if not sentence:
        return (0, 0, 0, 0, "")

    word_count = 0
    space_count = 0
    char_count = 0
    vowel_count = 0
    vowel_list = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
    
    # Initialize variables to build words from continuous characters
    temp_word = ""
    words = []
    
    for char in sentence:
        if char.isalpha():  # Consider alphabetic characters
            temp_word += char
            char_count += 1
            if char in vowel_list:
                vowel_count += 1
        else:
            if temp_word:
                words.append(temp_word)
                word_count += 1
                temp_word = ""
            if char == ' ':
                space_count += 1
    
    if temp_word:
        words.append(temp_word)
        word_count += 1
    
    formatted_sentence = ' '.join(words)
    
    return (word_count, space_count, char_count, vowel_count, formatted_sentence)

# Input sentence
sentence = input("Enter something : ")

# Calculate counts and formatted output
word_count, space_count, char_count, vowel_count, formatted_sentence = calculate_count(sentence)

# Print results
print('\nOutput: ', formatted_sentence)
print('Word count: ', word_count)
print('Space count: ', space_count)
print('Character count: ', char_count)
print('Vowel count: ', vowel_count)
