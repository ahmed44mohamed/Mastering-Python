capitals = {
    "France" : "Paris",
    "Germany" : "Berlin"
}

# Nested list in dictionary

travel_log = {
    "France" : ["Paris", "Lille", "Dijon"],
    "Germany" : ["Stuttgart", "Berlin"]
}

print (travel_log["France"][1])


# Nested list inside list

nested_list = ["A", "B", ["C" , "D"]]

print (nested_list[2][1])


travel_log = {
    "France" : {
        "total_visited" : 12,
        "cities_visited" : ["Paris", "Lille", "Dijon"]
    },
    "Germany" : {
        "cities_visited" : ["Stuttgart", "Berlin", "Hamburg"],
        "total_visits" : 5
    }
}



print (travel_log["Germany"]["cities_visited"][2])
