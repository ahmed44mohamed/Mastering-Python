
# CSV ===> Comma separated values


# with open ("weather_data.csv") as data_file:
#     data = data_file.readlines ()
#     print (data) # This will end with list with items end with \n


# import csv

# with open ("weather_data.csv") as data_file:
#     data = csv.reader (data_file)
#     temperatures = []
#     for row in data:
#         if row [1] != "temp": temperatures.append (int (row [1]))
#     print (temperatures)


import pandas


data = pandas.read_csv ("./csv_files_pandas_lib/reading_csv_files/weather_data.csv")

print (data)
print ("------------")
print (data["temp"])
print (data.condition)

