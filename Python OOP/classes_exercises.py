# Classes Exercises

print("\nQ1a\n")


# Q1a: Create a class which of a country (include continent, climate, language etc. in the inputs)

# A1a:
class Country:
    def __init__(self, name, continent, climate, language):
        self.name = name
        self.continent = continent
        self.climate = climate
        self.language = language

    def print(self):
        print("Country:", self.name)
        print("Continent:", self.continent)
        print("Climate:", self.climate)
        print("Language:", self.language)


# Create an instance of the Country class
country = Country("United Kingdom", "Europe", "Rain", "English")

country.print()

print("\nQ1b\n")


# Q1b: Create a subclass of a city which inherits from the country class

# A1b:
# By inheriting from the Country class, the City class can reuse the common country attributes and methods,
# and it can extend by providing its own implementations for specific city attributes and methods.
class City(Country):
    def __init__(self, name, continent, climate, language, city_name, population, economy, landmark):
        super().__init__(name, continent, climate, language)
        self.city_name = city_name
        self.population = population
        self.economy = economy
        self.landmark = landmark

    def print(self):
        super().print()
        print("City:", self.city_name)
        print("Population:", self.population)
        print("Economy:", self.economy)
        print("Landmark:", self.landmark)


# Example
city = City("France", "Europe", "Chilly", "French", "Paris",
            21012345, 500000000, "Eiffel Tower")

city.print()

# -------------------------------------------------------------------------------------- #

print("\nQ2a\n")
# Q2a: Using the predefined class and is_prime method below, loop through list_of_numbers and create
# a list of primes from that list
list_of_numbers = [1, 12, 44, 53, 6, 3, 6545, 76, 32, 345, 22, 17, 19, 223, 156]


class Number:
    def __init__(self, integer):
        self.integer = integer

    def is_prime(self):
        if self.integer >= 2:
            for x in range(2, self.integer):
                if self.integer % x == 0:
                    return False
            return True
        else:
            return False

    def divisible_by_n(self, n):
        if self.integer % n == 0:
            return True
        else:
            return False


# A2a:
# Create an empty list for new list of prime numbers
new_prime_numbers = []
# iterate through each num
for num in list_of_numbers:
    # create instance and call is_prime function
    if Number(num).is_prime():
        # append prime numbers to new list
        new_prime_numbers.append(num)

# sort the list
new_prime_numbers.sort()

print(new_prime_numbers)

print("\nQ2b\n")
# Q2b: Now create a list of numbers from list_of_numbers that are divisible
# by both 3 and 4 using the divisible_by_n method above

# A2b:
# Create an empty list for new list of prime numbers
divisible_by_three_and_four = []
# iterate through each num
for num in list_of_numbers:
    # create a variable to store current number
    current_number = Number(num)
    if current_number.divisible_by_n(3) and current_number.divisible_by_n(4):
        # append prime numbers to new list
        divisible_by_three_and_four.append(num)

# sort the list
divisible_by_three_and_four.sort()

print(divisible_by_three_and_four)

# -------------------------------------------------------------------------------------- #

print("\nQ3a\n")


# Q3a: Fix the following class and subclass (uncomment by selecting all rows and pressing CTRL + /)


# class Boss(object):
#     def __init__(self, name, attitude, behaviour, face):
#         name = name
#         attitude = attitude
#         behaviour = behaviour
#         face = face
#
#     def get_attitude(self):
#         return attitude
#
#     def get_behaviour(self):
#         return behaviour
#
#     def get_face(self):
#         return face
#
#
# class GoodBoss(Boss):
#     def __init__(self, name, attitude, behaviour, face):
#         super()
#
#    def encourage(self):
#        print(f"The team cheers for {self.name}, starts shouting awesome slogans then gets back to work.")


# A3a:
class Boss(object):
    def __init__(self, name, attitude, behaviour, face):
        # initialise instance variables using self
        self.name = name
        self.attitude = attitude
        self.behaviour = behaviour
        self.face = face

    def get_attitude(self):
        return self.attitude

    def get_behaviour(self):
        return self.behaviour

    def get_face(self):
        return self.face


# subclass GoodBoss
class GoodBoss(Boss):
    def __init__(self, name, attitude, behaviour, face):
        # superclass constructor needed to initialise common attributes
        # as GoodBoss inherits from superclass
        super().__init__(name, attitude, behaviour, face)

    def encourage(self):
        print(f"The team cheers for {self.name}, starts shouting awesome slogans, and then gets back to work.")


# Create an instance of the GoodBoss class
good_boss_example = GoodBoss("Pep", "Relentless", "Decisive", "Happy")

good_boss_example.encourage()

# Example
print(
    f"{good_boss_example.name} is {good_boss_example.attitude}, {good_boss_example.behaviour}"
    f", and {good_boss_example.face}")

# -------------------------------------------------------------------------------------- #
