# Coffee machine project

from data import MENU, resources

def ShowReport (money = 0):
    """
    This function show all resources we have and money
    * water
    * milk
    * coffee
    * money
    """
    print ("the current resource values. e.g.")
    for key in resources:
        print (f"{key}: {resources [key]}")
    print (f"Money: ${money}")

def CheckResources (fla_drink = "", want_to_check = ""):
    """
    This function check if there is enough resources or not if:\n
    --> Yes
            : return True
    --> No
            : print there is no enough this resources
            : return False
    """
    if resources[want_to_check] >= MENU [fla_drink] ["ingredients"][want_to_check]:
        return True
    else:
        print (f"Sorry there is not enough {want_to_check}.")
        return False
    
def CheckMoney (client_money = 0, fla_drink = ""):
    if client_money >= MENU [fla_drink]["cost"]:
        return True
    else:
        print ("Sorry that's not enough money. Money refunded.")
        return False

def InputMoney ():
    quarters = int (input ("Please insert coins.\nhow many quarters?: "))
    dimes = int (input ("how many dimes?: "))
    nickles = int (input ("how many nickles: "))
    pennies = int (input ("how many pennies: "))
    total = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)

    return total

def AddPrice (fla_drink = "", currant_money = 0):
    return currant_money + MENU [fla_drink]["cost"]

def PrintChange (client_money = 0, fla_drink = 0):
    if client_money > MENU [fla_drink]["cost"]:
        print (f"Here is ${round (client_money - MENU[fla_drink]["cost"], 2)} in change.")

def DecreaseResources (fla_drink = ""):
    if fla_drink == "espresso":
        resources["water"] = resources["water"] - MENU["espresso"]["ingredients"]["water"]
        resources["coffee" ] = resources["coffee"] - MENU["espresso"]["ingredients"]["coffee"]
    else:
        resources["water"] = resources["water"] - MENU[fla_drink]["ingredients"]["water"]
        resources["coffee"] = resources["coffee"] - MENU[fla_drink]["ingredients"]["coffee"]
        resources["milk"] = resources["milk"] - MENU[fla_drink]["ingredients"]["milk"]


def EndClient ():
    PrintChange (client_money= total, fla_drink= input_)
    print (f"Here is your {input_} ☕️. Enjoy!")
    DecreaseResources (fla_drink= input_)


is_on = True
money = 0
while is_on:
    # Input from client
    input_ = input ("What would you like? (espresso/latte/cappuccino): ").lower ()

    if input_ == "off":
        is_on = False
        break
    
    elif input_ == "report":
        ShowReport (money= money)

    elif input_ == "espresso" or input_ == "latte" or input_ == "cappuccino":
        if input_ == "espresso":
            ok_1 =  CheckResources (fla_drink= input_, want_to_check= "water")
            ok_2 = CheckResources (fla_drink= input_, want_to_check= "coffee")
            if ok_1 == ok_2 == True:
                total = InputMoney ()
                ok_6 = CheckMoney (client_money= total, fla_drink= input_)
                if ok_6:
                    EndClient ()
                    money = AddPrice (fla_drink= input_, currant_money= money)

        else:
            ok_3 = CheckResources (fla_drink= input_, want_to_check= "water")
            ok_4 = CheckResources (fla_drink= input_, want_to_check= "milk")
            ok_5 = CheckResources (fla_drink= input_, want_to_check= "coffee")
            if ok_3 == ok_4 == ok_5 == True:
                total = InputMoney ()
                ok_6 = CheckMoney (client_money= total, fla_drink= input_)
                if ok_6:
                    EndClient ()
                    money = AddPrice (fla_drink= input_, currant_money= money)
