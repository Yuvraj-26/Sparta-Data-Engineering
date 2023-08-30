# Control Flow Exercises functions
def print_first_five_numbers(number_list):
    print(number_list[:5])


# List comprehension offers a shorter syntax when you want to create a new list
# based on the values of an existing list.
# new_list = [expression for item in iterable if condition == True]
def print_even_numbers(numbers):
    # create a new list
    # iterate through num in numbers and create new list with even elements
    even_numbers = [num for num in numbers if num % 2 == 0]
    # loop through even numbers list
    for num in even_numbers:
        print(num, end=' ')


def print_even_numbers_up_to_fifth_element(numbers):
    # create new list with first fifth elements if even
    even_numbers_up_to_fifth_element = [num for num in numbers[:5] if num % 2 == 0]
    # for loop through the created list
    for num in even_numbers_up_to_fifth_element:
        print(num, end=' ')


# -------------------------------------------------------------------------------------- #

def get_first_letters(name_list):
    # create new list containing first letters of each name in name list
    # split name and for name in the list, find first word and first letter
    first_letters = [name.split()[0][0] for name in name_list]
    return first_letters


def get_index_of_space(name_list):
    # using your_string.index("substring")
    # index begins at 0
    # name.index finds first space within each name and iterate through each name
    index_of_spaces = [name.index(" ") for name in name_list]
    return index_of_spaces


def get_initials(name_list):
    # initialise an empty list
    initials = []
    # for loop for iterating through each name
    for name in name_list:
        # get initial for firstname by finding the first word and first character
        first_name = name.split()[0][0]
        # get initial for lastname by finding the last word and first character
        last_name = name.split()[-1][0]
        # concatenation
        full_initials = first_name + ' ' + last_name
        # append to full initials list
        initials.append(full_initials)
    return initials


# -------------------------------------------------------------------------------------- #

def print_lists_with_no_duplicates(list_of_lists):
    # for loop iterates over each element in list of lists
    for sub_list in list_of_lists:
        # if sub list length is the same as the length of set
        if len(sub_list) == len(set(sub_list)):
            # only print the sub list elements
            # that contain no duplicates as sets cannot have duplicates
            print(sub_list)


# -------------------------------------------------------------------------------------- #


def is_prime(number):
    # no negatives
    if number <= 1:
        return False
    if number <= 3:
        return True
    # modulo divisible by 2
    if number % 2 == 0:
        return False
    i = 3
    # iterate starting at 3
    while i * i <= number:
        # if divisible by i
        if number % i == 0:
            return False
        # increment by 2 to only test odd numbers
        # skips even numbers
        i += 2
    return True


def get_number_greater_than_one_hundred():
    while True:
        try:
            # store user input as number
            user_number = int(input("Please enter an Number (int) greater than 100: "))
            if user_number > 100:
                return user_number
            else:
                print("Enter a number greater than 100. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
