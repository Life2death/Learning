 # 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi = round(weight/ height ** 2)
if bmi <18.5:
    print (f"your bmi is {bmi}, you are underweight")
elif bmi <25:
    print (f"your bmi is {bmi}, you have normalweight")
elif bmi <30:
    print (f"your bmi is {bmi}, you are overrweight")
elif bmi <35:
    print (f"your bmi is {bmi}, you are obese")
else:
    print (f"your bmi is {bmi}, you are c obese")
 