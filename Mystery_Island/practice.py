energy = 5


def player_energy():
    print(f"Your energy: {energy}")


def check_bridge():
    has_rope = True
    has_energy = False

    if has_rope and has_energy:
        print("You can cross")
    else:
        print("You cannot cross")


def loop_practice():
    while True:
        print("\n1. explore")
        print("2. check inventory")
        print("q. quit")

        choice = input("Enter your choice: ")

        if choice == "q":
            print("Good bye 👋")
            break

        elif choice == "1":
            explore()

            if energy <= 0:
                print("you have run out of energy. Game  over!")
                break

        elif choice == "2":
            print(inventory)
            
            # print("Your inventory is empty")

        else:
            print("Invalid choice")


def welcome_player():
    name = input("Player enter your name: ")
    print(f"Welcome {name}")
    print("You are stranded on a mysterious island.")
    print("Your mission is to restore the lighthouse.")


def reduce_energy():
    global energy

    if energy > 0:
        energy = energy - 1
        print(f"Energy remaining: {energy}")

        if energy == 0:
            print("Game over")
    else:
        print("You have no energy left!")


def check_energy():
    if energy == 0:
        print("Game over")
    else:
        print("You are still alive!")


def explore():
    print("You are exploring the island!")
    reduce_energy()


def move_player(location):
    choice = input("Where do you want to go? (q to quit): ")

    if choice == "q":
        print("Goodbye!")
        return location

    if location == "Beach" and choice == "Jungle":
        location = "Jungle"

    elif location == "Jungle" and choice == "Cave":
        location = "Cave"

    elif location == "Cave" and choice == "Old Bridge":
        location = "Old Bridge"

    elif location == "Old Bridge" and choice == "Lighthouse":
        location = "Lighthouse"

    else:
        print("You cannot move from here.")

    return location


def show_location(location):
    print(location)

inventory = []
inventory.append("Rope")
inventory.append("Lantern")


# Start the game
welcome_player()
player_energy()
check_bridge()
check_energy()
show_location("Jungle")
loop_practice()