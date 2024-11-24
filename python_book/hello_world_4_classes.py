# The dog class
class Dog:
    """A simple attempt to model a dog"""

    def __init__(self, name, age):
        """Initialise name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command"""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate a dog rolling over in response to a command"""
        print(f"{self.name} rolled over!")


my_dog = Dog("Aren", 6)
print(f"My dog's name is {my_dog.name}")
print(f"{my_dog.name}'s age is {my_dog.age} years")
my_dog.sit()
my_dog.roll_over()


# The car class
class Car:
    """A simple attempt to represent a car"""

    def __init__(self, make, model, year):
        """Initialsie attributes to describe a car"""
        self.make = make
        self.model = model
        self. year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name"""
        long_name = f"{self.make} {self.model} {self.year}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it!")

    def update_odometer(self, mileage):
        """
        Set odometer reading to the given value.
        Rejects the change if it attempts to roll odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back odometer!!!")

    def increment_odometer(self, miles):
        if miles >= 0:
            self.odometer_reading += miles
        else:
            print("You cannot roll back odometer!!!")


my_new_car = Car("bmw", "a6", 2024)
print(my_new_car.get_descriptive_name())

my_new_car.update_odometer(15_000)  # Modifying the attribute "odometer_reading"
my_new_car.read_odometer()
my_new_car.increment_odometer(102)
my_new_car.read_odometer()


class Battery:
    """A simple attempt to model a battery for an electric car"""
    def __init__(self, battery_size=40):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car got a {self.battery_size}-kWh")

    def get_range(self):
        """Print a statement about the range this battery provides"""
        if self.battery_size == 40:
            range = 150
        elif self.battery == 60:
            range = 250

        print(f"This car can go {range} miles on a full battery.")

class ElectricCar(Car):
    """Represents aspects of a car, specific to electric vehicles"""

    def __init__(self, make, model, year):
        """Initialise attributes of the parent class.
        Then initialise attributes specific to the child class.
        """
        super().__init__(make, model, year)
        self.battery = Battery()



my_tesla = ElectricCar("tesla", "roadster", 2024)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()