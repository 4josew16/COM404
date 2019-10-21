# Ask for user input 
print("Please enter a number")
num_1=int(input())

#calculate factorial
count = 0
total =1

while (count < num_1):
    count = count + 1
    total = total * count

print("The factorial is", total)
