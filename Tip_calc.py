print("welcome to tip calcy")
Total_bill = float(input("whats the total bill-->"))
perc_tip = float(input("% tip would you like to give-->"))
Bill_split = int(input ("how many people do you want to split-->"))
#print(type(perc_tip))

Tip_amt = Total_bill /perc_tip
print (Tip_amt)
Final_bill = Tip_amt + Total_bill
amt_per_person = round(Final_bill /Bill_split)
#print (amt_per_person)

 