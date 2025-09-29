print ("Welcome to the tip calculator!")
bill = float(input ("What is the total bill? $"))
tip = int(input ("How much tip would you like to give 10, 12, 0r 15? "))
people = int(input ("How many people o split the bill? "))
tip_as_percent = tip / 100
tip_amount = bill * tip_as_percent
bill_with_tip = bill + tip_amount
bill_per_person = bill_with_tip / people
final_bill = round(bill_per_person, 2)
print (f"Each person should pay: ${final_bill}")