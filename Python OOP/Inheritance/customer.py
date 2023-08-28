'''
Inheritance
A fundamental concept in OOP that allows a new class (subclass or derived class) to inherit properties and behaviours (attributes and methods)
from an existing class (superclass or base class)
This promotes code reuse and hierarchical organisation of classes
The subclass can extend, modify, or override the attributes and methods
inherited from the superclass

'''

import person


# Customer class to be a subclass of Person class
# Specify superclass of person.Person  |
# person specifies name of the module, and Person is the name of the class
class Customer(person.Person):
    # define a new constructor for customer with address parameter
    def __init__(self, fname, lname, address):
        # assign a value to instance variable address
        self._address = address
        # call constructor in the superclass which does initialisation of first and last name
        super().__init__(fname, lname)

    # replace implementation for print function also
    def print(self):
        print(f'Address: {self._address} ', end='')
        super().print()


    '''
    # constructor method to create a new instance of the class
    def __init__(self, fname, lname):  # initialise variables
        # as variables are applicable to any person, move into Person class
        # Refactor, pull members up, select features to put into Person superclass
        # Refactor init, print(self), self_last_name, self_first_name
        self._first_name = fname
        self._last_name = lname

    def print(self):
        print(f'Full name: {self._first_name} {self._last_name}')

    # use a decorator
    # Allows us to provide information about classes and their intended use
    @property
    def first_name(self):
        print('In get method')
        return self._firstName

    # can add logic into set method to specify conditions to allow or prevent changes
    @first_name.setter
    def first_name(self, new_first_name):
        print('In set method')
        self._first_name = new_first_name
    '''
