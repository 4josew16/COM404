# work out number of odd and even numbers 
# get user response to questions 
print("Please enter a number between one and 10")
num_1=int (input())
if num_1%2==0:
    print("even")
else: 
    print("odd")
print("Please enter a second number betwween one and 10")
num_2=int (input())
if num_2%2==0:
    print("even")
else: 
    print("odd")
print("Please enter a third number betwween one and 10")
num_3=int (input())
if num_3%2==0:
    print("even")
else: 
    print("odd")
responses = [num_1,num_2,num_3]
count = responses.count('odd')
print("the countof odd is", count)