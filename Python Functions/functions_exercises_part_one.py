# Functions Exercises Part 1

print("\nQ1a and Q1b\n")


# Q1a: Write a function which takes in an integer as an argument
# and returns the divisors of that number as a list
# e.g. f(12) = [1, 2, 3, 4, 6, 12]
# hint: range(1, n) returns a collection of the numbers from 1 to n-1
def find_divisors(num):
    # initialise an empty list to store divisors
    divisor_list = []
    # iterates through numbers from 1 to num including num
    for i in range(1, num + 1):
        # if num is divisible by i
        if num % i == 0:
            # append i to divisors list if true
            divisor_list.append(i)
    return divisor_list


'''
# test function
input_number = int(input("Enter an integer: "))
new_divisors = find_divisors(input_number)
print("Divisors:", new_divisors)
'''


def find_common_divisor(user_num1, user_num2):
    # use find_divisors function to find divisors of first number
    divisors_of_num1 = find_divisors(user_num1)
    # use find_divisors function to find divisors of second number
    divisors_of_num2 = find_divisors(user_num2)

    for divisor in divisors_of_num1:
        # divisor is not 1 as we want to find divisors other than 1
        # and divisor cannot be in divisor of num2 list
        if divisor != 1 and divisor in divisors_of_num2:
            return True

    # no common divisors
    return False


# test function
# Examples: 10,100 returns true, 7, 23 returns false, 0, 7 returns false
# 1, 2 returns false, as 1 is excluded as common divisor
input_num1 = int(input("Enter first number: "))
input_num2 = int(input("Enter second number: "))

common_divisor_exists = find_common_divisor(input_num1, input_num2)
print(common_divisor_exists)
