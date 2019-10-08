#declare a variable to count the number of cables to be removed 
print("How many cables should I remove?")
answer =int(input())
#display the current count
removed_cables =1
while (removed_cables <= answer):
    removed_cables = removed_cables + 1
    print("removed_cables")