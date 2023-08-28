import person


# create a new class Employee which is a subclass of person.Person
# add additional features into the subclasses
class Employee(person.Person):
    # constructor for employee to which adds parameter department
    def __init__(self, fname, lname, department):
        self._department = department
        # superclass constructor
        super().__init__(fname, lname)

    def print(self):
        print(f'Department: {self._department} ', end='')
        super().print()
