# Function with outputs

def format_name (f_name, l_name): 
    if f_name == "" or l_name == "":
        return "You did not provide valid inputs!!!"

    return f_name.title () + " " +  l_name.title ()

print (format_name (input ("What is your first name? "), input ("What is your last name? ")))
