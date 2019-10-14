#this is there to ask how many cables shouldbe avoided 
cable_num=int(input("How many live cables must I avoid? "))
#this variable is there because it is the thing that will be incramented in the loop could be called anything
counter=0
#this  is the while loop which starts the looping in the program
while counter+1 <= cable_num:
    #this is the line that prints out the statement that is asked
    print("Avoiding.... Done!" + str((counter +1)) + "live cables have been avoided")
    #this makes the counter go up by one
    counter +=1
print()
print("All live cables have been avoided")