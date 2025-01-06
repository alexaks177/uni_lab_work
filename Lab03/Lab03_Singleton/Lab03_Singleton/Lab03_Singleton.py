class Singleton:
    _instance = None  # Stores single class unit

    def __new__(cls):
        if cls._instance is None:  # Checking if unit exists
            cls._instance = super(Singleton, cls).__new__(cls)  # Creating new unit
        return cls._instance  # Returning single unit

# Example use case
singleton1 = Singleton()
singleton2 = Singleton()

print(singleton1 is singleton2)  # Returns true, both objects are the same unit
