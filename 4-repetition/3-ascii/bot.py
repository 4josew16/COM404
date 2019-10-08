print("How many bars should be charged?")
answer = int(input())
message = "Charging █"
charging = 0
while (charging < answer):
    print(message)
    message = message + " █"
    charging = charging +1
print("The battery is fully charged" "█")
