# Ask use for what they saw or heard
print("Did you hear a grrr or a hoot?")
sound = input()
print("Did you see  two red eyes or some big eyes?")
sight = input()
# Determine what message to display
if  (sound == "grrr") and (sight == "two red eyes" ):
    print("There is a scary creature. I should get out here!")
else:
    print("I am a little scared but I will continue.")