class Product:
    def operation(self):
        return "Product operation result"

# Base class for product creators
class Creator:
    # Factory method, must be defined in children
    def factory_method(self):
        raise NotImplementedError("You have to redefine this method")  # Raises error if method is not redefined

# Concrete realisation of Creator, inherits Creator class
class ConcreteCreator(Creator):
    # Product creation method
    def factory_method(self):
        return Product()

# Defined creator use case
creator = ConcreteCreator() # Using just creator = Creator() raises NotImplementedError
product = creator.factory_method()  # Factory method for getting product
print(product.operation())  # Calling operation method, returns "Product operation result"
