# using return values 
# define bots characteristics 
name_1 = "Beep"
weight_1 = 12

name_2 = "Bop"
weight_2 = 20

total_weight = (weight_1 + weight_2)
average_weight = (total_weight /2)

# create function to calculate total weight of both bots 
def sum_weights(weight_1, weight_2):
    return total_weight

def calc_avg_weight(weight_1,weight_2):
    return average_weight

total_weight = (weight_1 + weight_2)
average_weight = (total_weight /2)

sum = total_weight
average = average_weight

def run():
    print("What is the weight of Beep?\n", weight_1)
    print("What is the weight of Bop?\n", weight_2)
    response=(input("Would you like to calculate (sum or average) "))
    if sum:
         print("The sum of Beep and Bop's weight is", total_weight)
    else: 
        if average:
            print("The average of Beep and Bop's weight is ", average_weight)
run()









