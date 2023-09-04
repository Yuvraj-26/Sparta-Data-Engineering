'''
IMDB Data Transformation

Transform the imdbtitles csv file using the following criteria:
    - only films from 2010 onwards selected
    - movies should be the only type of title
    - Only primary title used
    - Remove the end data and isadult fields

'''

# import csv
#
# Function to transform IMDb data
# def transform_imdb_data(old_file_name="imdbtitles.csv", new_file_name="new_version_of_imdbtitles.csv"):
#     # create list of lists
#     new_movie_list = []
#
#     # open the original file
#     with open(old_file_name, newline='') as csvfile:
#         # csv reader object
#         movie_csv = csv.reader(csvfile, delimiter=",")
#
#         for movie in movie_csv:
#             # first column has to be movie and fifth column is greater than 2010
#             if movie[0] == 'movie' and int(movie[4]) >= 2010:
#                 # append
#                 new_movie_list.append([movie[0], movie[1], movie[4], movie[6], movie[7]])
#
#     # open new file
#     with open(new_file_name, "w", newline='') as new_csv_file:
#         csv_writer = csv.writer(new_csv_file)
#         csv_writer.writerows(new_movie_list)
#
#
# transform_imdb_data()

# --------------------------------------------------------------------------------------------

# import csv
#
# # Improved transformation of IMDb data using functions
# def transform_imdb_data(old_file_name="imdbtitles.csv"):
#     # create a list of lists to store the transformed data
#     new_movie_list = []
#
#     # open the original file
#     with open(old_file_name, newline='') as csvfile:
#         # create a CSV reader object
#         movie_csv = csv.reader(csvfile, delimiter=",")
#
#         for movie in movie_csv:
#             # filter if the titleType column is 'movie' and the startYear column is greater than or equal to 2010
#             if movie[0] == 'movie' and int(movie[4]) >= 2010:
#                 # append the selected columns to the new_movie_list
#                 new_movie_list.append([movie[0], movie[1], movie[4], movie[6], movie[7]])
#
#     return new_movie_list
#
#
# # Function to create a new IMDb CSV file
# def create_new_imdb_file(old_file_name="imdbtitles.csv", new_file_name="new_version_of_imdbtitles.csv"):
#     # transform the IMDb data using the transform_imdb_data function
#     new_movie_list = transform_imdb_data(old_file_name)
#
#     # open the new file for writing
#     with open(new_file_name, "w", newline='') as new_csv_file:
#         # create a CSV writer object
#         csv_writer = csv.writer(new_csv_file)
#         # use writerows method to write transformed data as a list of lists to new csv file
#         csv_writer.writerows(new_movie_list)
#
#
# # Call the create_new_imdb_file function to create the new CSV file
# create_new_imdb_file()

# --------------------------------------------------------------------------------------------


import csv


# Improved transformation of IMDb data using functions, and field names output to new file
def transform_imdb_data(old_file_name="imdbtitles.csv"):
    # create a list of lists to store the transformed data
    new_movie_list = []

    # open the original file
    with open(old_file_name, newline='') as csvfile:
        # create a CSV reader object
        movie_csv = csv.reader(csvfile, delimiter=",")

        for movie in movie_csv:
            # filter if the titleType column is 'movie' and the startYear column is greater than or equal to 2010
            if movie[0] == 'movie' and int(movie[4]) >= 2010:
                # append the selected columns to the new_movie_list
                new_movie_list.append([movie[0], movie[1], movie[4], movie[6], movie[7]])

    return new_movie_list


# Function to create a new IMDb CSV file
def create_new_imdb_file(old_file_name="imdbtitles.csv", new_file_name="new_version_of_imdbtitles.csv"):
    # transform the IMDb data using the transform_imdb_data function
    new_movie_list = transform_imdb_data(old_file_name)

    # Add the header row
    field_header_row = ["titleType", "primaryTitle", "startYear", "runtimeMinutes", "genres"]
    # use the insert method with index 0 to insert the field headings
    new_movie_list.insert(0, field_header_row)

    # open the new file for writing
    with open(new_file_name, "w", newline='') as new_csv_file:
        # create a CSV writer object
        csv_writer = csv.writer(new_csv_file)
        # use writerows method to write transformed data as a list of lists to new csv file
        csv_writer.writerows(new_movie_list)


# Call the create_new_imdb_file function to create the new CSV file
create_new_imdb_file()
