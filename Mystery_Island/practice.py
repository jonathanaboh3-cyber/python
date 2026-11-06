# ==================================
# EXERCISE 1: PLAYER ENERGY
# ==================================

def player_energy():
    energy = 5
    print(energy)

player_energy()


# ==================================
# EXERCISE 2: CHECK THE BRIDGE
# ==================================

def check_bridge():
    has_rope = True
    has_energy = False

    if has_rope and has_energy:
        print("You can cross")
    else:
        print("You cannot cross")

check_bridge()


# ==================================
# EXERCISE 3: GAME MENU
# ==================================

def loop_practice():
    running = True

    while True:
        print("1. explore: ")
        print("2. check inventory: ")
        print("q. quit: ")

        choice = input("Enter your choice: ")

        if choice == "q":
            print("Good bye 👋")
            break

        elif choice == "1":
            print("You are exploring the island!: ")
        elif choice == "2":
            print("Your inventory is empty: ")
        else:
            print("Invalid choice")

loop_practice()

def welcome_player():
    name = input("Player enter your name: ")
    print(f"Welcome {name}")
    print("You are stranded on a mysterious island.")
    print("Your mission is to restore the lighthouse.")

welcome_player()
