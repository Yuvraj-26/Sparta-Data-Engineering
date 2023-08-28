'''
Encapsulation
Hides data and implementation details
Provides a simple, consistent interface to use the object

Encapsulation is about controlling access to the internal components of a class
Each class has a well-defined responsibility
_ convention is that if a feature of a class has underscore at start, it's a private feature
aimed at restricting direct access to certain attributes or methods of a class
It helps in controlling the visibility and accessibility of the internal workings of an object
'''


# Customer class
class Customer:
    # constructor method to create a new instance of the class
    def __init__(self, fname, lname): # initialise variables
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

    # add logic into set method to specify conditions to allow or prevent changes
    @first_name.setter
    def first_name(self, new_first_name):
        print('In set method')
        self._first_name = new_first_name
