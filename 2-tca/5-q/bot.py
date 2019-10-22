#Create variable 
health=100
print("Your health is 100%. Escape is in progress...")
count=0

while count <5:
    print("Oh dear, who is that?")
    response=input()
    if response =="Smiler's Bot":
        print("Time to jam out of here!")
        health=health-20
    elif response=="Hacker":
        print("Yay! Better follow this one! ")
        health=health+20
    else:
        print("Phew, Just another emoji!")
    count = count + 1
print("Escaped! Health is ", health,"%" )
