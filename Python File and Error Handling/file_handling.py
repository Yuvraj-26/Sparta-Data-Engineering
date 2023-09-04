"""
File Handling

Python and Pandas are often used together for file handling, but there are situations where we might choose to use
Python's built-in file handling capabilities instead of Pandas
For example:
- Simple File operations: reading and writing from or to a file without complex data manipulation is more
efficient when using Python built in libraries. Use open() for read and write without the overhead of loading
data into Pandas Data Frames
- Large file handling - working with very large files with high resource/memory demands,
as we do not want to load large files into AWS causing increased storage and usage costs

Deciding whether to use csv or json:
- Data format: csv for tabular data with comma-separated values,
                json for configuration files, API responses, semi structured data
- Data complexity: json better for representing hierarchical and nested data structures
- Ease of use: csv for operations like reading and writing rows of data
- Performance - pandas requires to be installed, data exploration is preferred in pandas whereas
                basic transformations on large datasets where multiple transformations are required,
                Python file handling is more efficient
                - memory: pandas loads the dataset into memory as a DataFrame which is memory-intensive
                - overhead: pandas involves the overhead of creating and searching through Dataframe meaning
                            slower operations, whereas iterating over rows in the CSV file directly
                - Depends on size of dataset, complexity of transformations, available memory resources

"""
import csv

# try:
#     file = open("order.txt")
# except FileNotFoundError as msg:
#     print("File not found error!")
#     print(msg)
#     raise # raises error in terminal
# except SyntaxError:
#     print("Syntax error!")

'''
File errors in Python
- FileNotFoundError - file doesnt exist in specified location
- PermissionError - file access permissions or writing to a read-only file or protected directory
- IsADirectoryError - opening a directory path instead of file
- UnsupportedOperation - unsupported operation on file such as reading from a file opened in w mode
- UnicodeDecodeError - using wrong encoding or invalid characters during decoding
- FileAlreadyExistsError - creating a file with same name without specifying correct mode or overwriting
'''

# Opens order.txt and iterates through each word, printing the word
try:
    # open file in read mode
    file = open("order.txt", "r")
    file_line_list = file.readlines()
    for line in file_line_list:
        line = line.split(',')
        for word in line:
            print(word.strip())
    file.close()
except FileNotFoundError as msg:
    print("File not found")

'''
Raising Fatal error
- includes CustomException, ValueError, TypeError, IndexError, AssertionError, KeyError (dictionary)

Common problems of using open()
- File overwriting - careful when overwriting contents or appending to existing data
- Truncating - truncating the file may remove existing data
- Closing file - must close the file after use using close()

'''

'''
Modes 
'r' default mode, opens file for reading
'w' writing mode, creates file if it does not exist, if file exists, it truncates the file
'x' creates a new file, if file exists already, operation fails
'a' open file in append mode, if file does not exist, creates new file
't' default mode, opens in text mode
'b' binary mode
'+' open a file for reading and writing (updating)

USEFUL FOR JSON

'''

# Prints list type as expected
try:
    file = open("order.txt", "r")
    file_line_list = file.readlines()
    print(type(file_line_list))
    file.close()
except FileNotFoundError as msg:
    print("Error occurred!")

# With open
with open("user_details.csv", newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # print(csvreader)
    # for row in csvreader:
    # print(row)  # indexing
    # print(row[0]) # indexing

    # iterable skips first row which is header row
    # iterable_csv = iter(csvreader)
    # next(iterable_csv)
    # for row in iterable_csv:
    #     print(row)
    # cast to a list (best practise is to create a new variable)

    # print list of lists using csvreader
    print(list(csvreader)[0][1])  # indexing

# with open
with open("user_details.csv", newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    print(list(csvreader)[3][1])  # indexing

# Example

import csv


# Function to transform user_details csv file
def transform_user_details(csv_file_name):
    # create empty list for new list of lists
    new_user_data = []
    with open(csv_file_name, newline='') as csvfile:
        user_details_csv = csv.reader(csvfile, delimiter=",")

        for user in user_details_csv:
            # initialise empty list
            transformation = []
            transformation.append(user[1])  # first name
            # transformation.append(change_name(user[1]))  # create and call change_name function
            transformation.append(user[2])  # last name
            transformation.append(user[-1])  # email
            new_user_data.append(transformation)

    return new_user_data


print(transform_user_details("user_details.csv"))


# Function to write to new file
def create_new_user_details(old_fle_name="user_details.csv", new_file_name="new_user_details.csv"):
    new_user_date = transform_user_details(old_fle_name)
    # write to file
    with open(new_file_name, "w", newline='') as new_file:
        csv_writer = csv.writer(new_file)
        # csv.write row - single row at a time or rows - multiple rows
        # as we have list of list use rows
        csv_writer.writerows(new_user_date)


create_new_user_details()
