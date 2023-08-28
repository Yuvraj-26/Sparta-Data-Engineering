'''
Polymorphism
Refers to the ability of different classes to be treated as instances of a common superclass
A number of different classes all capable of dealing with the same message
or operation being called on them, but classes know how to perform the action for their own particular case 
where the underlying implementation is unknown due to encapsulation

Different classes that can all respond to the same message or operation
Even though each class knows how to perform the action specific to its purpose
(due to encapsulation), you can simply tell a class to do a job, and it will know how to execute it
This concept enhances code reusability and adaptability
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
