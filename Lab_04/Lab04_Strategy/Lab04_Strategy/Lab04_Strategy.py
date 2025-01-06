from abc import ABC, abstractmethod  # Importing ABC and abstractmethod for making abstrack classes

# Defining strategy interface
class Strategy(ABC):
    @abstractmethod  # Decorator for abstract method
    def execute(self, data):  # Abstract method for strategy execution
        pass  # Redefine in children

# Concrete strategy for asc sort
class SortAsc(Strategy):
    def execute(self, data):
        return sorted(data)  # Return asc sorted list

# Concrete strategy for desc sort
class SortDesc(Strategy):
    def execute(self, data):
        return sorted(data, reverse=True)  # Return desc sorted list

# Context that uses the strategy
class Context:
    def __init__(self, strategy: Strategy):  # Init
        self.strategy = strategy  # Saving the strategy

    def set_strategy(self, strategy: Strategy):  # Method for changing the strategy
        self.strategy = strategy  # Saving new strat

    def execute_strategy(self, data):
        return self.strategy.execute(data)

# Example use case
data = [5, 2, 9, 1]  # Input data
context = Context(SortAsc())  # Creating a context with asc sort strategy
print(context.execute_strategy(data))  # Returns [1, 2, 5, 9]

context.set_strategy(SortDesc())  # Changing the strategy to sort desc
print(context.execute_strategy(data))  # Returns [9, 5, 2, 1]
