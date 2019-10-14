cable_num=int(input("How many live cables must I avoid? "))
counter=0
while counter+1 <= cable_num:
    print("Avoiding.... Done!" + str((counter +1)) + "live cables have been avoided")
    counter +=1
print("All live cables have been avoided")