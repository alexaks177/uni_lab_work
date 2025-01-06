#1
class LogProxy:

    def __init__(self, obj): # Constructor
        self._obj = obj  # Saving _obj (sent var, so _x)


    # Method for obj attributes call interception
    def __getattr__(self, attr):
        print(f"Calling method {attr}")
        return getattr(self._obj, attr) # Returning method from a real obj

# Using LogProxy class
class RealObject:
    def operation(self): # Methog called through proxy
        print("Real operation in progress")

obj = RealObject()
proxy = LogProxy(obj)
proxy.operation()

#2
class ExpensiveCalculator: # Class imitating resource-efficient calculations

    def calculate(self, x):
        # Method for a complex calculation (2nd power)
        print(f"Calculation of a complex operation for {x}...")
        return x * x  # Returning num to a 2nd power


class CachingProxy: # Proxy for caching calculation results

    def __init__(self, calculator): # Constructor
        # Saving link for obj calculator
        self.calculator = calculator
        # Initialising an empty dict for cache
        self.cache = {}

    def calculate(self, x):
        # Checking if result in cache
        if x in self.cache:
            print(f"Returning cached result for {x}")
            return self.cache[x]

        else:
            print(f"No result for {x} In cache. Calculations in proggress...")
            result = self.calculator.calculate(x) # Calling method calculate from a real calculator
            self.cache[x] = result # saving result
            return result


# Example use case

calculator = ExpensiveCalculator()
proxy = CachingProxy(calculator) # Init proxy obj, giving it real calculator

print(proxy.calculate(7))  # Calculations for 7 (result not cached)
print(proxy.calculate(7))  # Using cached result for 7 (result taken from cache)
print(proxy.calculate(12))  # Calculations for 12 (result not cached)
print(proxy.calculate(12))  # Using cached result for 12 (result taken from cache)
