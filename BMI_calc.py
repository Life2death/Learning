 # 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi = float (weight) /float( height) ** 2
bmi_as_round = int(bmi)
print (bmi_as_round)