# Adk user for the direction
print("Towards which direction should I paint?")
direction =input() 

# Decide which message to display
if(direction == "up"):
    print ("\n I am painting in the upward direction!")
elif(direction=="down"):
    print("\n I am painting in the downward direction!") 
elif(direction=="left"):
    print("\n I am painting towards the left")
elif(direction=="right"):
    print("\n I am painting towards the right")
else:
    print("\n Not sure which direction I am painting in!")