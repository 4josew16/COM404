# Decide where to look
print("Where should I look?")
place =input()

# Check the bedroom 
if (place=="in the bedroom"):
    print("Where in the bedroom should I look?")
    where_in_bedroom = input()
    if (where_in_bedroom =="under the bed"):
        print("Found some shoes but not battery")
    else:
        print("Found some mess but no battery")
        
# Check the bathroom
if (place=="in the bathroom"):
    print("Where in the bathroom should I look?")
    where_in_bathroom = input()
    if (where_in_bathroom=="in the bathtub"):
        print("Found a rubber duck but no battery")
    else:
        print("Found a wet surface but no battery")

# Check the lab
if (place=="in the lab"):
    print("Where in the lab should I look?")
    where_in_lab =input()
    if (where_in_lab=="on the table"):
        print("Yes I found my battery!")
    else:
        print("Found some tools but no battery")
# If an unknown place
else:
    print("I do not know what it is but I will keep looking")
    