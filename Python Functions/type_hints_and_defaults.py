'''
Typehints and Defaults

Typehints
Show argument and what is returned
 Annotations indicating expected data types for variables, function parameters, and return values
 Type hints help improve code readability,
 catch type-related errors early, and enable better code analysis.
'''

from typing import List


# Typehint example
def divisor(number: int) -> list:
    divisors_list = []
    for i in range(1, number + 1):
        if number % i == 0:
            divisors_list.append(i)
    print(divisors_list)


print(divisor(100))


# Typehint example

def divisor(number: int) -> List[int]:
    divisors_list: List[int] = []
    for i in range(1, number + 1):
        if number % i == 0:
            divisors_list.append(i)
    return divisors_list


'''
Defaults
Default arguments are a feature in Python that allow you to assign default values to function parameters.
 If a value for a parameter is not provided when the function is called, the default value is used instead.

'''


# Defaults example
# argument is required / mandatory but default value to parameter is 20
# useful for default connection information for databases and reading or writing to default files
def divisor_new(number=77) -> list:
    divisors_list = []
    for i in range(1, number + 1):
        if number % i == 0:
            divisors_list.append(i)
    return divisors_list


result = divisor_new()
print(result)


# Combining typehints and defaults
def divisor_both(number2: int, number: int = 99) -> list:
    divisors_list = []
    for i in range(1, number + 1):
        if number % i == 0:
            divisors_list.append(i)
    return divisors_list


result = divisor_both(10)  # Provide a value for number2
print(result)
