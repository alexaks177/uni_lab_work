from abc import ABC, abstractmethod  # Importing ABC and abstractmethod for creating abstract classes

# Handler abstract class
class Handler(ABC):
    def set_next(self, handler):  # Method for defining next handler
        self.next_handler = handler  # Defining
        return handler  # Returning

    @abstractmethod  # Decorator for an abstract method
    def handle(self, request):  # Abstract method for handling a request
        if hasattr(self, 'next_handler'):  # Checking for next handler
            return self.next_handler.handle(request)  # Requesting next handler
        return None  # Return None if no next handler

# Concrete handler for "Technical" type requests
class TechnicalHandler(Handler):
    def handle(self, request):  # HAndle method realisation
        if request == "Technical":  # Checking for request type
            return "Handled by a technical dept"  # Returning processing result
        else:
            return super().handle(request)  # Requesting next handler

# Concrete handler for "Finantial" type requests
class FinancialHandler(Handler):
    def handle(self, request):
        if request == "Finantial":
            return "Handled by a finantial dept"
        else:
            return super().handle(request)

# Example use case
technical_handler = TechnicalHandler()  # Creating technical handler
financial_handler = FinancialHandler()  # Creating finantial handler
technical_handler.set_next(financial_handler)  # Defining a chain of responsibilities: tech -> finance

print(technical_handler.handle("Technical"))  # Returns "Handled by a technical dept"
print(technical_handler.handle("Finantial"))   # Returns "Handled by a finantial dept"
print(technical_handler.handle("Marketing"))  # Returns "None" (request was not handled)
