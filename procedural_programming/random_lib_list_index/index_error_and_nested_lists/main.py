us_states = [
    "Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut",
    "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa",
    "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan",
    "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire",
    "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio",
    "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota",
    "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", "West Virginia",
    "Wisconsin", "Wyoming"
]

# print (us_states[50]) ==> Error, because 50 out of range 0 --> 49

# Nested lists

names_men = ["Amr", "Abdo", "Ahmed"]
names_women = ["Aliaa", "Zahra", "Hagar"]

all_names = [names_men, names_women]

print (all_names)

print (all_names[1][1]) # Zahra

list = [0, 1, 2, 3, 4, 5]

print (list[1 : 3])