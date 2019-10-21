# Ask for user input 
print("How far are we from the cave?")
distance = int(input())

# Show count down
print()

for count in range(distance, 0, -1):
     print(count, "steps remaining")
print("We have reached the cave!")