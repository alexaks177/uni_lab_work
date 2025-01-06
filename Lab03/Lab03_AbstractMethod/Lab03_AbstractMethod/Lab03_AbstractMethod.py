# 1
# Abstract
class Button:
    def render(self):
        pass  # Must be realised in children

# Concrete realisation/ Win
class WindowsButton(Button):
    def render(self):
        return "Windows button rendering"  # Render result

# Concrete / Mac
class MacOSButton(Button):
    def render(self):
        return "MacOS button rendering"  # Render result

# Abstract
class Checkbox:
    def render(self):
        pass  # Must be realised in children

# Concrete / Win
class WindowsCheckbox(Checkbox):
    def render(self):
        return "Windows flag rendering"  # Render result

# Concrete / Mac
class MacOSCheckbox(Checkbox):
    def render(self):
        return "MacOS flag rendering"  # Render result

# Abstract
class GUIFactory:
    def create_button(self):
        pass  # Must be realised in children

    # Creation method
    def create_checkbox(self):
        pass

# Concrete / Win
class WindowsFactory(GUIFactory):
    def create_button(self):
        return WindowsButton()  # Creates and returns WindowsButton

    def create_checkbox(self):
        return WindowsCheckbox()  # Creates and returns WindowsCheckbox

# Concrete / Mac
class MacOSFactory(GUIFactory):
    def create_button(self):
        return MacOSButton()  # Creates and returns MacOSButton

    def create_checkbox(self):
        return MacOSCheckbox()  # Creates and returns MacOSCheckbox

# Client code func on factory GUI
def client_code(factory: GUIFactory):
    button = factory.create_button()  # Creates button through factory
    checkbox = factory.create_checkbox()
    
    print(button.render())  # Calls button rendering method and returns result
    print(checkbox.render())

# Win factory example use
client_code(WindowsFactory())  # Returns button rendering for Win and flag rendering

# Mac factory example use
client_code(MacOSFactory())

#2
# Abstract A
class AbstractProductA:
    def useful_function_a(self):
        pass  # Must be realised in children

# Abstract B
class AbstractProductB:
    def useful_function_b(self):
        pass  # Must be realised in children

# Concrete A1
class ConcreteProductA1(AbstractProductA):
    # Useful func for A1 product
    def useful_function_a(self):
        return "Product A1 result"

# Concrete B1
class ConcreteProductB1(AbstractProductB):
    # Useful func for B1 product
    def useful_function_b(self):
        return "Product B1 result"

# Abstract factory creating products A & B
class AbstractFactory:
    def create_product_a(self):
        pass  # Must be realised in children

    def create_product_b(self):
        pass  # Must be realised in children

# Concrete factory realisation
class ConcreteFactory1(AbstractFactory):
    # Product A
    def create_product_a(self):
        return ConcreteProductA1()  # Creates and returns ConcreteProductA1

    # Product B
    def create_product_b(self):
        return ConcreteProductB1()

# Example use case
factory = ConcreteFactory1()  # Creation

# Product A through factory
product_a = factory.create_product_a()  
# Product B
product_b = factory.create_product_b()  

# Useful func A call and return result
print(product_a.useful_function_a())  # returns "Product A1 result"
# Product B
print(product_b.useful_function_b())  # returns "Product B1 result"