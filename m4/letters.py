# Module 4 In-Class Activity 1

word = input('Enter a word: ')
letter = input('Enter the letter to count: ')
num = 0

for char in word:
    if char == letter:
        num += 1

print(f'{letter} appears {num} times.')