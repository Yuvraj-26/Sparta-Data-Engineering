def sort_by_length_of_words(sentence):
    # Split the sentence into individual words
    words = sentence.split(" ")
    word_lengths = []  # A list to store the length of each word

    # Calculate the length of each word and store it in word_lengths list
    for word in words:
        word_lengths.append(len(word))

    # Now, sort the words based on their corresponding lengths using Bubble Sort
    for i in range(len(words)):
        for j in range(i, len(words)):
            # Swap the words and their lengths if the current word's length is less than the previous word's length
            if word_lengths[j] < word_lengths[i]:
                # Swap the lengths in word_lengths list
                temp_length = word_lengths[j]
                word_lengths[j] = word_lengths[i]
                word_lengths[i] = temp_length

                # Swap the words in the words list
                temp_word = words[j]
                words[j] = words[i]
                words[i] = temp_word

    return words


# Test the function
sentence = "brazil italy jamaica portugal trinidadandtobago argentina madagascar uk usa canada"
result = sort_by_length_of_words(sentence)
print(result)