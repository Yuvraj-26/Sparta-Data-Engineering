"""
Python Fundamentals

Python
Open source
Multi platform
Large and active community
Supporting libraries
Web - django and flask
Data science - numpy, pandas, SciPy
ML - tensor flow, keras

Data types: Integers, Floating Point Numbers, Strings, Boolean

# Math operators: + - * / % (modulo)`
print(55 * 5)

# string functions

print unicode
print (u'\u0061')

# print index
("hello world"[0]) # 0 index is h
print("hello world"[1])
print("hello world"[-1]) # last character
print("hello world"[-1]) # penultimate from last character
fruit = "passionfruit"
print(fruit[0:7])
print(fruit[-5])


# Boolean (True OR False)
# Equality operators: equal to == , != , >, <, >=. <=

print(type(True))
print(4 == 4)
print(4 != 3)
print(4 > 5.5)
print(2 == len("2"))

# Truthy or falsey (generate true or false depending on state)
# bool function
# anything other than 0 is considered true
print(bool(1))
print(bool(2))
print(bool(0))
print(bool(-1))
print(bool("world"))
print(bool("")) # empty string returns false
print(bool(" ")) # string returns true (space)

# variables (Use Python style Guide)
a = 4
b = 4.5
print(a + b)
more_than_one_word = 'snake case'
print(more_than_one_word)

# String concatenation and Escape characters
first_name = 'manny'
last_name = 'm'
age = 21
full_name = first_name + ' ' + last_name
# casting integer to string to print message
print(full_name + ' ' + str(age))

# Escape character
text = "someone then said, \"text can be tricky\""
print(text)
text = "someone then said, \'text can be tricky\'"
print(text)

# String Methods (Search Python string methods)
first_name = "pineapple"
print(first_name.capitalize())
print(first_name.upper())
print(first_name.replace('e', 'x'))

# Control Flow
# If statement
if 2 == 2:
    print("These numbers are equal")

# Exercise
customer_age = 18
if customer_age <= 12:
    print('U, PG, and 12 films available')
elif customer_age <= 15:
    print("U, PG, 12, 15 films available")
else:
    print("All films available")

time_of_day = 6

# Or and And

if time_of_day > 5 and time_of_day < 12:
    print('Good morning')
elif time_of_day > 12 and time_of_day < 18:
    print('Good afternoon')
else:
    print('Good evening')

# Collections
# lists / Arrays
# single data types ideal
example_list = [1, True, "string"]
print(type(example_list))
print(example_list)
print(example_list[0])
print(example_list[-1])
print(example_list[-2])
print(example_list[1])

shopping_list = ["eggs", "bread", "milk"]
shopping_list[1] = "apples"
shopping_list.append("grapes")
shopping_list.pop(0)
print(shopping_list.index("milk"))

# Dictionary / HashMap or Map - {key, value} pairs

# key value pairs
contacts_list = {
    "jane": "0123456789"

}

contacts_list["bob"] = "111111112222" # add to dict
contacts_list["bob"] = "new number" # add to dict
print(type(contacts_list)) # print type dict
print(contacts_list)
print(contacts_list["jane"]) # print number using specified key
print(contacts_list.keys()) # print all keys
print(contacts_list.values()) # print all values
print(contacts_list.pop("jane")) # pop by specifying key
print(contacts_list)

contact_list = {
    "a": {
        "anne": "0000000000"
    },
    "b": {
        "bob": "1111111111"
    },
    "c": {
        "charles": "22222222"
    }
}

# print(contact_list['b']) # print using b key
# print(contact_list['b'].keys()) # returns a dictionary, use keys method to see contacts under b key
print(contact_list['b']['bob']) # returns number by specifying key


# Loops
# While
# infinite loop
loop_control = True # False does not run
while loop_control:
    print("I am a loop")


counter = 0
while counter < 10:
    if counter % 2 == 0:
        print(counter)
    else:
        print("odd number")
    counter += 1


# Number guessing game

import random

game_random_number = random.randint(1,100)

game_active = True

while game_active:
    # print(type(game_random_number))
    game_start_message = "guess a number between 1 and 100"
    # print(input())
    user_guess = int(input())  # returns int which cannot be compared with str
    if user_guess == game_random_number:
        print("Correct")
        game_active = False
    elif user_guess < game_random_number:
        print("Too low, try again")
    else:
        print("Too high, try again")



# For Loop

example_string = "test"
basket = ["eggs", "bread"]

for basket_item in basket:
    print(basket_item)

# dictionary for loop
customers = {
    "name": "tess",
    "age": 28
}

for customer in customers.values():
    print(customer)


# Functions DRY - Dont repeat yourself
def print_item(first_name, last_name):
    print(first_name + ' ' + last_name)

print_item("bob", "bloggs")


def full_name(first_name, last_name):
    return first_name + ' ' + last_name

def print_name(data_type):
    print(data_type)

print(full_name("jane", "bloggs"))


# calc

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

choice = int(input('\n Enter 1 for addition and 2 for subtraction: '))
num1 = int(input("\n input first num"))
num2 = int(input("\n input second num"))

if choice == 1:
    print(num1, '+', num2, '=', add(num1, num2))
elif choice == 2:
    print(num1, '-', num2, '=', subtract(num1, num2))
else:
    print('invalid')



# Scrabble score calc

one_point_letters = ["a", "e", "i", "o", "u", "l", "n", "r", "s", "T"]
two_point_letters = ["d", "g"]
three_point_letters = ["b", "c", "m", "p"]
four_point_letters = ["f", "h", "v", "w", "y"]
five_point_letters = ["k"]
eight_point_letters = ["j", "x"]
ten_point_letters = ["q", "z"]

def scrabble_calc(word):
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


print(scrabble_calc('zoo'))


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
        print("Thank you for playing!")
        break

    if validate_input(input_word):
        score = scrabble_calc(input_word)
        print(f"The Scrabble score of '{input_word}' is {score}")
    else:
        print("Please enter a valid word containing only letters.")
"""