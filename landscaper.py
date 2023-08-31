# As you finish each function run pytest to see if the tests are passed

# GAME SETUP
user_input = input("You are starting a landscaping business, but all you have are your teeth. Would you like to proceed?")
print(user_input)

# Store game data in a dictionary
game_data = {
    "total": 0,
    "quit": False
    }

while (True):
    user_input = int(input("""
                            What would you like to do?
                            1 -- Spend the day cutting lawns with just your teeth and make $1. 
                                You can do this as much as you want.
                            2 -- Quit the game.
                           """))
    if (user_input == 1):
        game_data["total"] += 1
        print(f"You now have a total of ${game_data['total']}")

    if (user_input == 2):
        game_data["quit"] = True
    
    if (game_data["quit"] == True):
        print("You have quit the game. Goodbye!")
        break