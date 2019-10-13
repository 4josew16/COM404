# get the user to enter a number 
print("Please enter the first number (must be between 1 and 10)") # create variable for first number 
first_number = int(input())
# get user to enter a second number
print("Please enter a second number (must be between 1 and 10)") # create a variable for the second number
second_number=int(input())
# create a comparison operator 
if (first_number>second_number):
    print("The first number is the biggest")
if (second_number<first_number):
    print("The second number is the smallest")
elif (first_number==second_number):
    print("Both are equal")


