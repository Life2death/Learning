print ("welcome to the roller coster")
height = int (input("whstd your height"))
age = int(input("whats your age "))

if height >= 120:
    print ("you can ride the roller coaster")
    if age < 12:
         print ("Please pay 5")
    elif age<=18:
        print ("Please pay 7")
    else:
        print ("Please pay 12")

else:
    print("please grow up ")
