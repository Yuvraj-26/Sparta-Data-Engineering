# OOP encapsulation example 1
class Animals:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name


animal1 = Animals("Bob")
animal1.__name = "Jess"

print(animal1.__name)  # outputs Jess
print(animal1.get_name())  # outputs Bob
print("\n")

'''
Line 11 animal1.__name = "Jess"
creates a new instance variable called __name that is specific to the object animal 1,
it does not change the value of the actual name of the animal (Animal_name)
The name of animal1 stays as 'Bob' and doesnt change.
Line 11 does not successfully access the encapsulated data.

Line 13  animal1.__name = "Jess" accesses a new instance variable called __name,
but does not modify the actual attribute encapsulated by the class.

Line 14 calls the get_name() method of the animal1 object, which is a getter that 
gets the value of the private attributed __name.
print(animal1.get_name()) prints the actual value of __name of the object animal 1,
as initialise during object creation which is Bob.

'''  # OOP encapsulation example 2


class Animal:
    def speak(self):
        print("Animal speaks")


class Cat(Animal):
    def speak(self):
        print("Cat meows")


class Dog(Animal):
    def speak(self):
        print("Woof")


fudge = Cat()
pepper = Dog()

animal_list = [fudge, pepper]

for animal in animal_list:
    animal.speak()

'''
Encapsulation: Each class Animal, Cat, and Dog encapsulates its own behaviour encapsulation means bundling the 
data (attributes) and methods (functions) that operate on the data into a single unit (the class). 
speak method is  encapsulated within each class to define their specific behaviors. 

Inheritance: Cat and Dog classes inherit from the Animal class (is as relationship) 

Polymorphism: both Cat and Dog are treated as Animal objects. When you call speak on these objects, 
the method behaves differently based on the actual object type. This is known as method overriding, 
where child classes provide their own implementation of a method with the same name as the one in the parent class.

We can call speak() on any objects in this list without worrying about the specific type of animal.
The correct speak method for the actual object is called automatically
demonstrating the power of encapsulation.


'''
