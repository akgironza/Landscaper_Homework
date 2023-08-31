# As you finish each function run pytest to see if the tests are passed

# GAME SETUP
user_input = input("You are starting a landscaping business, but all you have are your teeth. Would you like to proceed?")
print(user_input)

# Store game data in a dictionary
game_data = {
    "total": 0,
    "quit": False
    }

while (game_data["total"] < 5):
    user_input = (input("""
        What would you like to do?
            USE TEETH -- Spend the day cutting lawns with just your teeth and make $1. 
                (If you save up enough money, maybe you can get some tools...)
            QUIT -- Quit the game.
                           """))
    if (user_input == "QUIT"):
        game_data["quit"] = True

    if (game_data["quit"] == True):
        print("You have quit the game. Goodbye!")
        break

    if (user_input == "USE TEETH"):
        game_data["total"] += 1
        print(f"You now have a total of ${game_data['total']}")

    while (game_data["total"] >= 5):
        user_input = (input("""
            You have reached $5! What would you like to do?
                USE TEETH -- Spend the day cutting lawns with just your teeth and make $1. 
                You can do this as much as you want.
                GET SCISSORS -- Buy a pair of rusty scissors for $5.
                QUIT -- Quit the game    
                               """))
        if (user_input == "QUIT"):
            game_data["quit"] = True

        if (game_data["quit"] == True):
            print("You have quit the game. Goodbye!")
            break

        if (user_input == "USE TEETH"):
            game_data["total"] += 1
            print(f"You now have a total of ${game_data['total']}")

        if (user_input == "GET SCISSORS"):
            game_data["total"] -=5
            print(f"You now have a total of ${game_data['total']}. But with your rusty scissors you're moving up in the world!")

            while (True):
                user_input = (input("""
                    USE TEETH -- Spend the day cutting lawns with just your teeth and make $1.
                    USE SCISSORS -- Spend the day cutting lawns with your rusty scissors and make $5.
                    QUIT -- Quit the game    
                               """))
                
                if (user_input == "QUIT"):
                    game_data["quit"] = True
                    
                if (game_data["quit"] == True):
                    print("You have quit the game. Goodbye!")
                    break
                
                if (user_input == "USE TEETH"):
                    game_data["total"] += 1
                    print(f"You now have a total of ${game_data['total']}")
                    
                if (user_input == "USE SCISSORS"):
                    game_data["total"] +=5
                    print(f"You now have a total of ${game_data['total']}")


    # At any point, if you are currently using your teeth, you can buy a pair of rusty scissors for $5. You can do this once, assuming you have enough money.

