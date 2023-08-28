def word_calc(word):
    # Dictionary to store point values for each letter
    point_values = {
        'a': 1, 'e': 1, 'i': 1, 'o': 1, 'u': 1, 'l': 1, 'n': 1, 'r': 1, 's': 1, 't': 1,
        'd': 2, 'g': 2,
        'b': 3, 'c': 3, 'm': 3, 'p': 3,
        'f': 4, 'h': 4, 'v': 4, 'w': 4, 'y': 4,
        'k': 5,
        'j': 8, 'x': 8,
        'q': 10, 'z': 10
    }

    # Convert the word to lowercase to handle uppercase letters
    word = word.lower()

    # Initialize the total score to 0
    total_score = 0

    # Calculate the score for each letter in the word and add it to the total score
    for letter in word:
        # If the letter is in the dictionary, add its corresponding point value to the total score
        if letter in point_values:
            # Add the point value of the letter to the total score
            total_score += point_values[letter]

    return total_score

# Test the function with the provided example
print(word_calc("zoo"))  # Output: 12
print(word_calc("bus"))  # Output: 5
print(word_calc("elephant"))  # Output: 13
print(word_calc("xylophone"))  # Output: 24
print(word_calc("ZOO"))  # Output: 12
print(word_calc("aaabbbcccddEEEE"))  # Output:29