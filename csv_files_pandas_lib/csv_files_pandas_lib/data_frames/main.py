import pandas

data = pandas.read_csv ("./csv_files_pandas_lib/data_frames/weather_data.csv")

# Two primary data structure of pandas
print (type (data)) # DataFrame
print (type (data ["temp"])) # Series

print ("---------------------")   

# Convert to dictionary
data_dic = data.to_dict ()
print (data_dic)

print ("---------------------")

# Convert to list and calc the avg for temp
temp_list = data["temp"].to_list ()
print (sum (temp_list) / len (temp_list)) # way 1
print (f"The Average: {data ["temp"].mean ()}") # way 2
print (f"Max num: {data['temp'].max ()}")
print (f"Min num: {data['temp'].min ()}")

print ("---------------------")

# Same way
print (data["condition"])
print (data.condition)

print ("---------------------")

# Get row
print ("Get row:")
print (data[data.day == "Monday"])

print ("---------------------")

# Get the row has max temp
print ("Get row has max temp:")
print (data[data.temp == data.temp.max ()])

print ("---------------------")

# Get value from row
print ("Get value from row:")
monday = data[data.day == "Monday"]
print (monday.condition)
temp_monday = monday.temp [0]
temp_monday_F = temp_monday * (9 / 5) + 32
print (temp_monday_F)

print ("---------------------")

# Create dataframe from scratch
data_dic = {
    "students" : ["Ahmed", "Bassam"],
    "scores" : [10, 20]
}

own_data = pandas.DataFrame (data_dic)
print (own_data)
print (type (own_data))
own_data.to_csv ("./csv_files_pandas_lib/data_frames/own_data.csv")

