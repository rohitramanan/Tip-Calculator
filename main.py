print ("Welcome to the tip calculator!!")
bill_amount = float(input("What was the total bill?"))
tip_amount = int(input("How much tip would you like to give? 10, 12 or 15?"))
people = int(input("How many people to split the bill?"))

tip = tip_amount/100
total_bill = bill_amount * tip + bill_amount
real_bill_total = total_bill/people
print (f"Each person pays ${real_bill_total}")
