live_cables=int(input("How many bars should be charged?"))
charging=0
message = "Charging █"
while (charging< live_cables):
    print(message)
    message = message + "█" 
    charging = charging + 1
print()
print("The battery is fully charged")
