# ask user to classify books 
print("What type of cover does the book have (hard or soft)?")
cover_type = input()
# decide if book i s hard or soft 
if (cover_type == "soft"):
    print("is it perfect bound (yes or no)?")
else:
    print("Book covers")
perfect_bound = input()
if (perfect_bound == "yes"): 
    print("Soft cover, perfect bound books are very popular!")
else:
    print("Soft covers with coils or stitches are great for short books")
