def is_league_united (hero_1, hero_2):
    if hero_1 =="Superman" and hero_2 =="Wonder Woman":
        return True
    else: 
        return False

        
def decide_plan (hero_1, hero_2):
    if is_league_united (hero_1, hero_2):
        return "Time to save the world!"
    else:
        return "We must unite the league!"

def run():
    print("Please enter the name of the first hero")
    hero_1= input()
    print("Please enter the name of the second hero")
    hero_2= input()
    print("Which league?")
    league = input()
    if league == "league":
        print (is_league_united (hero_1, hero_2))
    elif league == "plan": 
        print (decide_plan (hero_1, hero_2))

run()



  
