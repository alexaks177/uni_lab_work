class Car:
    # Initialization
    def __init__(self):  # __X__ for syntax clarity
        self.parts = []  # List for storing car parts

    # Method for adding car parts
    def add_part(self, part: str):
        self.parts.append(part)  # Adding to list

    # All parts display method
    def show_parts(self):
        return f"The car is made of: {', '.join(self.parts)}"

# Class for making a car
class CarBuilder:
    # Initialization
    def __init__(self):
        self.car = Car()  # Making a new car model

    # Engine
    def build_engine(self):
        self.car.add_part("Engine")  # Adding an "Engine" part to the car

    # Wheels
    def build_wheels(self):
        self.car.add_part("Wheels")

    # Car body
    def build_body(self):
        self.car.add_part("Body")

    # Displaying final car model
    def get_car(self) -> Car:
        return self.car

# CarBuilder example use case
def client_code():
    builder = CarBuilder()  # Creating a builder

    builder.build_engine()  # Adding an engine
    builder.build_wheels()  # Wheels
    builder.build_body()    # Car body
    
    car = builder.get_car()  # Initialising a var w/ given values
    print(car.show_parts())  # Returns "The car is made of: Engine, Wheels, Body"

client_code()  # client_code func call
