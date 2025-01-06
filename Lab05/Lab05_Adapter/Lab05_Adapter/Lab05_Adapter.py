

#1
class JsonData: # Class for working with Json
    def get_data(self):
        return '{"name": "John", "age": 15}' # Returnt Json string


class XmlData: # Class for working with Xml
    def get_data(self):
        return "<person><name>John</name><age>15</age></person>" # Returns Xml string


class DataAdapter: # Class for working with Single format data
    def __init__(self, data_provider):
        self.data_provider = data_provider # Saving data provider as an attribute

    def get_data(self): # Method for getting adapted data
        raw_data = self.data_provider.get_data()  # Getting non-processed data from provider
        print("Data adaptation...")
        # Reforming data into asingle format (i.e. Python dictionary)
        if raw_data.startswith('{'):  # If starts with '{' -> Json
            import json # Importing json for working w/ this data type
            return json.loads(raw_data)  # Json string into Python dict, then return
        elif raw_data.startswith('<'):  # If starts with '<' -> Xml
            import xml.etree.ElementTree as ET  # Importing xml for working w/ this data type
            tree = ET.ElementTree(ET.fromstring(raw_data)) # Parsing Xml string into a tree of elements
            root = tree.getroot()   # Getting root element
            return {child.tag: child.text for child in root}  # Making a dict from tags and their strings


# Example use case
json_provider = JsonData()
xml_provider = XmlData()

json_adapter = DataAdapter(json_provider)
xml_adapter = DataAdapter(xml_provider)

print(json_adapter.get_data())
print(xml_adapter.get_data())


#2
class OldSystem: # Old system interface
    def specific_request(self):
        return "Old system response"


class NewSystem: # New system interface
    def request(self):
        return "New system response"


class Adapter: # Adapter for old and new system compatibility
    def __init__(self, old_system: OldSystem): # var: class -> class variable outside of __init__
        self.old_system = old_system  # Saving old system

    def request(self):  # Changing interface into a new model
        return self.old_system.specific_request()


# Example use case
old_system = OldSystem()
adapter = Adapter(old_system)  # Defining adapter for old system

print(adapter.request())  # Calling adapter method that is using a new system
# Returns "Old system response"
