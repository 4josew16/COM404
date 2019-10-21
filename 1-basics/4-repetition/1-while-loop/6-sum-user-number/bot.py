# Ask user for number
print("How many numbers should I sum up?")
num_sum =int(input())

# Create a control variable 
sum_1 = 1

print()

# sum of numbers
total = 0

while(sum_1 <=num_sum):
    print("Please enter number", sum_1, "of", num_sum, ":")
    number = int(input())
    total = total + number
    sum_1 = sum_1 + 1

#Display result 
print("The answer is", total)



 