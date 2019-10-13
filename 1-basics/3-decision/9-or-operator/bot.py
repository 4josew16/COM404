print("What type of adventure should I have (scary, short, safe or long)?")
adventure = input()
if ((adventure == "scary") or (adventure =="short")):
    print("Entering the dark forest!")
    if ((adventure == "safe") or (adventure =="long")):
        print("Take the Safe Route")
else:
    print ("Not sure which route to take.")