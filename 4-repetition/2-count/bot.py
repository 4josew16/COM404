#display the number of cables to avoid 
print("How many live cables should I avoid?")
answer = int(input())
live_cables = 1
count =1
while(live_cables <=answer):
    print("Avoiding...Done!" + str(live_cables) + "live cables avoided.")
    live_cables=live_cables + 1
print("All live cables avoided")
