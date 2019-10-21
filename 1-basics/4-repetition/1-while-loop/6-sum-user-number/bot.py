# Ask user for number
print("How many numbers should I sum up?")
answer =int(input())

# Create a control variable 
sum_1 = 0

print()

# create a variable for sum of numbers
total = 0

while sum_1 > =answer:
    print("Please enter number", answer, "of", sum_1, ":")
    number = int(input())
    total = total + number
    summed = summed + 1

#Display result 
print("The answer is", total)



 