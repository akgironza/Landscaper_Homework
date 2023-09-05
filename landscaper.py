# As you finish each function run pytest to see if the tests are passed

# GAME SETUP
user_input = input("You are starting a landscaping business, but all you have are your teeth. Would you like to proceed?")
print(user_input)

# Store game data in a dictionary
game_data = {
    "total": 0,
    "quit": False,
    "inventory": ["TEETH"]
    }

# Function to handle quitting game
def quit_game():
    game_data["quit"] = True
    
    if (game_data["quit"] == True):
        print("You have quit the game. Goodbye!")
    
    # replaces:     
        #if (user_input == "QUIT"):
            #game_data["quit"] = True

        #if (game_data["quit"] == True):
            #print("You have quit the game. Goodbye!")
            #break

# functions for other stuff including "what would you like to do?" and "use teeth"

# add items to inventory as they are purchased, incorporate into what shows to user

# PLAYER CAN USE TEETH
while (game_data["total"] < 5):
    user_input = (input("""
        What would you like to do?
            USE TEETH -- Spend the day cutting lawns with just your teeth and make $1. 
                (If you save up enough money, maybe you can get some tools...)
            QUIT -- Quit the game.
                           """))
    
    if (user_input == "QUIT"):
        quit_game()
        break

    if (user_input == "USE TEETH"):
        game_data["total"] += 1
        print(f"You now have a total of ${game_data['total']}")

# PLAYER CAN GET SCISSORS
    while (game_data["total"] >= 5):
        user_input = (input("""
            You have reached $5! What would you like to do?
                USE TEETH -- Spend the day cutting lawns with just your teeth and make $1. 
                You can do this as much as you want.
                GET SCISSORS -- Buy a pair of rusty scissors for $5.
                QUIT -- Quit the game    
                               """))
        if (user_input == "QUIT"):
            quit_game()
            break

        if (user_input == "USE TEETH"):
            game_data["total"] += 1
            print(f"You now have a total of ${game_data['total']}")

        if (user_input == "GET SCISSORS"):
            game_data["total"] -=5
            print(f"You now have a total of ${game_data['total']}. But with your rusty scissors you're moving up in the world!")

# PLAYER CAN USE SCISSORS
            while (True):
                user_input = (input("""
                    USE TEETH -- Spend the day cutting lawns with just your teeth and make $1.
                    USE SCISSORS -- Spend the day cutting lawns with your rusty scissors and make $5.
                    QUIT -- Quit the game    
                               """))
                
                if (user_input == "QUIT"):
                    quit_game()
                    break
                
                if (user_input == "USE TEETH"):
                    game_data["total"] += 1
                    print(f"You now have a total of ${game_data['total']}")
                    
                if (user_input == "USE SCISSORS"):
                    game_data["total"] +=5
                    print(f"You now have a total of ${game_data['total']}")

# PLAYER CAN GET PUSH LAWNMOWER  
                while (game_data["total"] >= 25):
                    user_input = (input("""
                        You have reached $25! What would you like to do?
                        USE TEETH -- Spend the day cutting lawns with just your teeth and make $1.
                        USE SCISSORS -- Spend the day cutting lawns with your rusty scissors and make $5.
                        GET PUSH LAWNMOWER -- Buy an old-timey lawnmower for $25.
                        QUIT -- Quit the game    
                               """))
                    
                    if (user_input == "QUIT"):
                        quit_game()
                        break

                    if (user_input == "USE TEETH"):
                        game_data["total"] += 1
                        print(f"You now have a total of ${game_data['total']}")

                    if (user_input == "USE SCISSORS"):
                        game_data["total"] +=5
                        print(f"You now have a total of ${game_data['total']}")

                    if (user_input == "GET PUSH LAWNMOWER"):
                        game_data["total"] -=25
                        print(f"You now have a total of ${game_data['total']}. But with your push lawnmower you're moving up in the world!")

# PLAYER CAN USE PUSH LAWNMOWER
                    while (True):
                        user_input = (input("""
                            USE TEETH -- Spend the day cutting lawns with just your teeth and make $1.
                            USE SCISSORS -- Spend the day cutting lawns with your rusty scissors and make $5.
                            USE LAWNMOWER -- Spend the day cutting lawns with your old-timey lawnmower and make $50.
                            QUIT -- Quit the game    
                               """))
                
                        if (user_input == "QUIT"):
                            quit_game()
                            break
                
                        if (user_input == "USE TEETH"):
                            game_data["total"] += 1
                            print(f"You now have a total of ${game_data['total']}")
                    
                        if (user_input == "USE SCISSORS"):
                            game_data["total"] +=5
                            print(f"You now have a total of ${game_data['total']}")

                        if (user_input == "USE LAWNMOWER"):
                            game_data["total"] +=50
                            print(f"You now have a total of ${game_data['total']}")

                    
                    



