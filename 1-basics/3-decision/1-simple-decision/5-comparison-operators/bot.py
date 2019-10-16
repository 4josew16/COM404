# get the user to enter a number 
print("Please enter the first number") 

# create a variable for first number 
first_number = int(input())

# get user to enter a second number
print("Please enter a second number") 

# create a variable for the second number
second_number=int(input())

# Determine which message to display
if (first_number<second_number):
    print("\nThe first number is the smallest")
elif (second_number>first_number):
    print("\nThe second number is the smallest")
else: 
    print("\n The two numbers are equal.")


