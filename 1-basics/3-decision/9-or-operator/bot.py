#Ask user for the type of adventure
print("What type of adventure should I have (scary, short, safe or long)?")
adventure = input()

#Determine what message to display
if ((adventure == "scary") or (adventure =="short")):
    print("Entering the dark forest!")
elif ((adventure == "safe") or (adventure =="long")):
    print("Take the Safe Route")
else:
    print ("Not sure which route to take.")