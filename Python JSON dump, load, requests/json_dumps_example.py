import json

'''
The json.dumps() function in Python is used to serialize Python objects into a JSON-formatted string. 
Serialization refers to the process of converting a data structure or object into a format that can be easily stored, 
transmitted, or later reconstructed. In the case of json.dumps(), it takes a Python object (e.g., a dictionary) and 
converts it into a JSON string.
'''

# create a python dictionary with two key-value pairs
course = {"name": "Data 249", "trainer": "Paula"}

# outputs dict data type
print(type(course))

# outputs content of the course dictionary
print(course)

# use the json.dumps() function to convert the Python dictionary course into a JSON-formatted string
course_json_str = json.dumps(course)

# outputs string data type
print(type(course_json_str))
print(course_json_str)

'''
The json.dump() function in Python is used to serialize (convert to JSON format) and write a Python object 
directly to a file. It combines both serialization and writing to a file in a single step.
- Serialize: json.dump() serializes a Python object (e.g., a dictionary) into a JSON-formatted string, 
just like json.dumps(). 
- Write to a File: After serialization, json.dump() writes the resulting JSON string to a specified file.
'''
# opens a new file in write mode
with open("new_json_data.json", "w") as jsonfile:
    # use the json.dump() function to write the contents of the course dict to the new file in JSON format
    # where arguments are python dictionary to turn into JSON formatted file, and file type object
    json.dump(course, jsonfile)
