# Get user's name 
print("What is your name human?")
name=input()

#Get user's age
print("How old are you (in years?)")
age=int(input())

#Get user's height 
print("How tall are you (in meters?)")
height=float(input())

#Get user's weight 
print("How much do you weigh (in kilograms?)")
weight=float(input())
bmi=weight/(height**2)

print(name, "your bmi is", bmi)