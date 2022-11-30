# Create a game that gives the user options to choose from. Based on a selected option, let them progress to another stage that ends the game or gives another set of options until they win the game.

print("Welcome to Tressure Island\nYour mission is to find the tressure.")

left_or_right = input("There are two mystical gates! One on the left and the other on the right, choose one. Left or Right? ")
if (left_or_right == "left") or (left_or_right == "Left"):
    print("You fell into an endless pit! Game!! Over!!!")
elif (left_or_right == "right") or (left_or_right == "Right"):
    lion_bear = input("There are two beast; a lion and a bear. You can only fight one of them so choose. Lion or Bear? ")
    if (lion_bear == "lion") or (lion_bear == "Lion"):
        print("You are not Samson! Game!! Over!!!")
    elif (lion_bear == "bear") or (lion_bear == "Bear"):
        door = input("There are three doors each having equal probability of holding the TREASURE.\nDoor 1 is guarded by a Goblin\nDoor two is guarded by a Hydra\nDoor three is guarded by Fafnir Dragon\nChoose one. 1 or 2 or 3? ")
        if door == 1:
            print("Sorry nobody will let a Goblin guard treasure since they will steal it themselves and can easily be tricked with Honey! Game!! Over!!!")
        elif door == 2:
            print("Sorry, you are never going to finish cutting of the head")
        else:
            print("Congratulation! Level one completed. You have a better chance of finding the treasure behind that door since Fafnir Dragon are usually used to guard treasure\nHere is a tip for the next Level (A simple strategy to beat Fafnir is to equip your party with Mirror Mail or cast Reflectga on your characters, then stand out of range behind the rocks so that Fafnir is forced to only cast Shock, Sleepga, and Silencega.)")








