import random

import customer
import employee
import random

# Runtime example
# if random int is 0
if random.randint(0,1) == 0:
    # assign customer object to my_person
    my_person = customer.Customer('Manny', 'Lee', 'London')  # enter names as parameters to the constructor
else:
    # assign employee object to my_person
    my_person = employee.Employee('Kendall', 'Joshua', 'Finance')
# program automatically calls the correct print function at the point of program execution
# shows that sending message to the object, the object knows what to do which is Polymorphism
my_person.print()

'''
# Polymorphism
sent a print message to the customer object which called the customer version of the print function
sent a print message to the employee object which called the employee version of the print function
In Python, program looks for most specific version of the function available:
looks for print function on employee object/customer object, if not found, checks superclass
continues up the inheritance hierarchy until found or will throw an error
'''
