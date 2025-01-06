from collections.abc import Iterable, Iterator  # Importing Iterable and Iterator interfaces

# Collection class
class Collection(Iterable):
    def __init__(self):
        self.items = []  # Init empty list for data storage

    def add_item(self, item):  # Method for adding item to a collection
        self.items.append(item)

    def __iter__(self):  # Method for getting an iterator, returns items
        return Iterator(self.items)

# Iterator class
class Iterator(Iterator):
    def __init__(self, items):
        self._items = items  # Saving collection elements
        self._index = 0  # Index for iteration

    def __next__(self):  # Method for getting the next element
        if self._index < len(self._items):  # Checking if there are more elements
            result = self._items[self._index]  # Getting current element
            self._index += 1
            return result
        raise StopIteration()  # Call StopIteration if no more elements

# Example use case
collection = Collection()  # Creating a collection unit
collection.add_item("Element 1")  # Adding elements
collection.add_item("Element 2")
collection.add_item("Element 3")

for item in collection:  # Cycle for iteration through collection
    print(item)  # Returning each element