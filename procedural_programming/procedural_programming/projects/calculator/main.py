import art

def Add (num_1 = 0.0, num_2 = 0.0): return num_1 + num_2

def Sub (num_1 = 0.0, num_2 = 0.0): return num_1 - num_2

def Mul (num_1 = 1.0, num_2 = 1.0): return num_1 * num_2

def Div (num_1 = 1.0, num_2 = 1.0): return num_1 / num_2

operations_dictionary = {
    "+" : Add,
    "-" : Sub,
    "*" : Mul,
    "/" : Div
}

child_check = True

parent_check = True

while parent_check:

    print (art.logo)

    first_num = float  (input ("What's the first number?: "))

    child_check = True

    while child_check:

        print ("+\n-\n*\n/")

        operation = input ("Pick an operation: ")

        next_num = float (input ("What's the next number?: "))

        def calc ():
            if operation == "+":
                return Add (first_num, next_num)
            elif operation == "-":
                return Sub (first_num, next_num)
            elif operation == "*":
                return Mul (first_num, next_num)
            elif operation == "/":
                return Div (first_num, next_num)
            else:
                return "You picked wrong operation !!!!!!!"

        print (f"{first_num}  {operation}  {next_num} = {calc ()}")

        ask_continue = input (f"Type 'y' to continue calculating with {calc ()}, or type 'n' to start a new calculation: ").lower()

        if ask_continue == "y":
            child_check = True
            first_num = calc ()
        else:
            child_check = False
            print ('\n' * 100)