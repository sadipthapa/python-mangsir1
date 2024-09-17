from abc import ABC, abstractmethod

# Abstract base class
class Vehicle(ABC):
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    @abstractmethod
    def start_engine(self):
        """Method to be implemented by subclasses to start the engine"""
        pass
    
    @abstractmethod
    def stop_engine(self):
        """Method to be implemented by subclasses to stop the engine"""
        pass
    
    def __str__(self):
        return f"{self.brand} {self.model}"

# Subclass implementing the abstract methods
class Car(Vehicle):
    def start_engine(self):
        print(f"Starting the car engine of {self}.")

    def stop_engine(self):
        print(f"Stopping the car engine of {self}.")

# Subclass implementing the abstract methods
class Bike(Vehicle):
    def start_engine(self):
        print(f"Starting the bike engine of {self}.")

    def stop_engine(self):
        print(f"Stopping the bike engine of {self}.")

# Creating instances of Car and Bike
car = Car("Toyota", "Corolla")
bike = Bike("Yamaha", "MT-07")

# Using the methods
print(car)  # Output: Toyota Corolla
car.start_engine()  # Output: Starting the car engine of Toyota Corolla.
car.stop_engine()   # Output: Stopping the car engine of Toyota Corolla.

print(bike)  # Output: Yamaha MT-07
bike.start_engine()  # Output: Starting the bike engine of Yamaha MT-07.
bike.stop_engine()   # Output: Stopping the bike engine of Yamaha MT-07.
