#Read in user data
print ("what is your name human?")
name = input()
print ("what is your age?")
Age = int (input())
print ("What is your height?") 
height= float (input())
print ("what is your weight?")
weight = float (input())
BMI = weight/(height**2)
print ()
print (name + " you are " + str (Age) + " years old and your bmi is " + str (BMI))