import pandas

all_data = pandas.read_csv ("./csv_files_pandas_lib/projects/great_squirrel_census/2018_central_park_squirrel_census_squirrel_data.csv")
num_grey = all_data [all_data["Primary Fur Color"] == "Gray"] 
num_cinnamon = all_data [all_data["Primary Fur Color"] == "Cinnamon"] 
num_black = all_data [all_data["Primary Fur Color"] == "Black"] 

data_dic = {
    "Fur Color" : ["grey", "red", "black"],
    "Count" : [len (num_grey), len (num_cinnamon), len (num_black)]
}

data_count = pandas.DataFrame (data_dic)
data_count.to_csv ("./csv_files_pandas_lib/projects/great_squirrel_census/new_data.csv")
