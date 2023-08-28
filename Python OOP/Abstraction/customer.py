'''
Abstraction
Involves hiding complex implementation details of how an object works,
exposing only the relevant and essential features
Focus on what an object does rather than how it does it
This reduces complexity and enhances reusability

- An object is an instance of a class
- A class is a type of object
'''


# Customer class
class Customer:
    # constructor method to create a new instance of the class
    def __init__(self, fname, lname): # initialise variables
        self.firstName = fname
        self.lastName = lname

    def print(self):
        print(f'Full name: {self.firstName} {self.lastName}')
