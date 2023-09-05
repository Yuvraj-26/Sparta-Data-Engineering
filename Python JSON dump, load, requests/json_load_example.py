import json

'''
If you want to go from a JSON-formatted string back to a Python object, you would use the json.loads() function, 
where "loads" stands for deserialize. Deserialization is the process of reconstructing a data structure or object 
from a serialized format (in this case, from a JSON string to a Python object).
'''

# create a python dictionary with two key-value paris
course = {"name": "Data 249", "trainer": "Paula"}

# opens a previously created in default read mode
with open("new_json_data.json") as jsonfile:
    # use the json.load() function to read and parse the JSON data from the file
    # deserializes a JSON-formatted string document into a Python object (specifically a Python  dictionary)
    course_file = json.load(jsonfile)
    # print the contents of the course_file dict
    print(course_file)
    # outputs dict type
    print(type(course_file))
    # access and print the name key
    print(course_file['name'])



