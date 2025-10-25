import art

print (art.logo)

check = True

data_dictionary = {}

while check:


    name = input ("What is your name? ").lower()

    bid = int (input ("What is your bid?: $"))

    other = input ("Are there any other bidders? Type 'yes or 'no'.").lower()

    data_dictionary [name] = bid

    if other == "yes":
        check = True
        print ('\n' * 100)
    elif other == "no":
        check = False
        max_value = 0
        for key in data_dictionary:
            if data_dictionary[key] > max_value:
                max_value = data_dictionary[key]
                winner = key
        print (f"The winner is {winner} with a bid of ${max_value}.")
    else:
        print ("You types wrong!!!!")
