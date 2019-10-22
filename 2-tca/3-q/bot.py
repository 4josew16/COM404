# Get user response
print("How many zones must I cross?")
zones_to_cross = int(input())
print("Crossing zones...")


while (zones_to_cross >0):
    print("…crossed zone" + str(zones_to_cross))
    zones_to_cross=zones_to_cross +1

print("Crossed all zones.  Jumanji!")
    