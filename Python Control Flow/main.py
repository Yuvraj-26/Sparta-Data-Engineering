from control_flow_exercises import *

x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]
names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson", "Annie Easley", "Terence Tao"]
list_of_lists = [[1, 5, 7, 3, 44, 4, 1],
                 ["A", "B", "C"],
                 ["Hi", "Hello", "Ciao", "By", "Goodbye", "Ciao"],
                 ["one", "Two", "Three", "Four"]]

print("\nQ1a\n")
# Q1a: Print only the first 5 numbers in this list
print_first_five_numbers(x)

print("\nQ1b\n")
# Q1b: Now print only the even numbers in this list (the elements that are themselves even)
# assumption: print 2 as speedster elements
print_even_numbers(x)

print("\n\nQ1c\n")
# Q1c: Now only print the even numbers up to the fifth element in the list (e.g. 2, 4, 34)
print_even_numbers_up_to_fifth_element(x)

# -------------------------------------------------------------------------------------- #

print("\n\nQ2a\n")
# Q2a: from the list of names, create another list that consists of only the first letters of each first name
# e.g. ["Alan Turing", "Leonardo Fibonacci"] -> ["A", "L"]
new_first_letters = get_first_letters(names)
print(new_first_letters)

print("\n\nQ2b\n")
# Q2b: from the list of names, create another list that consists of only the index of the space in the string
# HINT: use your_string.index("substring")
new_index_of_spaces = get_index_of_space(names)
print(new_index_of_spaces)

print("\n\nQ2c\n")
# Q2c: from the list of names, create another list that consists of the first and last initial of each individual
initials = get_initials(names)
print(initials)

# testing
# for name in names:
#    split_name = name.split()
#    print(split_name)

# -------------------------------------------------------------------------------------- #


print("\n\nQ3a\n")
# Q3a: Here is a list of lists, print only the lists which have no duplicates
# Hint: This can be easily done by using sets as a set does not contain duplicates
# expected output is second and fourth sub lists printed out
print_lists_with_no_duplicates(list_of_lists)

# -------------------------------------------------------------------------------------- #


print("\n\nQ4a and Q4b\n")


# Q4a: Using a while loop, ask the user to input a number greater than 100, if they enter anything else,
# get them to enter again (and repeat until the conditions are satisfied). Finally print the number that
# they entered
# Q4b: Continue this code and print "prime" if the number is a prime number and "not prime" otherwise
# prime numbers greater than 100: 101, 103, 107, 109, 113, 127, ..., 199, 211, 223, and 227


def main():
    # get number
    new_number = get_number_greater_than_one_hundred()
    print("You entered:", new_number)

    # check if prime
    if is_prime(new_number):
        print("Your number IS Prime")
    else:
        print("Your number IS NOT Prime")


if __name__ == "__main__":
    main()
