# Functions Exercises Part 3

print("\nQ3a and Q3b\n")


# Q3a: Write a function which takes an integer as an input,
# and returns true if the number is prime, false otherwise.
# Q3b: Now add some functionality to the function
# which does not error if the user inputs something other than a digit

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


while True:
    # get user input
    user_input = input("Enter an integer (or type 'quit' to exit): ")

    if user_input.lower() == 'quit':
        break

    try:
        # convert user number into int and assign to input
        user_number = int(user_input)
        # call to function is_prime
        user_number_is_prime = is_prime(user_number)
        if user_number_is_prime:
            print(f"{user_number} IS Prime.")
        else:
            print(f"{user_number} IS NOT Prime.")
    except ValueError:
        print("Invalid input. Please enter a valid Integer.")
