# Create first function 
def sum_weights (w1, w2):
    total_weight = (w1 + w2)
    print ("The sum of robot 1 and 2 " + str (total_weight))
    return (total_weight)

#create second function 
def calc_avg_weight (weight, weight1):
    average_weight = ((weight + weight1) //2)
    print ("The average weight of robot 1 and 2 " + str (average_weight))
    return(average_weight)

def run ():
    print("What is the weight of robot 1?")
    weight_1=int(input())
    print("What is the weight of robot 2?")
    weight_2=int(input())
    print("what would you like to calculate (sum or average)?")
    response =input()
    if response=="sum":
        sum_weights(weight_1, weight_2)
    else:
        calc_avg_weight(weight_1, weight_2)
run()









