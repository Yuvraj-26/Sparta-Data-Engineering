import requests
import json

# Python code interacts with the https://postcodes.io/ API

# POST: To submit data to be processed to the server
# specify the Content-Type header we are passing through
headers = {'Content-Type': 'application/json'}


# json.dumps converts a Python object (dict) into a JSON-formatted string
# we prepare a JSON-formatted string using json.dumps().
# the JSON data includes a postcodes key with a list of postal codes.
json_data = json.dumps({'postcodes': ["PR3 0SG", "M45 6GN", "EX165BL"]})

# a json object is expected as argument, cannot pass through a python dictionary
# as a test, try without json.dumps() function
# the following line of code produces an error as expected
# json_data = ({'postcodes': ["PR3 0SG", "M45 6GN", "EX165BL"]})

# Traceback (most recent call last): File "/home/riggy/PycharmProjects/pythonProjectjson/main.py", line 75,
# in <module> print(post_codes_req.json()['result'][0]['result']['country']) ~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^
# KeyError: 'result' {'status': 400, 'error': 'Invalid JSON submitted.\nYou need to submit a JSON object with an
# array of postcodes or geolocation objects.\nAlso ensure that Content-Type is set to application/json\n'} <class
# 'dict'>

# sends a HTTP POST request to the specified URL; sets the HTTP headers, and json_data
# specifies a JSON formatted string to be sent in the request body
# this is the JSON object with a postcodes key and list of post codes
post_codes_req = requests.post("https://api.postcodes.io/postcodes/", headers=headers, data=json_data)


# print request
print(post_codes_req)

print("\n")
# returns list
print(post_codes_req.json())

print("\n")
# outputs list of different queries
# where each postcode has its own dictionary
# stored within the list of the result
print(type(post_codes_req.json()))

print("\n")
# to access specific data within the parsed JSON response use indexing
# as the JSON response contains nested structures

# post_codes_req.json()['result'] is expected to be a list, and [0] accesses the first item in that list
# ['result'] again accesses the "result" key within the first item, which is another dictionary
# ['result']['country'] accesses the "country" key within that nested dictionary
print(post_codes_req.json()['result'][0]['result']['country'])