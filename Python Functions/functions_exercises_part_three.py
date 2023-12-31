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
    user_input = input("Enter an integer (greater than 100) or type 'quit' to exit: ")

    if user_input.lower() == 'quit':
        break

    try:
        # convert user number into int and assign to input
        user_number = int(user_input)

        if user_number > 100:
            # call to function is_prime
            user_number_is_prime = is_prime(user_number)
            if user_number_is_prime:
                print(f"{user_number} IS Prime.")
            else:
                print(f"{user_number} IS NOT Prime.")
        else:
            print("Number should be greater than 100. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a valid Integer.")

'''
user_prompt = True
while user_prompt:
    number = input("Please type in a number that is greater than 100... ")
    if number.isdigit():
        if int(number) >= 100:
            user_prompt = False
print(number)
# if within an if as if the number is not a digit, them it cannot be converted to an integer

user_prompt = True
while user_prompt:
    number = input("Please type in a number that is greater than 100... ")
    if number.isdigit():
        if int(number) >= 100:
            user_prompt = False
prime = True
for i in range(2, int(number)):
    if int(number) % i == 0:
        prime = False
if prime:
    print("prime")
else:
    print("not prime")
'''
