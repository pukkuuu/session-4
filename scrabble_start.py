# Scrabble scores for each letter
letter_scores = {
    'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4,
    'I': 1, 'J': 8, 'K': 5, 'L': 1, 'M': 3, 'N': 1, 'O': 1, 'P': 3,
    'Q': 10, 'R': 1, 'S': 1, 'T': 1, 'U': 1, 'V': 4, 'W': 4, 'X': 8,
    'Y': 4, 'Z': 10

def calculate_score(word):
    score = 0
    for letter in word.upper():
        score += letter_scores.get(letter, 0)
    return score

def level_1():
    word = input("Enter a word: ")
    score = calculate_score(word)
    print(f"The score for {word} is {0}")
level_1()

