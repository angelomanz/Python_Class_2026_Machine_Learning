text ='Iam learning Python and I love it!'
total_characters_with_spaces = len(text)
total_characters_without_spaces = len(text.replace('' , ''))
words = text.split()
num_words = len(words)
total_words_length = sum(len(word) for word in words)

upper_text = text.upper()
lower_text = text.lower()


print(f'Total chars (with spaces): {len(text)}')
print(f'Total chars (no space):{len(text.replace("" , ""))}')
print(f'Number of words:{len(text.split())}')
print(f'Average word length:{sum(len(w) for w in text.split()) / len(text.split()):.2f}')
print(f'Uppercase: {text.upper()}')
print(f'Lowercase: {text.lower()}')