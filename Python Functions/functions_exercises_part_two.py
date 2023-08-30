# Functions Exercises Part 2

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
            "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]

print("\nQ2a\n")


# Q2a: write a function which takes a letter (as a string)
# as an input and outputs its position in the alphabet
# The index() method returns the position at the first occurrence of the specified value.
def letter_position(letter):
    # convert to lowercase
    letter = letter.lower()
    # index starts at 0 so add 1 if index expected is a = 1, b = 2 etc
    position = alphabet.index(letter)  # + 1

    return position


'''
# test function
# print entire alphabet with position
for current_letter in alphabet:
    position = letter_position(current_letter)
    print(f"'{current_letter}' is Position: {position}")
'''

# test function
user_input = input("Enter a letter: ")
letter_position = letter_position(user_input)
print(f"Position is {letter_position}")

print("\nQ2b\n")


# Q2b: create a function which takes a persons name as an input string and returns an
# ID number consisting of the positions of each letter in the name
# e.g. f("bob") = "1141" as "b" is in position 1 and "o" is in position 14

def get_id_number(name):
    name = name.lower()

    # initialise an empty string
    id_number = ""
    # loop through each letter
    for letter in name:
        if letter in alphabet:
            # find index which is the position of the letter where a = 0, b = 1, etc
            position = alphabet.index(letter)
            # convert position to a string and add to id number string
            id_number += str(position)
    return id_number


# test function
user_name = input("Enter a name: ")
user_id_number = get_id_number(user_name)
print(f"ID number: {user_id_number}")

print("\nQ2c\n")


# Q2c: Create a function which turns this ID into a password. The function should subtract
# the sum of the numbers in the id that was generated from the whole number of the id.
# e.g. f("bob") -> 1134 (because Bob's id was 1141 and 1+1+4+1 = 7 so 1141 - 7 = 1134)

def get_password(id_number):
    # initialise sum to 0
    sum_of_id_numbers = 0
    # iterated over each number in the id
    for num in id_number:
        # convert num to int and add to sum which is an int
        sum_of_id_numbers += int(num)
    # password is the id number int - sum
    password = int(id_number) - sum_of_id_numbers
    return password


'''
# generator expression version
#  generator is a function that returns an iterator
#  that produces a sequence of values when iterated over.
def get_password(id_number):
    # iterate through each num, convert to int, and calculate sum
    sum_of_id_numbers = sum(int(num) for num in id_number)
    # calculate password
    password = int(id_number) - sum_of_id_numbers
    return password
'''

# test function
# Example:
# name: jess
# id: 941818 where index j = 9, e = 4, s = 18,  s = 18
# 9 + 4 + 1 + 8 + 1 + 8 = 31
# password is 941818 - 31 = 941787
user_id = input("Enter an ID number: ")
user_password = get_password(user_id)
print(f"Password: {user_password}")
