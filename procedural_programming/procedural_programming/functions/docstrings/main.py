# Docstring

def format_name (f_name, l_name): 
    """
    This function will take the first name and last name and format it to return the title case version of the name
    """
    if f_name == "" or l_name == "":
        return "You did not provide valid inputs!!!"

    return f_name.title () + " " +  l_name.title ()

print (format_name (input ("What is your first name? "), input ("What is your last name? ")))
