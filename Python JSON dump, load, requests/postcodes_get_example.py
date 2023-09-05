import requests
import json

'''
Summary: 
json.dumps(): Serialize (convert) a Python object into a JSON-formatted string.

json.dump(): Serialize (convert) a Python object and write it to a JSON-formatted file.

json.loads(): Deserializes (parses) a JSON-formatted string into a Python object. 
It takes a JSON string as its argument and converts it into a Python data structure (e.g., a dictionary).

json.load: Deserializes (parses) a JSON-formatted file into a Python object. 
It takes a file object that has already been opened in read mode as its argument 
and converts the JSON data from the file into a Python data structure.

'''
# Python code interacts with the https://postcodes.io/ API

# GET: To request data from the server
# sends a HTTP GET request to the specified URL, which is the API end-point for postcode 'SE120NB'
# response from the API is stored in the variable
post_codes_req = requests.get("https://api.postcodes.io/postcodes/se120nb")

# print the HTTP response object from the API
print(post_codes_req)

print("\n")
# Print HTTP status code
print(post_codes_req.status_code)

print("\n")
# prints HTTP response headers
print(post_codes_req.headers)

print("\n")
# prints the content of the HTTP response as bytes (b represents bytes)
print(post_codes_req.content)

print("\n")
# takes the JSON content of the API response, parses it into a Python object, and then prints the Python object
print(post_codes_req.json())

print("\n")
# Print the type of the parsed JSON data (outputs Python dict)
print(type(post_codes_req.json()))
# access postcode key through result as result value is another dictionary

print("\n-----------------------------------------------------------------------------------------------------\n")
