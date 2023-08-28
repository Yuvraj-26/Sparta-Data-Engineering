# scrabble word calc improved

def scrabble_calc(word):
    one_point_letters = ["a", "e", "i", "o", "u", "l", "n", "r", "s", "t"]
    two_point_letters = ["d", "g"]
    three_point_letters = ["b", "c", "m", "p"]
    four_point_letters = ["f", "h", "v", "w", "y"]
    five_point_letters = ["k"]
    eight_point_letters = ["j", "x"]
    ten_point_letters = ["q", "z"]

    word = word.lower()  # Convert the word to lowercase
    word_score = 0

    for char in word:
        if char in one_point_letters:
            word_score += 1
        elif char in two_point_letters:
            word_score += 2
        elif char in three_point_letters:
            word_score += 3
        elif char in four_point_letters:
            word_score += 4
        elif char in five_point_letters:
            word_score += 5
        elif char in eight_point_letters:
            word_score += 8
        else:
            word_score += 10

    return word_score


def validate_input(word):
    for char in word:
        if char.isalpha() is False:
            return False
    return True


while True:
    input_word = input("Enter a word (or type 'quit. (with a fullstop)' to exit): ")

    if input_word.lower() == 'quit.':
        print("Thanks for playing!")
        break

    if validate_input(input_word):
        score = scrabble_calc(input_word)
        print(f"The Scrabble score of '{input_word}' is {score}")
    else:
        print("Please enter a valid word containing only letters.")
